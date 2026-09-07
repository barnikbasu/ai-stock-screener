def rank_stocks(stocks: list[dict]) -> list[dict]:
    """
    Rank stocks using a simple deterministic scoring system.

    This is a technical demonstration and is NOT financial advice.
    """

    ranked = []

    for stock in stocks:

        score = 0

        price = stock.get("regularMarketPrice")
        high = stock.get("fiftyTwoWeekHigh")
        low = stock.get("fiftyTwoWeekLow")

        # ----------------------------------------
        # 52-WEEK PRICE POSITION
        # ----------------------------------------

        if (
            price is not None
            and high is not None
            and low is not None
            and high > low
        ):

            position = (price - low) / (high - low)

            if position < 0.30:
                score += 2

            elif position < 0.50:
                score += 1

        # ----------------------------------------
        # ANALYST RATING
        # ----------------------------------------

        rating = stock.get("averageAnalystRating")

        if rating:

            rating_text = str(rating).lower()

            if "strong buy" in rating_text:
                score += 3

            elif "buy" in rating_text:
                score += 2

        # ----------------------------------------
        # SAVE SCORE
        # ----------------------------------------

        stock_copy = dict(stock)

        stock_copy["score"] = score

        ranked.append(stock_copy)

    # Highest score first
    ranked.sort(
        key=lambda stock: stock["score"],
        reverse=True
    )

    return ranked


def format_report(stocks: list[dict]) -> str:

    if not stocks:
        return "No stocks found."

    lines = [
        "",
        "=" * 80,
        "STOCK SCREENING RESULTS",
        "=" * 80,
        "",
    ]

    for index, stock in enumerate(stocks, start=1):

        symbol = stock.get(
            "symbol",
            "N/A"
        )

        name = stock.get(
            "shortName",
            "Unknown"
        )

        price = stock.get(
            "regularMarketPrice",
            "N/A"
        )

        score = stock.get(
            "score",
            0
        )

        lines.append(
            f"{index:>2}. "
            f"{symbol:<8} "
            f"{str(name)[:30]:<30} "
            f"Price: {str(price):<12} "
            f"Score: {score}"
        )

    lines.extend([
        "",
        "=" * 80,
        "Rule-based screening only — NOT financial advice.",
        "",
    ])

    return "\n".join(lines)