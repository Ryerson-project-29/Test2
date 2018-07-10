
import os

def thread_blocking(host):
    os.system('ping '+ host)
    
def thread_no_blocking(host):
    output = os.popen('ping '+ host)
    print (output.read())
    
if __name__ == '__main__':
    
    host = '10.10.10.3'
    thread_blocking(host)
    

