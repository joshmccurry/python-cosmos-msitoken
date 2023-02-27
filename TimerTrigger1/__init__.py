import datetime
import logging
import os
import asyncio

import azure.functions as func
from azure.identity import ManagedIdentityCredential
from azure.cosmos import CosmosClient

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')
        

    identity = os.environ["identity"]
    cosmos = os.environ["cosmos_url"]
    mi_credential = ManagedIdentityCredential(client_id=identity)
    CosmosClient(cosmos, mi_credential,
                        user_agent="AzureFunction",
                        user_agent_overwrite=True,
                        connection_verify=True, 
                        consistency_level="Session")
    logging.info('Log Change')
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    
