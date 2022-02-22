import accounts_omac
configSettings = accounts_omac.configFileConsole()
data = accounts_omac.defaultConfigurations.defaultLoadingConsole(configSettings)
data = accounts_omac.saveAccount(data, configSettings)
