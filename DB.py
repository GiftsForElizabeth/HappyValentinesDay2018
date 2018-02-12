#!/usr/bin/env python
import Config
import pg
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PDB = pg.DB(dbname=Config.get_database(), host=Config.get_host(), port=int(Config.get_port()),\
            user=Config.get_user(), passwd=Config.get_password())

def get_random_co_photography():
    
    return PDB.query('select img_url from co_photos offset random() * (select count(*) from co_photos) limit 1').dictresult()[0]['img_url']
