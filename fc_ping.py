
import os

def thread_blocking(host):
    result = os.system('ping -c 2 -w 2 %s'%(host))
    if result>0:
    	return False
    else:
    	return True
def thread_no_blocking(host):
    output = os.popen('ping -c 2 -w 2 %s'%(host))
    print (output.read())
    
if __name__ == '__main__':
    host = '10.10.10.3'
    thread_blocking(host)
    print (thread_blocking(host))
    
    

