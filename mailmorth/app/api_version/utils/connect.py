import threading

#----------------------------------------------------------------------------------
"""Create a thread to handle the logging in of a user into an email system
"""
#----------------------------------------------------------------------------------
def connectToMailSystem():
    """thread worker function"""
    print 'Worker\n'
    return

threads = []
t = threading.Thread(target=connectToMailSystem)
threads.append(t)
t.start()
