import accounts_omac
configSettings = accounts_omac.configFileConsole()
data = accounts_omac.defaultConfigurations.defaultLoadingConsole(configSettings)


appIDorName = 'yourExampleAppNameID1234'

#there is a function to create your data folders
#it returns the data back to you with empty lists for the 'appData' 'collectables' 'achievements' dicts
data = accounts_omac.createAppData(data, appIDorName)




#change data:
#data has these items: 'name' 'nickname' 'time' 'versionHistory' 'appData' 'collectables' 'achievements' 'loadTime'}
#whatever you do, don't touch the loadtime, it's used to count usetime of the account, and can easely break if you change it,
#just don't touch it

data['appdata'][appIDorName] = ['this is some data', 'this is more data']

#this is how you change data, in the collectables, appdata, and achievements dicts, you need to save it at your game id/name,
#keep in mind that if you choose obvious names, more people might have the name, so that's a problem, it's better to just take 
#a random string of characters 

