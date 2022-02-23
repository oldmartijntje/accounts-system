import accounts_omac
configSettings = accounts_omac.configFileConsole()
account = accounts_omac.askAccountNameConsole(configSettings)
if accounts_omac.checkForAccount(account, configSettings):
    data = accounts_omac.loadAccount(account, configSettings)
else:
    if accounts_omac.createConfirmationConsole():
        data = accounts_omac.createAccount(account, configSettings)

#do something
data = accounts_omac.saveAccount(data, configSettings)

#this example is the same as the exampleAppEasyConsole.py
#without the changing data part
#but with this, you can take out parts to make them/ customize them yourself
