'''
Created on 16 Mar 2017

@author: sysop
'''
from rtkit.resource import RTResource
from rtkit.authenticators import BasicAuthenticator
from rtkit.errors import RTResourceError

class RT_Ticket(object):
    '''
    classdocs
    '''


    def __init__(self, userName, password, rt_api_url):
        '''
        Constructor
        '''
        from rtkit import set_logging
        import logging
        set_logging('debug')
        logger = logging.getLogger('rtkit')
        #resource = RTResource('http://<HOST>/REST/1.0/', '<USER>', '<PWD>', BasicAuthenticator)
        resource = RTResource(rt_api_url, userName, password, BasicAuthenticator)
        
    def 
