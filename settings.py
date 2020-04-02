from os.path import isfile
from envparse import env
import logging

log = logging.getLogger('app')
log.setLevel(logging.DEBUG)

f = logging.Formatter('[L:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', datefmt = '%d-%m-%Y %H:%M:%S')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(f)
log.addHandler(ch)

if isfile('.env'):
    env.read_envfile('.env')

DEBUG = True

SITE_HOST = env.str('HOST') or '0.0.0.0'
SITE_PORT = env.int('PORT') or '8080'

