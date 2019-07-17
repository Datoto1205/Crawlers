## Crawler of Top 10 headlines of Wall Street Journal with Chinese Version
I tried to fetch the HTML code from the website “Wall Street Journal with Chinese version”. Afterward, I tried to decode the code and obtain some useful information, which included the title and the link of top ten news. I applied the package of “requests” and “BeautifulSoup” in this file.





## Crawler of Search Result in Baidu
I tried to collect what user want to search, and I use the keywords I store to get the website address. Afterwards, I download the HTML code from the particular website address, decode the HTML code and gain some information I want, which included the title and the link of the search result in the browser “Baidu”, a browser which was used in China. I applied the package of “requests” and “BeautifulSoup” in this file.





## Crawler of Stock Price in Taiwan Stock Market
I tried to get the stock codes from an excel file first so that I could assemble website addresses I want. Afterward, I download the HTML code from the particular website address, decode the HTML code and gain some financial data of the day, which included open price, close price, highest price and lowest price of stocks. I acquired all the financial data from Yahoo Finance, and the package I used included “pandas”, “requests” and “BeautifulSoup”. After you download the file “Crawler of Stock Price in Taiwan Stock Market.py” and the folder “Supporting Files”, you could run the codes with the terminal directly if you have installed python in your laptop. (The file "Crawler of Stock Price in Taiwan Stock Market.ipynb" in the folder "ipynb files" also could finish the same works, but it required jupyter notebook, another IDE, to run the code.)

(Note: This file is only used for demonstration of my ability of python, I do not guarantee the accuracy of the data, please do not use it for the real investment in the capital market!!!)
