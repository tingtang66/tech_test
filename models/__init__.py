import yaml 
from os.path import isfile
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

config_path = 'config'
config_file = '%s/database.yml' % config_path 

if isfile(config_file):
    with open(config_file, 'r') as file:
        conn_info = yaml.load(file.read())
else:
    raise SystemExit(conn_info)
db_conf = conn_info[0]
engine = create_engine('%s://%s:%s@%s:%s/%s?charset=utf8' % (db_conf['engine'], db_conf['db_user'], db_conf['db_pass'], db_conf['host'], db_conf['port'], db_conf['db_name']))

Base = declarative_base() 
session = scoped_session(sessionmaker())
session.configure(bind=engine)

@contextmanager
def session_scope():
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
