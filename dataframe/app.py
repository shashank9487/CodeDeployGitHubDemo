import boto3
import pandas as pd
from decimal import Decimal
from http import HTTPStatus


client = boto3.client('codepipeline')
        
def create_price_label(row):
    price = Decimal(row['price'])
    price = round(price, 2)
    return row['name'].title() + " $" + str(price)

def lambda_handler(event, context):
    try:
        print('event', event)
        url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
        chipo = pd.read_csv(url, sep = '\t')
        prices = [float(value[1 : -1]) for value in chipo.item_price]
        chipo.item_price = prices
        chipo_filtered = chipo.drop_duplicates(['item_name','quantity','choice_description'])
        chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]
        chipo_one_prod.fillna(0, inplace=True)
        print(chipo_one_prod)
        chipo.item_name.sort_values()
        chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]
        print(f'How many veggie salads? {len(chipo_salad)}')
        print(f'How many items? {len(chipo_salad)}')
        jobId = event['CodePipeline.job']['id']
        client.put_job_success_result(
            jobId=jobId
        )
    except Exception as e:
        client.put_job_failure_result(
            jobId=jobId,
             failureDetails={
                'type': 'JobFailed',
                'message': e
            }       
        )
    return "Completed"

