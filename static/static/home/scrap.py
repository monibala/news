from bs4 import BeautifulSoup
import requests
url = "https://www.bing.com/shop?q=Camera+On+Flipkart&FORM=SHOPTB"
response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.content)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify())
# for i in soup.find_all('div',attrs={'class':'topTools btTopToolsLeft btTextLeft'}):
#     icon = i.find('span', attrs={'class':'btIconWidgetIcon'})
#     print(icon.string)
    
