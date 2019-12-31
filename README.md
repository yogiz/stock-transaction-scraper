# stock-transaction-scraper

Scrape stock market data transaction (currently from Indopremier) including transaction depth (bid-offer price and lot)  with BeautifulSoup and requests

This scraping data will be used for machine learning. Becouse I can't find any stock database that included market transaction depth, so I am planning to scrape data by myself.

# How To Use It?

## Requirements

This scraper used `Python 3`.

If you plan to use this scraper, you need these library to be installed to your machine:

- BeautifulSoup, install with `pip install bs4 `
- pandas, install with `pip install pandas `
- pendulum, install with `pip install pendulum `

Install all prerequisites with thsi coommand :

` pip install -r requirements.txt `

Or if you in linux

` pip3 install -r requirements.txt `

## Start Scraping

You can see the file `example.py` to see how you can start using this scraper. Just modify the stock symbol with any IHSG symbol. Or you can tweak it to scrape many stock at the same time. Up to you ;) 

## Result Data

The script will be create a csv file or in stock.db (sqllite3) with any stock symbol you scrape.

## Usage Tips

Use vps server and then run using crontab, so you can scrape regularly for example every 5 minutes
