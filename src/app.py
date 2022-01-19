import json
import os


def lambda_handler(event, context):
    config = json.loads(os.environ["config"])
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world\n",
                "config": config,
            }
        ),
    }
