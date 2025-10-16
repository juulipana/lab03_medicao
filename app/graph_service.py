import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class GraphService:

    @staticmethod
    def _load_and_prepare(csv_path: str):
        """Carrega o dataset e cria colunas auxiliares."""
        df = pd.read_csv(csv_path)
        df["total_changes"] = df["additions"] + df["deletions"]
        df["total_feedback"] = df["comments"] + df["reviews"]
        return df

    @staticmethod
    def _plot_relation(df, x_col, y_col, title, xlabel, ylabel, save_path=None, filter_outliers=True):
        """Função genérica de plot com filtro de outliers e correlação."""
        # Filtrar outliers se necessário
        if filter_outliers:
            q95 = df[x_col].quantile(0.95)
            df_plot = df[df[x_col] <= q95]
        else:
            df_plot = df

        corr = df[x_col].corr(df[y_col])
        print(f"📈 Correlação entre {xlabel} e {ylabel}: {corr:.3f}")

        plt.figure(figsize=(8, 5))
        plt.scatter(df_plot[x_col], df_plot[y_col], alpha=0.6)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True, linestyle="--", alpha=0.6)

        if save_path:
            plt.savefig(save_path, bbox_inches="tight", dpi=300)
            print(f"🖼️ Gráfico salvo em {save_path}")
        else:
            plt.show()

        return {"correlation": corr, "visualized_prs": len(df_plot)}

    # 🧩 RQ1 — Tamanho x Feedback
    @staticmethod
    def analyze_pr_size_feedback(csv_path: str, save_path=None):
        df = GraphService._load_and_prepare(csv_path)
        return GraphService._plot_relation(
            df,
            x_col="total_changes",
            y_col="total_feedback",
            title="RQ1 — Relação entre tamanho do PR e feedback",
            xlabel="Tamanho do PR (additions + deletions)",
            ylabel="Feedback (comentários + revisões)",
            save_path=save_path
        )

    # ⏱️ RQ2 — Tempo de análise x Feedback
    @staticmethod
    def analyze_analysis_time_feedback(csv_path: str, save_path=None):
        df = GraphService._load_and_prepare(csv_path)
        df = df.dropna(subset=["analysis_time_h"])  # remover PRs sem fechamento

        return GraphService._plot_relation(
            df,
            x_col="analysis_time_h",
            y_col="total_feedback",
            title="RQ2 — Relação entre tempo de análise e feedback",
            xlabel="Tempo de análise (horas)",
            ylabel="Feedback (comentários + revisões)",
            save_path=save_path
        )

    # 📝 RQ3 — Descrição x Feedback
    @staticmethod
    def analyze_description_feedback(csv_path: str, save_path=None):
        df = GraphService._load_and_prepare(csv_path)

        return GraphService._plot_relation(
            df,
            x_col="description_length",
            y_col="total_feedback",
            title="RQ3 — Relação entre descrição e feedback",
            xlabel="Tamanho da descrição (caracteres)",
            ylabel="Feedback (comentários + revisões)",
            save_path=save_path
        )

    # 💬 RQ4 — Interações x Feedback
    @staticmethod
    def analyze_interactions_feedback(csv_path: str, save_path=None):
        df = GraphService._load_and_prepare(csv_path)
        df["total_interactions"] = df["comments"] + df["reviews"] + df["commits"]

        return GraphService._plot_relation(
            df,
            x_col="total_interactions",
            y_col="total_feedback",
            title="RQ4 — Relação entre interações e feedback",
            xlabel="Interações totais (comentários + revisões + commits)",
            ylabel="Feedback (comentários + revisões)",
            save_path=save_path
        )

