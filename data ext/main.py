# https://ev-database.org/#group=vehicle-group&av-1=1&rs-pr=10000_100000&rs-er=0_1000&rs-ld=0_1000&rs-ac=2_23&rs-dcfc=0_400&rs-ub=10_200&rs-tw=0_3000&rs-ef=100_350&rs-sa=-1_5&rs-w=1000_3500&rs-c=0_2500&rs-y=2010_2030&s=1&p=0-10
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://ev-database.org/#group=vehicle-group&av-1=1&rs-pr=10000_100000&rs-er=0_1000&rs-ld=0_1000&rs-ac=2_23&rs-dcfc=0_400&rs-ub=10_200&rs-tw=0_3000&rs-ef=100_350&rs-sa=-1_5&rs-w=1000_3500&rs-c=0_2500&rs-y=2010_2030&s=1&p=0-10")

name = []
crRange = []
efficiency = []
weight = []
acceleration = []
one_15_min_Stop_Range = []
battery_Cap = []
fast_charge = []
towing_cap = []
cargo_vol = []
price_per_range = []
germany_a = []
germany_p = []
netherlands_a = []
netherlands_p = []
united_kingdom_a = []
united_kingdom_p = []


pg_src = driver.page_source
soup = BeautifulSoup(pg_src, 'html.parser')

name_cont = soup.find_all('a', class_='title')
for brand_name in name_cont:
    name_list = brand_name.find('span', class_='hidden')
    name.append(name_list.text)

# specs_cont = soup.find_all('div', class_='specs')
# for item_specs in specs_cont:
#
#     try:
#         item_range = item_specs.find('div', class_='erange_real').text
#     except
#         item_range = np.nan
#     crRange.append(item_range)


