
from flask import Flask, render_template
from scraper import scrape_top_gainers
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():

    stocks = []
    error = None
    fetched_at = None

    try:
        # Fetch stock data from BSE
        stocks = scrape_top_gainers()

        # Check whether records were extracted
        if stocks:
            fetched_at = datetime.now().strftime(
                "%d-%m-%Y %I:%M:%S %p"
            )
        else:
            error = (
                "No stock data received from BSE. "
                "Please try refreshing the dashboard."
            )

    except Exception as e:
        error = f"Unable to fetch BSE data: {str(e)}"

    return render_template(
        "index.html",
        stocks=stocks,
        error=error,
        fetched_at=fetched_at
    )


if __name__ == "__main__":
    app.run(debug=True)
