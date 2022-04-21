# accounts-system
# Version 2.7.3

let's start with stating the obvious, you need to import it.
Drag accounts_omac.py into a folder where you are going to use it. And then put 'import accounts_omac' on the first line.

To test the exxampleapps, you need to copy the accounts_omac.py into that folder too

## 2.7.3 update:
Tempdata, Not forcing people to update their account, and asks in relevent type, console or tkinter (if you tell it to)
If you the location in the configfile doesn not exist, it will create the folder. createAccount has a fix when there is something wrong with config



## How is the Account built:
Your account is a dict, with these keys:
'name' 'nickname' 'time' 'versionHistory' 'appData' 'collectables' 'achievements' 'loadTime' 'UserID' 'TempData'

### Name 
Name needs to always stay the same, as it's needed to store itself. tho you can change the nickname freely, then you create an 
account the nickname and name are the same

### Time 
time is used to store how long you have used the account, every seccond is noted down. You don't need to cde anything for it to 
work, just open your account as explained in the examples, and save it as explained in the examples, and it will automatically 
work. The time is an erray/list, first place contains amount of seconds. Second place is a string of the time formatted to 
Hour:Minute:Seconds format.

### VersionHistory 
Pre V2.6.0:
VersionHistory saves the history of versions of the account system the account gets logged into. This is purely for debugging 
problems. It only stores a version if the version you are using is a different one than the one u used last time.
V2.6.0+ 
This shows the highest version the account has been logged into. This is used for when there are new features added to the accounts itself and not the system. If 
you load a newer account into pre 2.6.0 nothing catastrophical will happen. it will just try to update the account again, which the system will ignore.

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

### UserID
UserID is a string that is binded to your account, yes you could change it, but it's a risk, because some apps could build in a check. The reason this exists is 
mostly for multiplayer apps. The cahnce of a UID to not be unique is 0 since it's based of datetime and your username.

### TempData
TempData is a list of items. This is 1 variable that won't be saved. It is used for when a user doesn't want to update his account to a newer version, that adds new things. 
for example the UserID. This way the account still adds the UserID to your account so you can still use the app, but when it saves the account, it deletes it from the 
account.

# The built in functions:
There are a lot of built in functions, here we have the normal functions:
1.configFileConsole 2.loadAccount 3.createAccount 4.saveAccount 5.checkForAccount 6.removeCharacters 7.askAccountNameConsole 
8.askAccountNameTkinter 9.questionConsole 10.questionTkinter 11.createAppData 12.configFileTkinter 13.on_closing
To use any of these functions, you have to put 'accounts_omac.' infront of it, like this:
accounts_omac.configFileConsole()

### 1.configFileConsole:
This creates the config file of the account system. with things like, where to store the accounts. And autologin. this needs to 
be in the start of any of the apps you make with this, since it cant function without it.
It takes no arguments and it will return the settings in a list. Save this list as you need it for multiple other functions.
since version 2.1 it asks for an argument, that argument is the path to where accounts are stored. if False is given or left empty, the program will ask for you.

### 2.loadAccount:
This basically loads an existing account. It takes 2 arguments: the account name. and the settings from the config file. it 
returns the data from the account. it reads json files. Since 2.6.0 it will check if there is an update for your account. Since 2.7.1 will take an extra argument, 'Console'
or 'Tkinter' which makes it so when it asks the user to update their account, it gets asked in the used way.

### 3.createAccount:
This basically creates an account. It overwrites the account if it already exists. it takes 2 arguments: the account name. and 
the settings from the config file. It returns the data from the account, so you don't have to load it afterwards. It reads json 
files. Since 2.7.3 will take an extra argument, 'Console' or 'Tkinter' which makes it so when there is an error with the config, it will ask in the used way if you want to delete.

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
Since 2.2.0 you can also give a list of characters for it to remove instead of the default.

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

### 12.configFileTkinter:
This creates the config file of the account system. with things like, where to store the accounts. And autologin. this needs to 
be in the start of any of the apps you make with this, since it cant function without it.
It takes no arguments and it will return the settings in a list. Save this list as you need it for multiple other functions.
since version 2.1 it asks for an argument, that argument is the path to where accounts are stored. if False is given or left empty, the program will ask for you in 
a Tkinter window.

### 13.on_closing:
This function asks you in tkinter to confirm that you want to close the app, and if you confirm it will exit. Be aware that it won't save your account data when 
you use it, it will liturally just close the program.

# Default functions:
I also made some Default functions. To use any of these functions, you have to put 'accounts_omac.defaultConfigurations.' infront of 
it, like this: accounts_omac.defaultConfigurations.defaultLoadingConsole()
These are the functions: 1.defaultLoadingConsole 2.defaultLoadingTkinter

### 1.defaultLoadingConsole:
This is a function you can call to use the account when you don't want to customize anything. It runs the other commands by himself. It will ask u 
for a username. It will create it if it doesn't exits, atleast if you want it to create an account. If you tell it not to create an account, it 
will return False. Otherwise it will return the account data.

### 2.defaultLoadingTkinter:
This is a function you can call to use the account (in tkinter) when you don't want to customize anything. It runs the other commands by himself. 
It will ask u for a username. It will create it if it doesn't exits, atleast if you want it to create an account. If you tell it not to create an 
account, it will return False. Otherwise it will return the account data.

# Easy functions:
I also made some Easy functions. To use any of these functions, you have to put 'accounts_omac.easy.' infront of 
it, like this: accounts_omac.easy.createPathIfNotThere()
These are the functions: 1.createPathIfNotThere 2.addRandomNoDuplicates 3.stringToAscii

### 1.createPathIfNotThere
This function takes 1 argument, the path. If it exists, it returns True. If it doesn't exist, it returns false and creates it.

### 2.addRandomNoDuplicates
This function takes 2-4 arguments: list, int, list, boolean boolean. The first list is a list with all possible items, for example: alphabet. The int is a number f 
items, for example: 5. The second list is the begin list, could be empty, could also already have 3 letters of the alphabet or something. The boolean is for if you 
want to ignore the already existing items or not. By default it will ignore it. What it does is it first checks the first list for duplicates, (same with the 
second list depending of the boolean is set to True or False) and then it adds the amount of the numbers items from the first list and adds it to the second list. 
If the last boolean is True, if there are no items left in the first list it will immediately return the list. if false, it will probably cause an error.

### 3.stringToAscii
This function takes 1 argument that needs to be a string, and this function returns the string turned into the ASCII values.

# system functions
There are system functions. these functons are needed to run the account system, but probably not needed for you, so i won't explain them here. But i will give you 
a list: 1.systemFunctions.userID() 2.systemFunctions.on_closing() 3.systemFunctions.updateRequest() 4. systemFunctions.CAFU() 5.systemFunctions.checkVersion()
They all heve descriptions of their own when you put them into your code.