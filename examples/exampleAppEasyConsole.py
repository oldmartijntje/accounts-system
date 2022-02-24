import accounts_omac
configSettings = accounts_omac.configFileConsole()
data = accounts_omac.defaultConfigurations.defaultLoadingConsole(configSettings)
#do something
data = accounts_omac.saveAccount(data, configSettings)
#you can continue using it, and save multiple times, and it will still work


data = accounts_omac.saveAccount(data, configSettings)