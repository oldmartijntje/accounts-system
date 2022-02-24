# accounts-system

let's start with stating the obvious, you need to import it.
drag accounts_omac.py into a folder where you are going to use it. and then put 'import accounts_omac' on the first line.

To test the exxampleapps, you need to copy the accounts_omac.py into that folder too

# The basics:
you have an account. and you store data on it. and view the same data in other apps. but how?
as the exampleAppData.py shows, use: accounts_omac.createAppData() to create your data foders.

# How is the Account built:

Your account is a dict, with these keys:
'name' 'nickname' 'time' 'versionHistory' 'appData' 'collectables' 'achievements' 'loadTime'

## Name 
name needs to always stay the same, as it's needed to store itself. tho you can change the nickname freely, hen you create an 
account the nickname and name are the same

## Time 
time is used to store how long you have used the account, every seccond is noted down. u don't need to cde anything for it to 
work, just open your account as explained in the examples, and save it as explained in the examples, and it will automatically 
work. the time is an erray/list, first place contains amount of seconds. second place is a string of the time formatted to 
Hour:Minute:Seconds format.

## VersionHistory 
VersionHistory saves the history of versions of the account system the account gets logged into. this is purely for debugging 
problems. it only stores a version if it isn't already the last one in the list.

## AppData 
AppData is a dict with appdata. with the accounts_omac.createAppData() it automatically adds your app to the dictionary.
it then looks like this: data['appdata'][appIDorName] = []
this is where you can put all the appdata you need.

## Collectables 
Collectables works the same as appdata. but i advice you to split the list: data['collectables'][appIDorName] = []
up into 1 list and 1 dict: [[],{}] and then store the collectables in the list, and put the info about it in the dict. this
makes it easy to load othe apps their collectables into your apps. but you don't have to, you can use it any way you want

## Achievements
achievements work the same as Collectables ^^

## LoadTime
loadTime is used to save how much time you have used the account. do not touch this. if you change it it can, and possably will, 
break the Time stored on your account

# The built in functions:
there are a lot of built in functions, here we have the normal functions:
1.configFileConsole 2.loadAccount 3.createAccount 4.saveAccount 5.checkForAccount 6.removeCharacters 7.askAccountNameConsole 
8.askAccountNameTkinter 9.createConfirmationConsole 10.createConfirmationTkinter 11.createAppData

## 1.configFileConsole:
this creates the config file of the account system. with things like, where to store the accounts. and autologin. this needs to 
be in the start of any of the apps you make with this, since it cant function without it.
it takes no arguments and it will return the settings in a list. save this list as you need it for multiple other functions.