import accounts_omac
configSettings = accounts_omac.configFileTkinter()
data = accounts_omac.defaultConfigurations.defaultLoadingTkinter(configSettings)
if data == False:
    exit()


#this saves the account data, without having to reopen the app
data = accounts_omac.saveAccount(data, configSettings)
#you can continue using it, and save multiple times, and it will still work




data = accounts_omac.saveAccount(data, configSettings)