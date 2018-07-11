import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# driver = webdriver.Chrome('C:\\Users\\Joe\\Desktop\\chromedriver_win32\\chromedriver')
# driver.get("http://www.google.com")

#specifying the url
yelptop30 = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Austin%2C+TX'
page = requests.get(yelptop30)
soup = BeautifulSoup(page.text, 'html.parser')
names = str(soup.find_all("a", class_="biz-name js-analytics-click"))
print(names)

newlist = list()
newlist.append(names)
for elem in newlist:
        newlist.extend(elem.rstrip().split('<span class="indexed-biz-name">'))
print(newlist)
