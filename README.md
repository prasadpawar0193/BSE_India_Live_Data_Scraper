
# BSE India Live Data Scraper and Dashboard

## 1. Project Overview

This project is a Python-based web scraping application that collects live Top Gainers stock information from the official BSE India website and displays it through a Flask web dashboard.

The application extracts stock information and presents it in a structured table.

## 2. Features

- Scrapes Top Gainers data from BSE India.
- Extracts Security Code, Company Name, Last Traded Price (LTP), and Change Percentage.
- Uses Selenium to open and load the BSE website.
- Uses BeautifulSoup to parse HTML and extract stock information.
- Displays extracted data through a Flask web application.
- Provides a refresh button to fetch updated data.
- Displays the last successful fetch timestamp.
- Shows error messages when data cannot be retrieved.
- Supports responsive dashboard styling.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Selenium | Browser automation |
| BeautifulSoup | HTML parsing |
| Flask | Backend web framework |
| HTML | Dashboard structure |
| CSS | Dashboard styling |

## 4. Project Structure

```text
Project_1_BSE_Scraper/
│
├── scraper.py
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## 5. Installation

### Step 1: Clone or download the project

Open the project folder in VS Code.

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Configure Chrome

Make sure Google Chrome is installed. Selenium uses Chrome to open the BSE website.

## 6. How to Run the Project

### Option 1: Run the scraper independently

```bash
python scraper.py
```

This opens the BSE website, extracts stock information, and prints the results in the terminal.

### Option 2: Run the Flask dashboard

```bash
python app.py
```

Open the following URL in your browser:

http://127.0.0.1:5000/

The dashboard displays the extracted BSE Top Gainers information.

## 7. Project Workflow

1. The user opens the Flask dashboard.
2. Flask executes the home route.
3. The application calls the `scrape_top_gainers()` function.
4. Selenium opens the official BSE Top Gainers webpage.
5. BeautifulSoup parses the webpage HTML.
6. The scraper identifies the required table columns.
7. Python extracts the stock records.
8. Flask passes the extracted records to the HTML template.
9. The dashboard displays the stock information.
10. The user can click Refresh Data to fetch the latest available information.

## 8. Extracted Data Fields

| Field | Description |
|---|---|
| Security Code | Unique BSE security code |
| Company Name | Stock/company name |
| LTP | Last Traded Price |
| Change % | Percentage change in stock price |

## 9. Error Handling

The application includes basic error handling:

- Handles scraping exceptions.
- Displays an error message when stock data is unavailable.
- Displays a no-data message if no matching records are extracted.
- Saves debugging files (`bse_debug.html` and `bse_debug.png`) to help inspect website responses.

## 10. Important Notes

- Data is fetched from the BSE website when the dashboard is opened or refreshed.
- The application does not automatically refresh in the background.
- Successful scraping depends on BSE website availability and access permissions.
- The extracted data reflects the information returned by BSE at the time of fetching.

## 11. Conclusion

This project demonstrates practical implementation of web scraping, browser automation, HTML parsing, Python backend development, and Flask-based dashboard development using BSE India market data.

# BSE_India_Live_Data_Scraper
Live BSE India stock market data scraper and Flask dashboard using Selenium and BeautifulSoup.
