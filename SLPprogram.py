from slp3817 import *
#Aggregates the functions and runs program

clientfilespath = clientfilespathfunc()

slptempcontent = goalornot()

clientfile = specifyclient(clientfilespath)

regexsub(slptempcontent, clientfile)





