# used to log messages

import logging
#u can write any message inside logging block
'''
#we can implement in below order only
logging.critical('Critical message')
logging.error("my error")
logging.warning("my warning")
logging.info("my info")
logging.debug("my debug")
'''
'''
logging.basicConfig(filename='myFile.log',level=logging.ERROR)
#it will print till Eroor level and its above levels
logging.critical('Critical message')
logging.error("my error")
logging.warning("my warning")
logging.info("my info")
logging.debug("my debug")
'''


logging.basicConfig(filename='myFile.log',level=logging.DEBUG)
#it will print till DEBUG level and its above levels// all levels log will print
logging.critical('Critical message')
logging.error("my error")
logging.warning("my warning")
logging.info("my info")
logging.debug("my debug")

