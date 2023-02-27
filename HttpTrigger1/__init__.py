import datetime
import logging
import os
import asyncio

import azure.functions as func
from azure.identity import ManagedIdentityCredential
from azure.cosmos import CosmosClient


async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    utc_timestamp = datetime.datetime.utcnow()
    identity = os.environ["identity"]
    cosmos = os.environ["cosmos_url"]
    logging.info('Getting Token for Client id: %s', identity)
    mi_credential = ManagedIdentityCredential(client_id=identity)
    CosmosClient(cosmos, mi_credential,
                        user_agent="AzureFunction",
                        user_agent_overwrite=True,
                        connection_verify=True,
                        consistency_level="Session")
    logging.info('Python trigger function ran at %s', utc_timestamp)

    return func.HttpResponse(
            "This HTTP triggered function executed successfully.",
            status_code=200
    )
