# accounts-system

let's start with stating the obvious, you need to import it.
Drag accounts_omac.py into a folder where you are going to use it. And then put 'import accounts_omac' on the first line.

To test the exxampleapps, you need to copy the accounts_omac.py into that folder too

## How is the Account built:
Your account is a dict, with these keys:
'name' 'nickname' 'time' 'versionHistory' 'appData' 'collectables' 'achievements' 'loadTime'

### Name 
Name needs to always stay the same, as it's needed to store itself. tho you can change the nickname freely, then you create an 
account the nickname and name are the same

### Time 
time is used to store how long you have used the account, every seccond is noted down. You don't need to cde anything for it to 
work, just open your account as explained in the examples, and save it as explained in the examples, and it will automatically 
work. The time is an erray/list, first place contains amount of seconds. Second place is a string of the time formatted to 
Hour:Minute:Seconds format.

### VersionHistory 
VersionHistory saves the history of versions of the account system the account gets logged into. This is purely for debugging 
problems. It only stores a version if the version you are using is a different one than the one u used last time.

### AppData 
AppData is a dict with appdata. with the accounts_omac.createAppData() it automatically adds your app to the dictionary.
it then looks like this: data['appdata'][appIDorName] = []
this is where you can put all the appdata you need.

### Collectables 
Collectables works the same as appdata. But i advice you to split the list: data['collectables'][appIDorName] = []
up into 1 list and 1 dict: [[],{}] and then store the collectables in the list, and put the info about it in the dict. This
makes it easy to load othe apps their collectables into your apps. But you don't have to, you can use it any way you want

### Achievements
Achievements work the same as Collectables ^^

### LoadTime
LoadTime is used to save how much time you have used the account. Do not touch this. if you change it it can, and possably will, 
break the Time stored on your account

# The built in functions:
There are a lot of built in functions, here we have the normal functions:
1.configFileConsole 2.loadAccount 3.createAccount 4.saveAccount 5.checkForAccount 6.removeCharacters 7.askAccountNameConsole 
8.askAccountNameTkinter 9.questionConsole 10.questionTkinter 11.createAppData
To use any of these functions, you have to put 'accounts_omac.' infront of it, like this:
accounts_omac.configFileConsole()

### 1.configFileConsole:
This creates the config file of the account system. with things like, where to store the accounts. And autologin. this needs to 
be in the start of any of the apps you make with this, since it cant function without it.
It takes no arguments and it will return the settings in a list. Save this list as you need it for multiple other functions.

### 2.loadAccount:
This basically loads an existing account. It takes 2 arguments: the account name. and the settings from the config file. it 
returns the data from the account. it reads json files.

### 3.createAccount:
This basically creates an account. It overwrites the account if it already exists. it takes 2 arguments: the account name. and 
the settings from the config file. It returns the data from the account, so you don't have to load it afterwards. It reads json 
files.

### 4.saveAccount:
This function saves your account to a file. It also counts the time you have opened it and updates it. It also changes some data 
because just storing it yourself isn't gonna work, cause the 'loadTime' data prevent's it from being saved, so it changes that 
when saving it, and then fixes it again so you can keep on using the program. It takes 2 arguments: the data, and the config 
settings. It returns the data

### 5.checkForAccount:
This is a function that checks if the account exists. This is used so you don't try to load an account when it doesn't exist, and 
don't try to create an account when it already exists. It takes 2 arguments: the data, and the config settings. It returns a True 
or False Boolean.

### 6.removeCharacters:
This is a support function I use in some functions to remove illegal characters from account names so that you won't try to 
create a file that for example has a / in the name, cause that obviously won't work. It removes everything in the 
'string.punctuation' (from the string import) and all spaces. And returns the name. It takes 1 argument: The name.

### 7.askAccountNameConsole:
This is used to tell the app what account to login to. It will just ask for an account name. It will automatically use the 
removeCharacters() function. it takes 2 arguments: the config settings, and if you want to, custom text. It will return the 
username.

### 8.askAccountNameTkinter:
This is the same as askAccountNameConsole() except for the fact that it uses tkinter instead of the console to ask the name.
It takes 4 arguments: the config settings, The text on the button, The text on the label, the exampleName. If you only provide 
the settings, it will still work since the last 3 aren't neccasery. It returns the username.

### 9.questionConsole:
This function asks the user a question. Returns True or False, depending on of they answered with Y or N. Takes 1 argument:
The question. Default question is account creation question.

### 10.questionTkinter:
This function asks the user a question in a tkinter window. Returns True or False, depending on of they answered with Y or N. 
Takes 2 arguments: The question and the popup title. Default question is account creation question.

### 11.createAppData:
This checks if the app already has it's own key in the 3 dicts(appdata, achievements, collectables). And when it doesn't have 
these keys, it creates them. So you can add data to your apps.

# Easy functions:
I also made some easy functions. To use any of these functions, you have to put 'accounts_omac.defaultConfigurations.' infront of 
it, like this: accounts_omac.defaultConfigurations.defaultLoadingConsole()
These are the functions: 1.defaultLoadingConsole 2.defaultLoadingTkinter

### 1.defaultLoadingConsole:
This is a function you can call to use the account when you don't want to customize anything. It runs the other commands by himself. It will ask u 
for a username. It will create it if it doesn't exits, atleast if you want it to create an account. If you tell it not to create an account, it 
will return False. Otherwise it will return the account data.

### 2.defaultLoadingTkinter:
This is a function you can call to use the account (in tkinter) when you don't want to customize anything. It runs the other commands by himself. It will ask u for a username. It will create it if it doesn't exits, atleast if you want it to create an account. If you tell it not to create an account, it will return False. Otherwise it will return the account data.