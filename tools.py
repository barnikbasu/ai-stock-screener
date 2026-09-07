import yfinance as yf


def get_stocks(
    screen_type: str,
    offset: int = 0,
    size: int = 10,
) -> list[dict]:
    """
    Fetch stocks from a Yahoo Finance predefined screener.

    Args:
        screen_type: Yahoo Finance screener name.
        offset: Starting position for pagination.
        size: Number of stocks to return.

    Returns:
        A list of dictionaries containing stock information.
    """

    available_screeners = yf.PREDEFINED_SCREENER_QUERIES

    if screen_type not in available_screeners:
        available = ", ".join(available_screeners.keys())
        raise ValueError(
            f"Unknown screener '{screen_type}'. "
            f"Available screeners: {available}"
        )

    query = available_screeners[screen_type]["query"]

    result = yf.screen(
        query,
        offset=offset,
        size=size,
    )

    fields = [
        "symbol",
        "shortName",
        "exchange",
        "regularMarketPrice",
        "regularMarketChangePercent",
        "marketCap",
        "fiftyTwoWeekHigh",
        "fiftyTwoWeekLow",
        "averageAnalystRating",
    ]

    stocks = []

    for stock in result.get("quotes", []):
        stocks.append(
            {
                key: stock.get(key)
                for key in fields
                if key in stock
            }
        )

    return stocks