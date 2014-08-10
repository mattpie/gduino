"""
mail.py
Connect and interact with a gmail account
"""

from gmail import Gmail
import getpass


class Mail():
    def __init__(self):
        # user info
        self.username = None
        self.password = None
        
        # object using the gmail library
        self.g = Gmail()
    
    
    def login(self):
        # get user info    
        username = raw_input('Username: ').strip()
        password = getpass.getpass('Password: ').strip()
            
        #login
        try:
            self.g.login(username, password)
        except:
            print 'Unable to login'
  
  
    def logout(self):
        # logout
        self.g.logout()
                  
       
    def getNumUnread(self):
        # get number of unread email  
        try:
            return len(self.g.inbox().mail(unread=True))
        except Exception as err:
            print str(err)

