# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:   
# https://aws.amazon.com/developers/getting-started/python/

import boto3
import base64
from botocore.exceptions import ClientError
import json
import logging
logger = logging.getLogger()


def get_secret():

    secret_name = "arn:aws:secretsmanager:us-east-2:939595455984:secret:naomi-airbnb-db-sm-NT2plR"
    region_name = "us-east-2"
    text_secret_data = ""
    binary_secret_data = ""

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        logger.debug("Response from client received")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            logger.debug("The requested secret %s was not found", secret_name)
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            logger.debug("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            logger.debug("The request had invalid params", e)
        elif e.response['Error']['Code'] == 'DecryptionFailure':
            logger.debug("he requested secret can't be decrypted using the provided KMS key:", e)
        elif e.response['Error']['Code'] == 'InternalServiceError':
            logger.debug("An error occurred on service side:", e)
    else:
        logger.debug("No exceptions")
        # Secrets Manager decrypts the secret value using the associated KMS CMK
        # Depending on whether the secret was a string or binary, only one of these fields will be populated
        if 'SecretString' in get_secret_value_response:
            text_secret_data = get_secret_value_response['SecretString']
            return json.loads(text_secret_data)
        else:
            binary_secret_data = get_secret_value_response['SecretBinary'] 
            return json.loads(binary_secret_data)
