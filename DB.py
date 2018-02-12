import Config
import pg

PDB = pg.DB(dbname=Config.get_database(), host=Config.get_host(), port=int(Config.get_port()),\
            user=Config.get_user(), passwd=Config.get_password())

def random_co_photography():
    pass
