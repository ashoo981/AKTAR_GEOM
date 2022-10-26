import configparser




config = configparser.RawConfigParser()
config.read(".\\Configrations\\config.ini")

class ReadConfig:

    @staticmethod
    def get_file_to_transfer(param):
        file = config.get('common info',param)
        return file

    @staticmethod
    def get_data_path_address():
        path = config.get('common info','dataPathAddress')   

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_database_host():
        db_host = config.get('common info', 'db_host')
        return db_host

    @staticmethod
    def get_database_port():
        db_port = config.get('common info', 'db_port')
        return db_port

    @staticmethod
    def get_database_name():
        db_name = config.get('common info', 'db_name')
        return db_name

    @staticmethod
    def get_database_username():
        db_user = config.get('common info', 'db_user')
        return db_user

    @staticmethod
    def get_database_password():
        db_password = config.get('common info', 'db_password')
        return db_password  

    


  

