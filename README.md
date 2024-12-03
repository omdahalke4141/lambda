Lambda Function
Create a Python-based Lambda function that:
  -Accepts two arguments via the API (e.g., num1 and num2).
  -Computes their sum after a 15-second delay using time.sleep.
  -Returns the sum as a JSON response.


Create an AWS API Gateway:
  -Define an endpoint to trigger the Lambda function.
  -Accept input arguments (num1, num2) via query parameters or JSON body.

SAM Template
Write a SAM (Serverless Application Model) template to define the infrastructure:
 -Lambda function: Define runtime, handler, and permissions.
 -API Gateway: Define an HTTP API or REST API to integrate with the Lambda function

Package and deploy:
  -sam build
  -sam deploy --guided

Test using the API Gateway URL:
  -https://<api-gateway-url>/add?num1=5&num2=10
