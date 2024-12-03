import json
import time

def lambda_handler(event, context):
    # Extract numbers from the API input
    num1 = int(event.get('queryStringParameters', {}).get('num1', 0))
    num2 = int(event.get('queryStringParameters', {}).get('num2', 0))

    # Delay to simulate processing time
    time.sleep(15)

    # Return the sum
    result = {"sum": num1 + num2}
    return {
        "statusCode": 200,
        "body": json.dumps(result),
        "headers": {"Content-Type": "application/json"}
    }
