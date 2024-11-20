stock_symbol = Element("stock_symbol")
stock_chart_img = Element("stock_chart")
site_links = Element("site_links")
news_link_template = Element("site_link_template").select(".news_link", from_content=True)

sites = {
    "FinViz": "https://www.finviz.com/quote.ashx?t={}",
    "ChartMill": "https://www.chartmill.com/stock/quote/{}/fundamental-analysis",
    "ChartMill (Income Statement)": "https://www.chartmill.com/stock/quote/{}/financials/income-statement",
    "ChartMill (Analyst Ratings)": "https://www.chartmill.com/stock/quote/{}/analyst-ratings",
    "GuruFocus": "https://www.gurufocus.com/stock/{}/financials",
    "GuruFocus (Ownership)": "https://www.gurufocus.com/stock/{}/ownership",
    "MarketChameleon": "https://marketchameleon.com/Overview/{}/",
    "BarChart (Price)": "https://www.barchart.com/stocks/quotes/{}/overview",
    "BarChart (Options)": "https://www.barchart.com/stocks/quotes/{}/options",
    "BarChart (Put/Call Ratio)": "https://www.barchart.com/stocks/quotes/{}/put-call-ratios",
    "BarChart (Income Statement)": "https://www.barchart.com/stocks/quotes/{}/income-statement/annual",
    "BarChart (Filings)": "https://www.barchart.com/stocks/quotes/{}/sec-filings",
    "StockInvest": "https://stockinvest.us/technical-analysis/{}",
    "TradingView": "https://www.tradingview.com/chart/?symbol={}",
    "SeekingAlpha": "https://seekingalpha.com/symbol/{}",
    "SwingTradeBot": "https://swingtradebot.com/equities/{}",
    "StockTwits (Sentiments)": "https://stocktwits.com/symbol/{}",
    "Y Finance": "https://finance.yahoo.com/quote/{}/holders?p=ZZZ",
    "OAI Earnings": "https://tools.optionsai.com/earnings/{}",
    "OptionStrat (Long Call)": "https://optionstrat.com/build/long-call/{}",
    "TipRanks": "https://www.tipranks.com/stocks/{}/forecast",
    "TipRanks (Analysis)": "https://www.tipranks.com/stocks/{}/stock-analysis",
    "TipRanks (Hedge Fund)": "https://www.tipranks.com/stocks/{}/hedge-funds",
    "ETF Holdings": "https://etfdb.com/stock/{}/",
}


def show_stock():
    symbol_entered = stock_symbol.element.value
    stock_chart_img.element.src = f"https://charts.finviz.com/chart.ashx?t={symbol_entered}&p=d&ta=sma_20,sma_50,sma_200"

    site_links.element.innerText = ""

    for site_key, site_url in sites.items():
        news_link_copy = news_link_template.clone()
        news_link_copy.element.text = site_key
        news_link_copy.element.href = site_url.format(symbol_entered)

        site_links.element.appendChild(news_link_copy.element)
        site_links.element.appendChild(js.document.createTextNode(" | "))

    stock_symbol.element.focus()
    stock_symbol.element.setSelectionRange(0, len(stock_symbol.element.value))


if js.location.search and len(js.location.search.split("symbol=")) > 1:
    symbol = js.location.search.split("symbol=")[1].split("&")[0]
    stock_symbol.element.value = symbol
    show_stock()
else:
    stock_symbol.element.value = "AAPL"
    show_stock()


def show_stock_if_enter(e):
    if e.key == "Enter":
        show_stock()


stock_symbol.element.onkeypress = show_stock_if_enter
