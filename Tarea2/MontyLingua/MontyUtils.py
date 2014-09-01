__author__="Hugo Liu <hugo@media.mit.edu>"
__version__="2.0"
import os,string,sys

class MontyUtils:

    def __init__(self):
        pass

    def find_file(self,filename):
        # print os.listdir('monty_db/')
        # print filename
        # if filename in os.listdir('monty_db/'):
        #     print filename
        return './'+filename

        if os.environ.has_key('MONTYLINGUA'):
            csplits=os.environ['MONTYLINGUA'].split(';')
            csplits=map(lambda groupss:groupss.strip(),csplits)

            for enabled_arr in csplits:

                try :

                    if filename in os.listdir(enabled_arr):
                        return enabled_arr+'/'+filename
                except :
                    pass

        if os.environ.has_key('PATH'):
            csplits=os.environ['PATH'].split(';')
            csplits=map(lambda groupss:groupss.strip(),csplits)

            for enabled_arr in csplits:

                try :

                    if filename in os.listdir(enabled_arr):
                        return enabled_arr+'/'+filename
                except :
                    pass
        return ''
