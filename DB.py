#!/usr/bin/env python
import Config
import pg
import logging
from random import shuffle
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PDB = pg.DB(dbname=Config.get_database(), host=Config.get_host(), port=int(Config.get_port()),\
            user=Config.get_user(), passwd=Config.get_password())

co_photos, lets_dos, pleasant_memories = [], [], []

def get_random_co_photography():
    global co_photos
    if not len(co_photos):
    	co_photos = PDB.query('select img_url from co_photos').dictresult()
    	shuffle(co_photos)
    return co_photos.pop(0)['img_url']

def get_random_lets_do():
    global lets_dos
    if not len(lets_dos):
    	lets_dos = PDB.query('select msg, img_url from lets_dos').dictresult()
    	shuffle(lets_dos)
    return lets_dos.pop(0)

def get_random_pleasant_memory():
    global pleasant_memories
    if not len(pleasant_memories):
    	pleasant_memories = PDB.query('select msg, img_url from pleasant_memories').dictresult()
    	shuffle(pleasant_memories)
    return pleasant_memories.pop(0)
