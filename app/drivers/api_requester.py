import csv
from datetime import datetime
import requests
import json

TOKEN = ""

class ApiRequester:

    @staticmethod
    async def get_top1000_git_repositories(keyword: str, num_repos: int = 1000):
        headers = {
            "Authorization": f"token {TOKEN}"
        }

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
                items = data.get("items", [])
                all_repos.extend(items)

            filename = f"repos_{keyword}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "name", "full_name", "stars", "language",
                    "created_at", "updated_at", "open_issues", "html_url"
                ])
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

    @staticmethod
    def get_top100_git_repositories():
        headers = {"Authorization": f"token "}
        url = "https://api.github.com/graphql"
        params = {
            "q": "stars:>1 sort:stars-desc",
            "first": 100
        }

        query = """
        query TopRepos($q: String!, $first: Int!) {
          search(query: $q, type: REPOSITORY, first: $first) {
            repositoryCount
            pageInfo { hasNextPage endCursor }
            edges {
              node {
                ... on Repository {
                  nameWithOwner
                  url
                  stargazerCount
                  createdAt
                  updatedAt
                  pushedAt
                  primaryLanguage { name }
                  releases { totalCount }
                  pullRequests(states: MERGED) { totalCount }
                  openIssues: issues(states: OPEN) { totalCount }
                  closedIssues: issues(states: CLOSED) { totalCount }
                }
              }
            }
          }
        }
        """
        response = requests.post(url, json={"query": query, "variables": params}, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print("Top 100 repositórios coletados com sucesso!")
            with open("repos_100.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            return data
        else:
            print("Erro:", response.status_code, response.text)
            return None

    @staticmethod
    def get_repo_details(owner: str, name: str):
        """Consulta detalhes de 1 repositório usando GraphQL"""
        headers = {"Authorization": f"token {TOKEN}"}
        url = "https://api.github.com/graphql"

        query = """
            query RepoDetails($owner: String!, $name: String!) {
              repository(owner: $owner, name: $name) {
                nameWithOwner
                url
                stargazerCount
                createdAt
                updatedAt
                primaryLanguage { name }
                releases { totalCount }
                pullRequests(states: MERGED) { totalCount }
                openIssues: issues(states: OPEN) { totalCount }
                closedIssues: issues(states: CLOSED) { totalCount }
              }
            }
            """

        variables = {"owner": owner, "name": name}

        response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)

        if response.status_code == 200:
            data = response.json()
            repo = data.get("data", {}).get("repository", {})
            return repo
        else:
            print("Erro:", response.status_code, response.text)
            return None

    @staticmethod
    def get_pull_requests(owner: str, repo: str, per_page: int = 50):
        headers = {"Authorization": f"token {TOKEN}"}
        base_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        params = {
            "state": "all",
            "per_page": per_page
        }
        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Erro ao buscar PRs de {repo}: {response.text}")
            return []
        return response.json()