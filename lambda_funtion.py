import json
import requests 
import pandas

def lambda_function(event, context):
    # TODO implement
    print('event' , event)
    
    response = requests.get('https://www.google.com')
    status_code = response.status_code
    headers = dict(response.headers)
    content = response.text  # or response.json() if the content is JSON
    
    # Format response as a JSON-serializable dictionary
    result = {
        'statusCode': status_code,
        'headers': headers,
        'body': content
    }

    data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

    df = pandas.DataFrame(data)
    print(df)
    
    return result