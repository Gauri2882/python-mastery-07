# python-mastery-07 - Data Projects

Comprehensive collection of **7 parts** that teach practical data skills using Python — from numerical linear algebra and data cleaning to visualization, time-series analysis, web scraping, and working with external APIs. This README **explicitly documents every folder and every file** you provided.

📚 Past Repositories

[python-mastery-01](https://github.com/Gauri2882/python-mastery-01): basics – Core Python syntax, data types, and control structures.

[python-mastery-02](https://github.com/Gauri2882/python-mastery-02): intermediate – Functions, modules, file handling, and error handling.

[python-mastery-03](https://github.com/Gauri2882/python-mastery-03): OOP – Classes, objects, inheritance, polymorphism.

[python-mastery-04](https://github.com/Gauri2882/python-mastery-04): data-handling – Pandas, NumPy, CSV/JSON handling.

[python-mastery-05](https://github.com/Gauri2882/python-mastery-05): tkinter – GUI development using Tkinter.

[python-mastery-06](https://github.com/Gauri2882/python-mastery-06): flask – Flask + HTML Templates + CSS + Jinja2

---

## 🚀 At a glance

* **Purpose:** A step-by-step series of small projects and scripts for learning practical data tasks in Python.
* **Structure:** `part-01` → `part-07` (each part contains scripts and small projects).
* **Audience:** Beginners to intermediate learners who want hands-on practice.

---

## ⚙️ Requirements

Install the core packages used across parts:

```bash
pip install numpy pandas matplotlib seaborn requests beautifulsoup4
```

(If you prefer a `requirements.txt`, create one with the above packages.)

---

## 📂 Full folder & file breakdown (exact — nothing omitted)

### **Part-01** — Matrix operations & Matrix Calculator

* `part-01/01_python-data.py` — **Matrix operations with NumPy**

  * Creates 2×2 matrices, demonstrates addition, subtraction, element-wise multiplication, dot product, transpose, determinant and inverse (if invertible).

* `part-01/02_python-data.py` — **Handling user input for matrices**

  * `get_matrix()` reads rows/cols and row values from STDIN and returns a NumPy array.

* `part-01/03_python-data.py` — **Project: Matrix Calculator**

  * Interactive CLI project using `get_matrix()` and `matrix_operations()` to perform addition, subtraction, element-wise multiplication, dot product, transpose, determinant and inverse with error handling.

---

### **Part-02** — Data analysis & cleaning with Pandas

* `part-02/04_python-data.py` — **Pandas quick exploration & cleaning demo**

  * Loads `part-02/data.csv`, prints head, shape, dtypes, summary stats, null counts. Demonstrates filling NAs, dropping rows, deduplication, transformations, normalization and renaming columns.
  * **Requires:** `part-02/data.csv` (sample CSV).

* `part-02/05_python-data.py` — **Project: Data Cleaner**

  * CLI tool: `load_data()`, `clean_data()`, `save_data()`.
  * Prompts user for input/output file paths and writes cleaned CSV.

---

### **Part-03** — Data visualization with Matplotlib

* `part-03/06_python-data.py` — **Creating basic plots**

  * Examples: line plot, bar chart, scatter plot. Uses `plt.show()` for interactive display.

* `part-03/07_python-data.py` — **Customizing graphs**

  * Demonstrates plot styling, annotations, subplots and grid.

* `part-03/08_python-data.py` — **Plotting from data files**

  * Loads `part-03/data.csv` (expects columns `X` and `Y`) and plots.
  * **Requires:** `part-03/data.csv`.

* `part-03/09_python-data.py` — **Project: Graph Plotter**

  * Interactive CLI: choose graph type, input manually or load CSV, plot and optionally save to file.

---

### **Part-04** — Sales data analysis & reporting

* `part-04/10_python-data.py` — **Loading and exploring sales data**

  * Loads `part-04/sales_data.csv`, checks missing values, type conversions, feature engineering (`Year_Month`, `Revenue`), groups monthly sales and top products, and plots monthly sales.
  * **Requires:** `part-04/sales_data.csv`.

* `part-04/11_python-data.py` — **Project: Sales Report Analyzer**

  * CLI: prompts for CSV path, runs `load_data()`, `clean_data()`, `analyze_data()` and visualizes monthly sales and top products.

---

### **Part-05** — Time-series (temperature) analysis

* `part-05/12_python-data.py` — **Plotting temperature trends**

  * Loads `part-05/temperature_data.csv`, uses seaborn style, saves plots, detects anomalies (±2σ) and computes a 7-day rolling average.
  * **Requires:** `part-05/temperature_data.csv`.

* `part-05/13_python-data.py` — **Project: Temperature Plotter**

  * CLI: load CSV, plot trends with rolling averages and anomalies, optionally save the plot.

---

### **Part-06** — Web scraping & live tracking

* `part-06/14_python-data.py` — **Understanding web scraping basics**

  * Uses `requests` and `BeautifulSoup` to fetch and parse pages. Example: attempt to extract stock info from Google Finance markup and an example `track_stock_price()` loop.
  * **Note:** scraping Google Finance by scraping HTML is brittle — class names and structure change frequently.

* `part-06/15_python-data.py` — **Project: Stock Price Tracker**

  * CLI: prompts user for ticker and interval, repeatedly fetches the stock price and prints it. Requires internet.
  * **Caution:** Respect target website's terms of service and robots.txt; prefer official APIs where possible.

---

### **Part-07** — API integration & dashboard (weather)

* `part-07/16_python-data.py` — **Weather data fetch + plotting**

  * Uses OpenWeatherMap API (`API_KEY` required) to fetch current weather, prints a small summary, plots a simulated 5-day trend and runs a `compare_weather()` bar chart for multiple cities.
  * **Requires:** An OpenWeatherMap API key set in `API_KEY` or environment variable.

* `part-07/17_python-data.py` — **Project: Global Weather Dashboard**

  * CLI menu: (1) view weather for a city, (2) compare multiple cities, (3) exit. Uses the same OpenWeatherMap API.

---

## 🔎 Important notes & troubleshooting

* **Missing CSVs:** Parts 02, 03, 04 and 05 expect sample CSV files at the paths shown (e.g., `part-02/data.csv`, `part-03/data.csv`, `part-04/sales_data.csv`, `part-05/temperature_data.csv`). Provide these or edit the script to point to your data.

* **APIs & keys:** Parts in `part-07` require an OpenWeatherMap API key. Do not commit API keys to public repos. Use environment variables, e.g.:

```bash
export OPENWEATHER_API_KEY='your_key_here'   # macOS/Linux
setx OPENWEATHER_API_KEY "your_key_here"   # Windows (restart terminal)
```

* **Web scraping caution:** `part-06` scrapes Google Finance HTML. The structure of the page may change; consider using a public stock API (e.g., Alpha Vantage, Yahoo Finance APIs) for reliability.

* **Saving plots:** Many scripts call `plt.show()`; to save plots, use the interactive prompt or edit the script to call `plt.savefig('file.png')` before `plt.show()`.

* **Long-running loops:** `part-06/14_python-data.py` and `part-06/15_python-data.py` may run indefinite loops. Use `Ctrl+C` to stop.

---

## ✅ Suggested `requirements.txt`

```
numpy
pandas
matplotlib
seaborn
requests
beautifulsoup4
```

---

## ✍️ Next steps (optional extras you might want me to add)

* Add inline code snippets / short examples for each script's main functions.
* Include sample CSV files or a `data-samples/` folder with small example files.
* Add badges (Python version, license) and a short CONTRIBUTING section.
* Create a single `run_all.sh` or `Makefile` to execute selected demos.

---
