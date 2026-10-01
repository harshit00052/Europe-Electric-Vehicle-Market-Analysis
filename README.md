# Electric Vehicle (EV) Data Scraping Project

## Overview

This project focuses on collecting electric vehicle (EV) data from [EV Database](https://ev-database.org/) using Python, Selenium, and BeautifulSoup.

The objective is to build a structured dataset containing information about electric vehicle specifications, performance, pricing, and country-wise availability. The scraped data can be used for exploratory data analysis (EDA), market research, and understanding trends in the electric vehicle industry.

## Objectives

* Automate the collection of electric vehicle data from EV Database.
* Extract technical specifications and performance metrics.
* Collect vehicle pricing information across different European countries.
* Handle missing values and structure the extracted data.
* Create a dataset suitable for further analysis and visualization.

## Technologies Used

| Technology       | Purpose                            |
| ---------------- | ---------------------------------- |
| Python           | Core programming language          |
| Selenium         | Browser automation and pagination  |
| BeautifulSoup    | HTML parsing and data extraction   |
| Pandas           | Data organization and manipulation |
| NumPy            | Handling missing values            |
| Jupyter Notebook | Development and experimentation    |

## Data Collection

The data was scraped from [EV Database](https://ev-database.org/), which provides detailed information about electric vehicles.

The scraping process involved:

1. Accessing the EV Database website using Selenium.
2. Extracting vehicle information from the HTML source.
3. Parsing HTML elements using BeautifulSoup.
4. Collecting specifications, performance metrics, and pricing details.
5. Automating pagination to navigate through multiple pages.
6. Handling missing or unavailable information using NumPy.
7. Organizing the extracted information into structured lists and a Pandas DataFrame.

## Dataset Features

The dataset contains the following attributes:

### Vehicle Information

* **name:** Name of the electric vehicle.
* **crRange:** Real-world driving range.
* **efficiency:** Energy consumption per 100 km.
* **weight:** Vehicle weight.
* **acceleration:** Acceleration time from 0 to 100 km/h.
* **one_15_min_Stop_Range:** Long-distance driving range including a 15-minute charging stop.
* **battery_Cap:** Battery capacity.
* **fast_charge:** Fast-charging speed.
* **towing_cap:** Maximum towing capacity.
* **cargo_vol:** Cargo volume.
* **price_per_range:** Price relative to driving range.

### Country-Wise Pricing

* **germany_a:** Additional pricing information for Germany.
* **germany_p:** Vehicle price in Germany.
* **netherlands_a:** Additional pricing information for the Netherlands.
* **netherlands_p:** Vehicle price in the Netherlands.
* **united_kingdom_a:** Additional pricing information for the United Kingdom.
* **united_kingdom_p:** Vehicle price in the United Kingdom.

*Note: The additional pricing fields store tooltip information extracted from the website, while the corresponding price fields store the displayed pricing text.*

## Project Structure

```text
EV-Data-Scraping/
│
├── datasets/
│   └── ev_dataset.csv
│
├── notebooks/
│   └── ev_data_scraping.ipynb
│
├── README.md
└── requirements.txt
```

*Update the file and folder names according to your actual repository structure.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd EV-Data-Scraping
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Notebook

Open the Jupyter Notebook and execute the cells to explore the scraping process.

## Applications

The collected dataset can be used for:

* Analyzing the relationship between battery capacity and driving range.
* Comparing EV efficiency across manufacturers.
* Studying the relationship between vehicle price and performance.
* Comparing electric vehicle prices across countries.
* Identifying trends in battery technology and charging capabilities.
* Building interactive dashboards for EV market analysis.
* Developing machine learning models for price prediction.

## Key Learnings

Through this project, I gained practical experience in:

* Automating web interactions using Selenium.
* Extracting structured information from HTML using BeautifulSoup.
* Implementing pagination in web scraping workflows.
* Handling missing and inconsistent data.
* Organizing scraped data using Pandas and NumPy.
* Building an end-to-end data collection pipeline.

## Data Source

[EV Database – Electric Vehicle Specifications and Comparison](https://ev-database.org/)

**Disclaimer:** This project is intended for educational and analytical purposes. All data belongs to its respective source. Please respect the website's terms of use and scraping policies.

---

**Author:** Harshit Kumar

**Domain:** Data Analytics | Web Scraping | Python
