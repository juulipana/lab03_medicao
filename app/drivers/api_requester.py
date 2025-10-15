import csv
import time
from datetime import datetime
import requests

TOKEN = ""

class ApiRequester:

    @staticmethod
    async def get_top1000_git_repositories(keyword: str, num_repos: int = 1000):
        headers = {"Authorization": f"token {TOKEN}"}
        base_url = "https://api.github.com/search/repositories"
        all_repos = []
        per_page = 100
        total_pages = (num_repos // per_page)

        try:
            for page in range(1, total_pages + 1):
                params = {
                    "q": keyword,
                    "sort": "stars",
                    "order": "desc",
                    "per_page": per_page,
                    "page": page
                }
                response = requests.get(base_url, headers=headers, params=params)
                response.raise_for_status()
                data = response.json()
                all_repos.extend(data.get("items", []))
                time.sleep(1)  # evita rate limit

            filename = f"repos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "full_name", "stars", "language",
                                 "created_at", "updated_at", "open_issues", "html_url"])
                for repo in all_repos:
                    writer.writerow([
                        repo.get("name"),
                        repo.get("full_name"),
                        repo.get("stargazers_count"),
                        repo.get("language"),
                        repo.get("created_at"),
                        repo.get("updated_at"),
                        repo.get("open_issues_count"),
                        repo.get("html_url")
                    ])
            return all_repos

        except requests.RequestException as e:
            print("Erro:", e)
            return None

    # ⚙️ GraphQL - retorna PRs ricos (para suas RQs)
    @staticmethod
    def get_pr_data(owner: str, repo: str, num_prs: int = 100):
        url = "https://api.github.com/graphql"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        query = """
        query($owner: String!, $repo: String!, $numPRs: Int!) {
          repository(owner: $owner, name: $repo) {
            pullRequests(first: $numPRs, states: [MERGED, CLOSED], orderBy: {field: CREATED_AT, direction: DESC}) {
              nodes {
                number
                title
                state
                merged
                createdAt
                closedAt
                mergedAt
                additions
                deletions
                changedFiles
                bodyText
                comments { totalCount }
                reviews { totalCount }
                commits { totalCount }
                author { login }
              }
            }
          }
        }
        """

        variables = {"owner": owner, "repo": repo, "numPRs": num_prs}
        r = requests.post(url, json={"query": query, "variables": variables}, headers=headers)

        if r.status_code == 200:
            data = r.json()
            try:
                return data["data"]["repository"]["pullRequests"]["nodes"]
            except (TypeError, KeyError):
                print(f"Nenhum PR retornado de {owner}/{repo}")
                return []
        else:
            print(f"Erro: {r.status_code} - {r.text}")
            return []

    @staticmethod
    def extract_pr_metrics(prs):
        metrics = []
        for pr in prs:
            created = datetime.fromisoformat(pr["createdAt"].replace("Z", "+00:00"))
            closed = datetime.fromisoformat(pr["closedAt"].replace("Z", "+00:00")) if pr["closedAt"] else None
            analysis_time_h = (closed - created).total_seconds() / 3600 if closed else None

            body_len = len(pr.get("bodyText") or "")

            metrics.append({
                "number": pr["number"],
                "state": pr["state"],
                "merged": pr["merged"],
                "additions": pr["additions"],
                "deletions": pr["deletions"],
                "changed_files": pr["changedFiles"],
                "description_length": body_len,
                "analysis_time_h": analysis_time_h,
                "comments": pr["comments"]["totalCount"],
                "reviews": pr["reviews"]["totalCount"],
                "commits": pr["commits"]["totalCount"],
            })
        return metrics

    @staticmethod
    def save_to_csv(metrics, filename="prs_dataset.csv"):
        if not metrics:
            print("⚠️ Nenhum dado para salvar.")
            return
        keys = metrics[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(metrics)
        print(f"✅ {len(metrics)} PRs salvos em {filename}")
