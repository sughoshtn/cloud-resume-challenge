import boto3 
from botocore.exceptions import ClientError
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb_table = boto3.resource('dynamodb').Table('visitor_counter_tbl')

def lambda_handler(event, context):
    try:
        response = dynamodb_table.update_item(
            Key={'sitevisit': 'https://resume.sughoshnagarajan.com'},
            ExpressionAttributeValues={':val': decimal.Decimal(1)},
            UpdateExpression="set visitor_count = visitor_count + :val",
            ReturnValues="UPDATED_NEW"
    )
    except ClientError as e:
        print(e.response['Error']['Message']) 
    
    item = dynamodb_table.get_item(Key={'sitevisit': 'https://resume.sughoshnagarajan.com'})
    count_views = item['Item']['visitor_count']
        
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "headers": {
            "Access-Control-Allow-Origin": "https://resume.sughoshnagarajan.com"
        },
        "body": json.dumps(count_views, indent=4, cls=DecimalEncoder)
    }