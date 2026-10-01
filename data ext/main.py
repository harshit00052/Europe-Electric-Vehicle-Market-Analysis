# https://ev-database.org/#group=vehicle-group&av-1=1&rs-pr=10000_100000&rs-er=0_1000&rs-ld=0_1000&rs-ac=2_23&rs-dcfc=0_400&rs-ub=10_200&rs-tw=0_3000&rs-ef=100_350&rs-sa=-1_5&rs-w=1000_3500&rs-c=0_2500&rs-y=2010_2030&s=1&p=0-10
import numpy as np
import pandas as pd
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
    try:
        name_list = brand_name.find('span', class_='hidden').text
    except (AttributeError, KeyError):
        name_list = np.nan
    name.append(name_list)

specs_cont = soup.find_all('div', class_='specs')
for item_specs in specs_cont:

    try:
        item_range = item_specs.find('span', class_='erange_real').text
    except (AttributeError, KeyError):
        item_range = np.nan
    crRange.append(item_range)

    try:
        effi = item_specs.find('span', class_='efficiency').text
    except (AttributeError, KeyError):
        effi = np.nan
    efficiency.append(effi)

    try:
        wt = item_specs.find('span', class_='weight_p').text
    except (AttributeError, KeyError):
        wt = np.nan
    weight.append(wt)

    try:
        acc = item_specs.find('span', class_='acceleration_p').text
    except (AttributeError, KeyError):
        acc = np.nan
    acceleration.append(acc)

    try:
        one_Stop_Range = item_specs.find('span', class_='long_distance_total').text
    except (AttributeError, KeyError):
        one_Stop_Range = np.nan
    one_15_min_Stop_Range.append(one_Stop_Range)

    try:
        btry = item_specs.find('span', class_='battery_p').text
    except (AttributeError, KeyError):
        btry = np.nan
    battery_Cap.append(btry)

    try:
        fst = item_specs.find('span', class_='fastcharge_speed_print').text
    except (AttributeError, KeyError):
        fst = np.nan
    fast_charge.append(fst)

    try:
        toweing = item_specs.find('span', class_='towweight_p').text
    except (AttributeError, KeyError):
        toweing = np.nan
    towing_cap.append(toweing)

    try:
        crgo = item_specs.find('span', class_='cargo').text
    except (AttributeError, KeyError):
        crgo = np.nan
    cargo_vol.append(crgo)

    try:
        ppr = item_specs.find('span', class_='priceperrange_p').text
    except (AttributeError, KeyError):
        ppr = np.nan
    price_per_range.append(ppr)


price_cont = soup.find_all('div', class_='pricing org')

for item_prc in price_cont:
    try:
        germany_tooltip_div = item_prc.find('span', class_='country_de',attrs={"data-tooltip": True})
        germany_item_tooltip = germany_tooltip_div['data-tooltip']
        germany_price = item_prc.find('span', class_='country_de').text
    except (AttributeError, KeyError):
        germany_item_tooltip = float(np.nan)
        germany_price = np.nan
    germany_a.append(germany_item_tooltip)
    germany_p.append(germany_price)

    try:
        netherlands_tooltip_div = item_prc.find('span', class_='country_nl',attrs={"data-tooltip": True})
        netherlands_item_tooltip = netherlands_tooltip_div['data-tooltip']
        netherlands_price = item_prc.find('span', class_='country_nl').text
    except (AttributeError, KeyError):
        netherlands_item_tooltip = float(np.nan)
        netherlands_price = np.nan
    netherlands_a.append(netherlands_item_tooltip)
    netherlands_p.append(netherlands_price)

    try:
        united_kingdom_tooltip_div = item_prc.find('span', class_='country_uk',attrs={"data-tooltip": True})
        united_kingdom_item_tooltip = united_kingdom_tooltip_div['data-tooltip']
        united_kingdom_price = item_prc.find('span', class_='country_uk').text
    except (AttributeError, KeyError):
        united_kingdom_item_tooltip = float(np.nan)
        united_kingdom_price = np.nan
    united_kingdom_a.append(united_kingdom_item_tooltip)
    united_kingdom_p.append(united_kingdom_price)



# name = [] crRange = [] efficiency = [] weight = [] acceleration = [] one_15_min_Stop_Range = []
# battery_Cap = [] fast_charge = [] towing_cap = [] cargo_vol = [] price_per_range = []
# germany_a = [] germany_p = [] netherlands_a = [] netherlands_p = [] united_kingdom_a = [] united_kingdom_p = []


data = {
    'brand_model' : name,
    'range':crRange,
    'efficiency':efficiency,
    'weight':weight,
    'acceleration':acceleration,
    'one_15_min_Stop_Range':one_15_min_Stop_Range,
    'battery_Capacity':battery_Cap,
    'fast_charge':fast_charge,
    'towing_capacity':towing_cap,
    'cargo_volume':cargo_vol,
    'price_per_range':price_per_range,
    'Germany info':germany_a,
    'Germany price':germany_p,
    'netherlands info':netherlands_a,
    'netherlands price':netherlands_p,
    'united_kingdom info':united_kingdom_a,
    'united_kingdom price':united_kingdom_p,
}


df = pd.DataFrame(data)
df.to_csv('electric_car_dataset.csv', index=False)