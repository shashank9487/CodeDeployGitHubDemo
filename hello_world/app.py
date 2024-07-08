import pandas as pd
from decimal import Decimal


def create_price_label(row):
    price = Decimal(row['price'])
    price = round(price, 2)
    return row['name'].title() + " $" + str(price)

def lambda_handler(event, context):
    url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    chipo = pd.read_csv(url, sep = '\t')
    prices = [float(value[1 : -1]) for value in chipo.item_price]
    chipo.item_price = prices
    chipo_filtered = chipo.drop_duplicates(['item_name','quantity','choice_description'])
    chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]
    chipo_one_prod.fillna(0, inplace=True)
    print(chipo_one_prod)
    chipo.item_name.sort_values()
    print("Finished tab")
