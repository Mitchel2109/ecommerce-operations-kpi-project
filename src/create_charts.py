from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

SALES_DATA_PATH = PROJECT_ROOT / "data" / "sales_only_retail.csv"
CHARTS_DIR = PROJECT_ROOT / "reports" / "charts"

MONTHLY_REVENUE_CHART = CHARTS_DIR / "monthly_revenue_trend.png"
TOP_COUNTRIES_CHART = CHARTS_DIR / "top_countries_by_revenue.png"


def format_pounds(value):
    return f"GBP {value:,.0f}"


def create_monthly_revenue_chart(df):
    monthly_revenue = (
        df.groupby("year_month", as_index=False)["Revenue"]
        .sum()
        .sort_values("year_month")
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        monthly_revenue["year_month"],
        monthly_revenue["Revenue"],
        marker="o",
        linewidth=2,
        color="#2F5597",
    )

    ax.set_title("Monthly Revenue Trend", fontsize=14, pad=12)
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.tick_params(axis="x", rotation=45)
    ax.yaxis.set_major_formatter(lambda value, position: format_pounds(value))
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    fig.tight_layout()
    fig.savefig(MONTHLY_REVENUE_CHART, dpi=150)
    plt.close(fig)


def create_top_countries_chart(df):
    top_countries = (
        df.groupby("Country", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
        .head(10)
        .sort_values("Revenue")
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        top_countries["Country"],
        top_countries["Revenue"],
        color="#70AD47",
    )

    ax.set_title("Top Countries by Revenue", fontsize=14, pad=12)
    ax.set_xlabel("Revenue")
    ax.set_ylabel("Country")
    ax.xaxis.set_major_formatter(lambda value, position: format_pounds(value))
    ax.grid(axis="x", linestyle="--", alpha=0.4)

    fig.tight_layout()
    fig.savefig(TOP_COUNTRIES_CHART, dpi=150)
    plt.close(fig)


def main():
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(SALES_DATA_PATH)

    create_monthly_revenue_chart(df)
    create_top_countries_chart(df)

    print("Charts created:")
    print(f"- {MONTHLY_REVENUE_CHART}")
    print(f"- {TOP_COUNTRIES_CHART}")


if __name__ == "__main__":
    main()
