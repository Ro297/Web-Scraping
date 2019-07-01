# Web-Scraping
Web scraping 4 websites to populate an excel file with tender details

Install python 3 latest version based on your operating system type from https://www.python.org/download/releases/3.0/

After installing python3,
1. For windows, open command prompt in the folder with the requirements.txt file and enter the following command "pip install -r requirements.txt"

2. In the python script - tenderscraper.py,

3.```python
__name__ == '__main__':
	driver = webdriver.Chrome('C:/Users/Rohan/Documents/chromedriver') # <----- EDIT THIS PATH TO THE PATH OF THE FOLDER THE CHROMEDRIVER IS IN eg: C:/Users/Madhav/Webscraper/chromedriver
```
4. Run the python script - tenderscraper.py
