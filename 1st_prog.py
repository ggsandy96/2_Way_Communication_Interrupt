import signal
import sys
import time
import os
b = "$59"
def signal_handler(signal, frame):
        global b
        file = open('foo.txt', 'r')
        fi = file.read()
        file.close()
        if( fi!=b):
                b = fi
                print fi
                cmd = "echo "+fi+" > /dev/ttymxc0"
                os.system(cmd)
        else:
                b = fi
signal.signal(signal.SIGUSR1, signal_handler)
while True:
        a = raw_input()
        fi_op =open('foo.txt', 'w')
        fi_op.write(a)
        fi_op.close()
        os.system("ps -ef | grep '2nd_prog.py' | awk '{print $2}' | xargs sudo kill -USR2")


