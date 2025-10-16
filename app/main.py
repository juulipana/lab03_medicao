import asyncio
import csv
import os
import time
from app.drivers.api_requester import ApiRequester
from app.graph_service import GraphService


async def main():
    # Etapa 1 — Buscar top 200 repositórios (e salvar CSV)
    repos = await ApiRequester.get_top1000_git_repositories(keyword="stars:>1000", num_repos=200)
    if not repos:
        print("❌ Nenhum repositório retornado.")
        return

    print(f"✅ {len(repos)} repositórios salvos em CSV.")

    # Etapa 2 — Coletar PRs dos 200 repositórios e consolidar métricas
    api = ApiRequester()
    all_metrics = []
    i = 0
    for repo in repos:
        i+=1
        full_name = repo.get("full_name")
        if not full_name or "/" not in full_name:
            continue

        owner, name = full_name.split("/")
        print(f"\n📦 Coletando PRs de {owner}/{name}...")

        try:
            prs = api.get_pr_data(owner, name, num_prs=100)
            if not prs:
                print(f"⚠️ Nenhum PR retornado de {owner}/{name}")
                continue

            metrics = api.extract_pr_metrics(prs)

            # adiciona nome do repo para identificar no CSV final
            for m in metrics:
                m["repo"] = f"{owner}/{name}"

            all_metrics.extend(metrics)
            print(f"✅ {len(metrics)} PRs coletados de {owner}/{name}")

            # evita rate limit
            time.sleep(1.2)
            if i == 20:
                break
        except Exception as e:
            print(f"❌ Erro ao processar {owner}/{name}: {e}")
            continue

    # Etapa 3 — Salvar dataset consolidado
    if all_metrics:
        output_file = "dataset_top200_repos_prs.csv"
        api.save_to_csv(all_metrics, output_file)
        print(f"\n📊 Dataset final salvo em {output_file}")
        print(f"Total de {len(all_metrics)} PRs coletados de {len(repos)} repositórios.")
    else:
        print("\n⚠️ Nenhum PR coletado de nenhum repositório.")


if __name__ == "__main__":
    csv_path = "dataset_top200_repos_prs.csv"

    GraphService.analyze_pr_size_feedback(
        csv_path, save_path="rq1_pr_size_feedback.png"
    )
    GraphService.analyze_analysis_time_feedback(
        csv_path, save_path="rq2_analysis_time_feedback.png"
    )
    GraphService.analyze_description_feedback(
        csv_path, save_path="rq3_description_feedback.png"
    )
    GraphService.analyze_interactions_feedback(
        csv_path, save_path="rq4_interactions_feedback.png"
    )

    GraphService.analyze_pr_size_reviews(csv_path, "rq5_pr_size_reviews.png")
    GraphService.analyze_analysis_time_reviews(csv_path, "rq6_analysis_time_reviews.png")
    GraphService.analyze_description_reviews(csv_path, "rq7_description_reviews.png")
    GraphService.analyze_interactions_reviews(csv_path, "rq8_interactions_reviews.png")

    print("\n✅ Todos os gráficos RQ1–RQ4 foram gerados e salvos com sucesso!")
