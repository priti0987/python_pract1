import configparser

config = configparser.RawConfigParser()
confPath = "..\\Configurations\\config.ini"
config.read(confPath)


class ReadConfig:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(confPath)
    @staticmethod
    def getApplicationURL():
        url = config.get('common_info', 'baseUrl')
        print("............................hjgjhygyj98798")
        return url

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password

    @staticmethod
    def getUsername():
        usernameEmail = config.get('common_info', 'email')
        return usernameEmail

ok = ReadConfig()
print(ok.getApplicationURL())