#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from os import environ
from bcrypt import checkpw

logFilePath = '/var/log/myvpn/auth.log'

Username = environ['username']
Password = environ['password']

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',level=logging.INFO)

try:

    with open( "user.data" ) as f:
        lines = f.read().splitlines()

    for line in lines:
        words = line.split( ":" )
        if words[0][0] == '#':
            continue
        if words[0] != '' and words[1] != '' and words[0][0] != ' ' and words[1][0] != ' ':
            if words[0] == Username:
                if checkpw( Password.encode(), words[1].encode() ):
                    logging.info( "User: " + words[0] + " - Sucessfully Authenticated" )
                    exit( 0 )
                else:
                    logging.warning("User: "+words[0]+" - Password Did not Match" )
                    exit( 1 )

    logging.warning( "User: " + Username + " - User not Found" )
    exit( 1 )

except Exception as e:
    logging.critical(str(e))
    exit(1)