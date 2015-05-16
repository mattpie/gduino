'''
check gmail and light an LED
if there are unread emails
'''

from mail import Mail
from sConnection import SConnection
import sys



def main():
    MAIL    = 'M'
    NO_MAIL = 'N'
    
    # create Mail object, login get 
    # number of unread emails, then logout
    g = Mail() 
    g.login()
    numUnread = g.getNumUnread()
    g.logout()
    
    # create SConnection object and connect
    # to serial port
    s = SConnection()
    s.connectToSerial('COM3')
    
    # write message to serial depending on if
    # there are unread emails or not
    if numUnread > 0:
        s.writeToSerial(MAIL)
    else:
        s.writeToSerial(NO_MAIL)
    
    # close serial connection
    s.closeSerial() 
    
if __name__ == '__main__': main()


