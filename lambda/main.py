import json
import os

def handler(event, context):
  version = os.environ.get('VERSION', '0.0')
  response_body = {
    "message": "Hello World! :hand:",
    "version": version
  }

  return {
    "statusCode": 200,
    "body": json.dumps(response_body)
  }