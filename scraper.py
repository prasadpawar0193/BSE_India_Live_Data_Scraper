
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


# BSE Top Gainers URL
BSE_URL = (
    "https://www.bseindia.com/markets/equity/"
    "eqreports/mktwatchr?filter=gainer*all$all$"
)


def scrape_top_gainers():

    # Step 1: Configure Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    results = []

    try:
        # Step 2: Open BSE website
        print("Opening BSE website...")
        driver.get(BSE_URL)

        # Step 3: Wait for page to load
        time.sleep(10)

        print("Page title:", driver.title)

        # Step 4: Get website HTML
        page_source = driver.page_source

        # Step 5: Save debug files
        driver.save_screenshot("bse_debug.png")

        with open("bse_debug.html", "w", encoding="utf-8") as file:
            file.write(page_source)

        # Step 6: Parse HTML
        soup = BeautifulSoup(page_source, "html.parser")

        tables = soup.find_all("table")

        print("Number of tables found:", len(tables))

        # Step 7: Find the stock table
        for table in tables:

            rows = table.find_all("tr")

            if len(rows) < 2:
                continue

            # Extract table headers
            headers = [
                cell.get_text(" ", strip=True).lower()
                for cell in rows[0].find_all(["th", "td"])
            ]

            print("Table headers:", headers)

            # Find required column indexes
            def find_column(keywords):
                for index, header in enumerate(headers):
                    if any(word in header for word in keywords):
                        return index
                return None

            code_col = find_column(
                ["security code", "scrip code", "code"]
            )

            company_col = find_column(
                ["security name", "company name", "company"]
            )

            ltp_col = find_column(
                ["ltp", "last traded price"]
            )

            change_col = find_column(
                ["% chg", "chg %", "change %", "% change", "percent change"]
            )

            # Check required columns
            if None in [
                code_col,
                company_col,
                ltp_col,
                change_col
            ]:
                continue

            # Step 8: Extract stock details
            for row in rows[1:]:

                cells = row.find_all(["td", "th"])

                required_index = max(
                    code_col,
                    company_col,
                    ltp_col,
                    change_col
                )

                if len(cells) <= required_index:
                    continue

                stock = {
                    "security_code": cells[code_col].get_text(
                        " ", strip=True
                    ),
                    "company_name": cells[company_col].get_text(
                        " ", strip=True
                    ),
                    "ltp": cells[ltp_col].get_text(
                        " ", strip=True
                    ),
                    "change_percent": cells[change_col].get_text(
                        " ", strip=True
                    )
                }

                results.append(stock)

            if results:
                break

        # Step 9: Display extracted records
        print("\n========== BSE TOP GAINERS ==========")

        if results:
            for stock in results:
                print(stock)
        else:
            print("No stock records extracted.")
            print("Check bse_debug.html and bse_debug.png")

        print("\nTotal records:", len(results))

        return results

    except Exception as e:
        print("Scraping error:", str(e))
        return results

    finally:
        # Step 10: Close browser
        driver.quit()


# Run scraper
if __name__ == "__main__":
    scrape_top_gainers()