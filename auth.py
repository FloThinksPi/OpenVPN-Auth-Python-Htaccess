# coding=utf-8
from logging import getLogger, FileHandler, Formatter, INFO
from os import environ

from bcrypt import checkpw

logFilePath = '/var/log/myvpn/OpenVPN-Auth.log'

Username = environ['username']
Password = environ['password']

logger = getLogger( 'OpenVPN-Auth' )
hdlr = FileHandler( logFilePath )
formatter = Formatter( '%(asctime)s %(levelname)s %(message)s' )
hdlr.setFormatter( formatter )
logger.addHandler( hdlr )
logger.setLevel( INFO )

try:

    with open( "user.data" ) as f:
        data = f.readlines()

    for line in data:
        words = line.split( ":" )
        if words[0][0] == '#':
            continue
        else:
            if words[0] == Username:
                if checkpw( Password.encode(), words[1].encode() ):
                    logger.info( "User: " + words[0] + " - Sucessfully Authenticated" )
                    exit( 0 )
                else:
                    logger.warning("User: "+words[0]+" - Password Did not Match" )
                    exit( 1 )

except Exception as e:
    logger.critical(str(e))