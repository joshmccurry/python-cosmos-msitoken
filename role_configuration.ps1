#Replace Variable Names
$resourceGroup = "<Resource Group Name>";
$cosmosName = "<Cosmos Name>";  
$functionName = "<Function Name>";
$subscription_ID = "<Subscription ID>";  


#Setup Custom Role
az account set --subscription $subscription_ID;
$cosmosEndpoint = az cosmosdb show --resource-group $resourceGroup --name $cosmosName --query documentEndpoint;
$scope = az cosmosdb show --resource-group $resourceGroup --name $cosmosName --query id --output tsv;
$principal = az webapp identity show --resource-group $resourceGroup --name $functionName --query principalId --output tsv;
$json = "{'RoleName': 'Read Azure Cosmos DB Metadata','Type': 'CustomRole','AssignableScopes': ['/'],'Permissions': [{'DataActions': ['Microsoft.DocumentDB/databaseAccounts/readMetadata']}]}";
az cosmosdb sql role definition create --resource-group $resourceGroup --account-name $cosmosName --body $json;
az cosmosdb sql role assignment create --resource-group $resourceGroup --account-name $cosmosName --role-definition-name "Read Azure Cosmos DB Metadata" --principal-id $principal --scope $scope;