@description('The name of the App Service plan.')
param appServicePlanName string = 'm365-it-manager-plan'

@description('The name of the Web App.')
param webAppName string = 'm365-it-manager-webapp'

@description('The location for the resources.')
param location string = resourceGroup().location

resource appServicePlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: 'F1'
    capacity: 1
  }
}

resource webApp 'Microsoft.Web/sites@2022-03-01' = {
  name: webAppName
  location: location
  serverFarmId: appServicePlan.id
  properties: {
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: 'PYTHON|3.11'
    }
  }
}
