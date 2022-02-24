import accounts_omac

#you need the config file of the account system, 1. so it matches all your apps in same directory. 2.it needs the settings
configSettings = accounts_omac.configFileConsole()


account = accounts_omac.askAccountNameConsole(configSettings)
if accounts_omac.checkForAccount(account, configSettings):
    data = accounts_omac.loadAccount(account, configSettings)
else:
    if accounts_omac.createConfirmationConsole():
        data = accounts_omac.createAccount(account, configSettings)


#some functions that might be usefull
print(accounts_omac.removeCharacters('cheese@my.house.com/today is cool'))





#this saves the account data, without having to reopen the app
data = accounts_omac.saveAccount(data, configSettings)

#this example is the same as the exampleAppEasyConsole.py
#but with this, you can take out parts to make them/ customize them yourself
