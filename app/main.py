import asyncio
import csv
from datetime import datetime

from app.drivers.api_requester import ApiRequester


async def main_get_top200():
    api = ApiRequester()
    repos = await api.get_top1000_git_repositories(keyword="stars:>1000", num_repos=200)
    print(f"{len(repos)} repositórios salvos em CSV.")

def extract_metrics(prs):
    metrics = []
    for pr in prs:
        if not pr.get("created_at") or not pr.get("closed_at"):
            continue

        created = datetime.fromisoformat(pr["created_at"].replace("Z", "+00:00"))
        closed = datetime.fromisoformat(pr["closed_at"].replace("Z", "+00:00"))
        time_diff = (closed - created).total_seconds() / 3600  # horas

        # pegar detalhes do PR (linhas e arquivos)
        additions = pr.get("additions", 0)
        deletions = pr.get("deletions", 0)
        files_changed = pr.get("changed_files", 0)
        description_len = len(pr.get("body") or "")

        metrics.append({
            "id": pr["id"],
            "state": pr["state"],
            "additions": additions,
            "deletions": deletions,
            "files_changed": files_changed,
            "description_length": description_len,
            "analysis_time_h": time_diff,
        })
    return metrics

def save_metrics_to_csv(metrics, filename="prs_metrics.csv"):
    keys = metrics[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(metrics)

if __name__ == "__main__":
    # Etapa 1 - Buscar top 200 repositórios
    asyncio.run(ApiRequester.get_top1000_git_repositories("stars:>1000", num_repos=200))

    # Etapa 2 - Exemplo: pegar PRs de 1 repositório e gerar dataset
    api = ApiRequester()
    owner, repo = "microsoft", "vscode"  # exemplo
    prs = api.get_pull_requests(owner, repo)
    metrics = extract_metrics(prs)
    save_metrics_to_csv(metrics, "vscode_prs_metrics.csv")
    print(f"Coletadas {len(metrics)} métricas de PRs do {repo}.")