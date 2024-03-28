import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html")
# for Products names
product = soup.find_all("a",class_ = "title")

product_name = []

for i in product:
    name = i.text
    product_name.append(name)
# print(product_name)

# For Prices
prices = soup.find_all("h4",class_ = "float-end price card-title pull-right")
prices_list = []

for i in prices:
    price = i.text
    prices_list.append(price)
# print(prices_list)

# for descriptions
descriptions = soup.find_all("p",class_ = "description card-text")
descriptions_list = []

for i in descriptions:
    description = i.text
    descriptions_list.append(description)
# print(descriptions_list)

# for reviews
reviews = soup.find_all("p",class_ = "float-end review-count")
reviews_list = []

for i in reviews:
    review = i.text
    reviews_list.append(review)
# print(reviews_list)

# Making DataFrame

df = pd.DataFrame({"Product Name": product_name,"Prices":prices_list,"Description":descriptions_list," Number of Reviews": reviews_list})
# print(df)

# df.to_csv("Product_detail.csv")
df.to_excel("Product_detail.csv")