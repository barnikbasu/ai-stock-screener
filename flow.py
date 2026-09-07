from typing import TypedDict

from langgraph.graph import START, END, StateGraph

from tools import get_stocks
from screener import rank_stocks, format_report


class State(TypedDict):
    screen_type: str
    stocks: list[dict]
    ranked_stocks: list[dict]
    report: str


def fetch_stocks(state: State):
    """Fetch stock data from Yahoo Finance."""

    stocks = get_stocks(
        screen_type=state["screen_type"],
        offset=0,
        size=10,
    )

    return {
        "stocks": stocks
    }


def rank_results(state: State):
    """Rank stocks using a deterministic scoring system."""

    ranked = rank_stocks(
        state["stocks"]
    )

    return {
        "ranked_stocks": ranked
    }


def create_report(state: State):
    """Create the final stock screening report."""

    report = format_report(
        state["ranked_stocks"]
    )

    return {
        "report": report
    }


graph_builder = StateGraph(State)

graph_builder.add_node(
    "fetch_stocks",
    fetch_stocks
)

graph_builder.add_node(
    "rank_results",
    rank_results
)

graph_builder.add_node(
    "create_report",
    create_report
)

graph_builder.add_edge(
    START,
    "fetch_stocks"
)

graph_builder.add_edge(
    "fetch_stocks",
    "rank_results"
)

graph_builder.add_edge(
    "rank_results",
    "create_report"
)

graph_builder.add_edge(
    "create_report",
    END
)

graph = graph_builder.compile()


if __name__ == "__main__":

    print()
    print("=" * 60)
    print("             AI STOCK SCREENER")
    print("=" * 60)
    print()

    print("Available screeners:")
    print()
    print("1. day_gainers")
    print("2. day_losers")
    print("3. most_actives")
    print("4. growth_technology_stocks")
    print("5. undervalued_growth_stocks")
    print("6. undervalued_large_caps")
    print("7. small_cap_gainers")
    print("8. most_shorted_stocks")
    print()

    screen_type = input(
        "Enter screener: "
    ).strip()

    try:

        result = graph.invoke(
            {
                "screen_type": screen_type,
                "stocks": [],
                "ranked_stocks": [],
                "report": "",
            }
        )

        print(result["report"])

    except Exception as error:

        print()
        print(f"Error: {error}")