# --- RQ5 ---
    @staticmethod
    def analyze_pr_size_reviews(csv_path: str, save_path: str | None = None):
            """
            RQ5. Relação entre tamanho do PR e número de revisões realizadas.
            Mostrado como gráfico de dispersão com linha de tendência.
            """
            df = pd.read_csv(csv_path)
            df["total_changes"] = df["additions"] + df["deletions"]

            corr = df["total_changes"].corr(df["reviews"])
            print(f"📊 RQ5: Correlação (tamanho do PR x revisões): {corr:.3f}")

            q95 = df["total_changes"].quantile(0.95)
            df = df[df["total_changes"] <= q95]

            plt.figure(figsize=(8, 5))
            sns.regplot(data=df, x="total_changes", y="reviews", scatter_kws={'alpha': 0.6})
            plt.title(f"RQ5 — Tamanho do PR x Revisões (r = {corr:.2f})")
            plt.xlabel("Tamanho do PR (additions + deletions)")
            plt.ylabel("Número de revisões")
            plt.grid(True, linestyle="--", alpha=0.5)

            if save_path:
                plt.savefig(save_path, bbox_inches="tight", dpi=300)
            else:
                plt.show()

    # --- RQ6 ---
    @staticmethod
    def analyze_analysis_time_reviews(csv_path: str, save_path: str | None = None):
            """
            RQ6. Relação entre tempo de análise dos PRs e número de revisões realizadas.
            Mostrado com boxplot (tempo em intervalos).
            """
            df = pd.read_csv(csv_path)
            df = df[df["analysis_time_h"].notnull()]
            df["analysis_time_days"] = df["analysis_time_h"] / 24

            # Categorizar tempos (faixas)
            bins = [0, 1, 3, 7, 14, 30, 9999]
            labels = ["<1d", "1–3d", "3–7d", "7–14d", "14–30d", ">30d"]
            df["time_range"] = pd.cut(df["analysis_time_days"], bins=bins, labels=labels)

            plt.figure(figsize=(8, 5))
            sns.boxplot(data=df, x="time_range", y="reviews", color="skyblue")
            plt.title("RQ6 — Tempo de análise x Revisões")
            plt.xlabel("Tempo de análise (dias)")
            plt.ylabel("Número de revisões")
            plt.grid(True, axis="y", linestyle="--", alpha=0.5)

            if save_path:
                plt.savefig(save_path, bbox_inches="tight", dpi=300)
            else:
                plt.show()

        # --- RQ7 ---
    @staticmethod
    def analyze_description_reviews(csv_path: str, save_path: str | None = None):
            """
            RQ7. Relação entre descrição dos PRs e número de revisões realizadas.
            Usando gráfico de dispersão logarítmico.
            """
            df = pd.read_csv(csv_path)
            df["description_length"] = df["description_length"].fillna(0)

            corr = df["description_length"].corr(df["reviews"])
            print(f"📊 RQ7: Correlação (descrição x revisões): {corr:.3f}")

            q95 = df["description_length"].quantile(0.95)
            df = df[df["description_length"] <= q95]

            plt.figure(figsize=(8, 5))
            plt.scatter(df["description_length"], df["reviews"], alpha=0.6)
            plt.xscale("log")
            plt.title(f"RQ7 — Comprimento da descrição x Revisões (r = {corr:.2f})")
            plt.xlabel("Comprimento da descrição (log)")
            plt.ylabel("Número de revisões")
            plt.grid(True, linestyle="--", alpha=0.5)

            if save_path:
                plt.savefig(save_path, bbox_inches="tight", dpi=300)
            else:
                plt.show()

        # --- RQ8 ---
    @staticmethod
    def analyze_interactions_reviews(csv_path: str, save_path: str | None = None):
            """
            RQ8. Relação entre interações (comentários) e número de revisões realizadas.
            Usando heatmap de densidade (2D histogram).
            """
            df = pd.read_csv(csv_path)
            df["interactions"] = df["comments"] + df["commits"]

            corr = df["interactions"].corr(df["reviews"])
            print(f"📊 RQ8: Correlação (interações x revisões): {corr:.3f}")

            plt.figure(figsize=(7, 5))
            sns.kdeplot(
                data=df,
                x="interactions",
                y="reviews",
                fill=True,
                cmap="Blues",
                thresh=0.05,
            )
            plt.title(f"RQ8 — Interações x Revisões (r = {corr:.2f})")
            plt.xlabel("Interações (comentários + commits)")
            plt.ylabel("Número de revisões")

            if save_path:
                plt.savefig(save_path, bbox_inches="tight", dpi=300)
            else:
                plt.show()