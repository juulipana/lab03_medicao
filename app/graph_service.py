import pandas as pd
from matplotlib import pyplot as plt


class GraphService:

    @staticmethod
    def analyze_pr_size_feedback(csv_path: str, save_path: str | None = None):
        """
        Analisa a relação entre o tamanho dos PRs e o feedback (comentários/reviews),
        removendo outliers para melhor visualização.
        """
        # 1️⃣ Ler o dataset
        df = pd.read_csv(csv_path)

        # 2️⃣ Criar métricas principais
        df["total_changes"] = df["additions"] + df["deletions"]
        df["total_feedback"] = df["comments"] + df["reviews"]

        # 3️⃣ Calcular correlação (usando todos os dados)
        corr = df["total_changes"].corr(df["total_feedback"])
        print(f"📊 Correlação entre tamanho do PR e feedback: {corr:.3f}")

        # 4️⃣ Remover outliers apenas para visualização
        q95 = df["total_changes"].quantile(0.95)
        df_filtered = df[df["total_changes"] <= q95]

        print(f"🔎 Visualizando apenas PRs com até {int(q95):,} alterações (95 % menores).")

        # 5️⃣ Plotar gráfico
        plt.figure(figsize=(8, 5))
        plt.scatter(df_filtered["total_changes"], df_filtered["total_feedback"], alpha=0.6)
        plt.title("Relação entre tamanho do PR e feedback (RQ1, sem outliers)")
        plt.xlabel("Tamanho do PR (additions + deletions)")
        plt.ylabel("Feedback (comentários + revisões)")
        plt.grid(True, linestyle="--", alpha=0.6)

        if save_path:
            plt.savefig(save_path, bbox_inches="tight", dpi=300)
            print(f"🖼️ Gráfico salvo em {save_path}")
        else:
            plt.show()

        # 6️⃣ Retornar informações úteis
        return {
            "correlation": corr,
            "avg_changes": df["total_changes"].mean(),
            "avg_feedback": df["total_feedback"].mean(),
            "n_prs": len(df),
            "visualized_prs": len(df_filtered)
        }