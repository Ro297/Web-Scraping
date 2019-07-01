from lxml import html
import requests
import pandas as pd
import os
from selenium import webdriver
import time

def data_to_csv(data, filename, key):
	df = pd.DataFrame.from_dict(data).reset_index().set_index('index')
	writer = open(os.path.join(filename), "a")#, encoding="utf-8")
	csv_data = df.to_csv()
	writer.write(key)
	writer.write('\n')
	writer.write(csv_data)
	writer.close()

def tender_details():
	home = 'https://www.tenderdetail.com/Indian-tender/'
	keywords = ['Data','Technology','MIS','Information-Systems','IT','Information-Technology','Monitoring','Impact']
	ext = '-tenders'

	for key in keywords:
		page = requests.get(home+key+ext)
		tree = html.fromstring(page.content)

		title = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "workDesc", " " ))]//span[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')

		#description = tree.xpath("//*[(@id = 'listing')]//p//span/text()")

		prices = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "price", " " ))]/text()')

		#state = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "state", " " ))]/text()')
		
		date = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "dd", " " ))]/span//text()')
		date = [ x+' '+y+' '+z for x,y,z in zip(date[0::3], date[1::3], date[2::3])]

		link = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "viewnotice", " " ))]//@href')
		link = ['https://www.tenderdetail.com'+x for x in link[0::1]]

		data_dict= {
			'Tender Name': title,
			#'Description': description,
			'Price': prices,
			#'State': state,
			'Date': date,
			'Link': link
			}

		filename= f"tenderdetails.csv"
		data_to_csv(data_dict, filename, key)

def adb():
	home = 'https://www.adb.org/projects/tenders?terms='  
	ext = '&sort_by=field_date_content&sort_order=DESC'
	keywords = ['Data','Technology','MIS','Information+Systems','IT','Information+Technology','Monitoring','Impact']

	for key in keywords:
		page = requests.get(home+key+ext)
		tree = html.fromstring(page.content)

		title = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "item-title", " " ))]/text()')
		title = [x.encode("utf-8") for x in title[1::2]]

		link = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "item-title", " " ))]//@href')
		link = ['https://www.adb.org'+x for x in link]

		date = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "item-meta", " " ))]//div/text()')
		date = [x for x in date[1::2]]

		data_dict= {
			'Tender Name': title,
			'Date': date,
			'Link': link
			}

		filename= f"adb.csv"
		data_to_csv(data_dict, filename, key)

def worldbank():
	home = 'http://projects.worldbank.org/procurement/procurementsearch?lang=en&qterm='
	keywords = ['Data','Technology','MIS','Information+Systems','IT','Information+Technology','Monitoring','Impact']
	ext = '&srce=both'
	for key in keywords:
		driver.get(home+key+ext)
		driver.implicitly_wait(20)
		python_button = driver.find_element_by_id('downloadsearchresults')
		python_button.click()

def devnetjobs():
	home = 'http://www.devnetjobsindia.org/rfp_assignments.aspx'
	keywords = ['Data','Technology','MIS','IT','Monitoring','Impact']
	
	for key in keywords:
		driver.get(home)
		search_box = driver.find_element_by_id('ContentPlaceHolder1_txtKeywords') 
		search_box.send_keys(key)
		python_button = driver.find_element_by_id('ContentPlaceHolder1_imgSearchJob')
		python_button.click()
		content = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "datacontent", " " ))] | //*[(@id = "ContentPlaceHolder1_SearchView1_grdJobs")]//tr[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//td')
		text = content.text.splitlines()
		text = text[1:-1]
		title = [x for x in text[0::3]]
		description = [x for x in text[1::3]]
		temp = [x for x in text[2::3]]
		location = [x.split('Apply by:')[0] for x in temp]
		location = [x.split('Location:')[1] for x in location]
		date = [x.split('Apply by:')[1] for x in temp]

		print(len(title))
		print(len(description))
		print(len(location))
		print(len(date))

		data_dict= {
		'Tender Name': title,
		'Description': description,
		'Location': location,
		'Apply by': date,
		}


		filename= f"devnetjobs.csv"
		data_to_csv(data_dict, filename, key)

if __name__ == '__main__':
	tender_details()
	adb()
	driver = webdriver.Chrome('C:/Users/Rohan/Documents/chromedriver')
	devnetjobs()
	worldbank()
	driver.quit()
	print("done")	