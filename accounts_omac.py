version = '1.0.0'
#code made by OldMartijntje

def configFileConsole():
    '''creates or reads config file (consoleApp)'''
    import configparser
    import string
    import os
    if os.path.isfile("systemConfig.ini"):#read config if it exists
        config = configparser.ConfigParser()
        config.read('systemConfig.ini')
    else:#create config
        with open('systemConfig.ini', 'w') as configfile:
            config = configparser.ConfigParser(allow_no_value=True)
            config['DEFAULT'] = {'#don\'t change the file-extention if you are not sure of what it is' : None,
                'fileExtention' : '_omac'}
            folder = input('do you have a specific folder where you want to store account data?\nimport the path, or not\n>')
            if os.path.isdir(folder):#check if the inputted folder exists
                if folder[len(folder)-1] != '/' and folder[len(folder)-1] != '\\':
                    folder += '\\'
                config['User'] = {'SaveFileFolder' : folder,'AutoLogin' : 'False', 'AccountName' : 'testaccount'}
            else:
                config['User'] = {'SaveFileFolder' : 'accounts/','AutoLogin' : 'False', 'AccountName' : 'testaccount'}
                try:
                    os.mkdir('accounts/')
                except:
                    pass
            config.write(configfile)
            print('we created systemConfig.ini, this contains configurations for the account system, change the [User] section at any time')
    
    fileExtention = config['DEFAULT']['fileExtention']
    path = config['User']['SaveFileFolder']
    autoLogin = config['User']['AutoLogin']
    autoLoginName = config['User']['AccountName']
    autoLoginName = autoLoginName.replace(" ", "")
    for character in string.punctuation:
        autoLoginName = autoLoginName.replace(character, '')
    if autoLoginName == '':
        autoLogin = 'False'
    return path, autoLogin, autoLoginName, fileExtention

def loadAccount(accountName = 'testaccount', configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
    '''load existing acount'''
    import json
    import datetime
    path, autoLogin, autoLoginName, fileExtention = configSettings
    #just loading the json
    with open(f'{path}{accountName.lower()}{fileExtention}.json') as json_file:
        dataString = json.load(json_file)
        data = json.loads(dataString)
        data['loadTime'] = datetime.datetime.now()
    if data['versionHistory'][len(data['versionHistory']) -1] != version:
        data['versionHistory'].append(version)
    return data

def createAccount(accountName = 'testaccount', configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
    '''create the account (will wipe existing data!!!)'''
    import json
    import datetime
    path, autoLogin, autoLoginName, fileExtention = configSettings
    today = datetime.datetime.today()
    data = {'name': accountName, 'nickname': accountName, 'time': [0,'0'], 'versionHistory':[version], 'appData':{}, 'collectables':{}, 'achievements':{}, 'loadTime':0}
    

    #creating the json
    json_string = json.dumps(data)
    with open(f'{path}{accountName.lower()}{fileExtention}.json', 'w') as outfile:
        json.dump(json_string, outfile)
        data['loadTime'] = datetime.datetime.now()
    return data

def saveAccount(data, configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
    '''saves the account back to the json, will return data for when you want to keep using the data'''
    import json
    import datetime
    path, autoLogin, autoLoginName, fileExtention = configSettings
    now = datetime.datetime.now()
    timePlayed = ((now - data['loadTime']).total_seconds()) // 1
    data['loadTime'] = 0
    data['time'][0] += timePlayed
    data['time'][1] = str(datetime.timedelta(seconds=data['time'][0]))
    json_string = json.dumps(data)
    with open(f'{path}{data["name"].lower()}{fileExtention}.json', 'w') as outfile:
        json.dump(json_string, outfile)
        data['loadTime'] = datetime.datetime.now()
    return data

def checkForAccount(accountName = 'testaccount', configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
    '''check if the account exists'''
    import os
    path, autoLogin, autoLoginName, fileExtention = configSettings
    if os.path.exists(f'{path}{accountName.lower()}{fileExtention}.json'):#check if account exists
        return True
    else:
        return False

def checkName(name):
    import string
    name = name.replace(" ", "")
    for character in string.punctuation:
        name = name.replace(character, '')
    return name

def askAccountNameConsole(configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
    '''simply asks input for an account name (console app), returns account name'''
    path, autoLogin, autoLoginName, fileExtention = configSettings
    #for the autologin
    if autoLogin.lower() == 'true':
        username = autoLoginName
    else:
        username = ''
        while username == '':  
            username = input('please give username\n>')
            username = checkName(username)
    
    return username

def askAccountNameTkinter(configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
    '''input the account name (tkinter), returns account name'''
    import tkinter
    def click():
        username = checkName(nameVar.get())
        if username != '':
            window.destroy()
    path, autoLogin, autoLoginName, fileExtention = configSettings
    if autoLogin.lower() == 'true':
        username = autoLoginName
    else:
        window = tkinter.Tk()
        nameVar=tkinter.StringVar()
        nameVar.set('exampleName')
        tkinter.Label(text = 'input your name here').pack()
        nameEntry = tkinter.Entry(window,textvariable = nameVar, font=('calibre',10,'normal'))
        nameEntry.pack()
        button = tkinter.Button(window, text = 'click me when you chose your name', command = lambda: click()).pack()
        window.mainloop()
        username = checkName(nameVar.get())
    return username

def createConfirmationConsole():
    '''simply asks user (console app) if they want to create the account, returns True or False'''
    answer = 0
    print('account doesn\'t exist, should i create it? (Y/N)')
    while answer != 'y' and answer != 'n':
        answer = input().lower()
    if answer == 'y':
        return True
    else:
        return False

def createConfirmationTkinter():
    '''simply asks user (Tkinter) if they want to create the account, returns True or False'''
    import tkinter
    import tkinter.messagebox
    if tkinter.messagebox.askokcancel("POPUP", "Doesn\'t exists, should we create this account?"):
        return True
    else:
        return False

class defaultConfigurations:
    def defaultLoadingConsole(configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
        '''The default loading system without your configuration, in the console app'''
        account = askAccountNameConsole(configSettings)
        if checkForAccount(account, configSettings):
            return loadAccount(account, configSettings)
        else:
            if createConfirmationConsole():
                return createAccount(account, configSettings)

    def defaultLoadingTkinter(configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
        '''The default loading system without your configuration, using tkinter'''
        account = askAccountNameTkinter(configSettings)
        if checkForAccount(account, configSettings):
            return loadAccount(account, configSettings)
        else:
            if createConfirmationTkinter():
                return createAccount(account, configSettings)


