import pandas as pd

def lambda_handler(event, context):
    data = {'col1': [1, 2], 'col2': [3,4], 'col3': None}
    df = pd.DataFrame(data=data)
    df = df.fillna(0)
    print(df)
    print("Done pd test")