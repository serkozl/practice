#-*-encoding: UTF-8 -*-
dict = {'один' : 'час', 'два' : 'часа', 'много' : 'часов' }
def humanizer(n, dict):
  if type(n) != int:
    print "Это не число!"
  else:
    if (n % 10)>=1 and (n % 10)<5:
        if (n % 100)>=11 and (n % 100)<=15:
            print str(n) + " " + dict['много']
        elif n % 10 == 1:
            print str(n) + " " + dict['один']
        else:
            print str(n) + " " + dict['два']
    else:
        print str(n) + " " + dict['много']

humanizer(25, dict)
