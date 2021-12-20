#!/usr/bin/env python
###########################################
## name:            Connsumer APIs       ##
## author:          ejhoapa              ##
###########################################

from urllib2 import Request, urlopen, URLError
import argparse, datetime

parser = argparse.ArgumentParser(description='This program test the APIs given as parameter and return the response code.', usage='Execute using the following structure: ./main.py -f apis.lst')
parser.add_argument('-file', '-f', help='Use the following filename: apis.lst')
args = parser.parse_args()
apis = args.file

def readInputFile(file):
    """ This method read an input file given in the parameter and return a list of the file content
    @param: Filaname of the input file
    @return: return a list of the file content
    """
    with open(file, 'r') as f:
        line = f.readlines()
        lst_params = [x.rstrip() for x in line]
    return lst_params

def reqApi():
    """Fetch the url and get the response code, in case of error it generates an exception"""
    print("\tRESULT CODE TEST EXECUTION")
    print("Date: {}".format(datetime.datetime.now()))
    for url in [x for x in readInputFile(apis)]:
        req = Request(url)
        try:    
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print("Faled to reach the server.")
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('Server couldn\'t fulfill the request.')
                print('Error Code: ', e.code)
        else:
            print("URL: {} Response CODE: {} ".format(response.geturl(), response.getcode()))

if __name__ == '__main__':
    reqApi()