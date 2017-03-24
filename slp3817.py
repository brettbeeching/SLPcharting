#example of what regexs can do

import re

import os
    
def goalornot():

    goalornot = input('Do you need to add goals?(Y/N) ')
    
    while goalornot.lower() != 'y' and goalornot.lower() != 'n':
        goalornot = input('Do you need to add goals?(Y/N) ')
    if goalornot.lower() == 'y':

        slptemplist = listslp('slptemp1')

        slptemplistgoal = goalsetting(slptemplist)

        slptempcontent = listtostr(slptemplistgoal)

        return slptempcontent
    
    elif goalornot.lower() == 'n':

        slptempcontent = openslp('slptemp1')

        return slptempcontent
        
    
def clientfilespathfunc():
    '''Creates directory for output files.'''
    
    clientfilespath = 'C:\\python\\clientfiles'
    
    if not os.path.exists(clientfilespath):
        os.makedirs(clientfilespath)

    return clientfilespath

#os.chdir(newpath)
def openslp(template):
    '''Opens template and reads to an object'''
    
    slptemp = open(os.getcwd() + '\\' + template + '.txt')
    slptempcontent = slptemp.read()
    slptemp.close()
    return slptempcontent

def listslp(template):
    '''Use to turn the template into a list. Need to insert specific
       number of goals'''
    
    slptemplist = []
    slptemp = open(os.getcwd() + '\\' + template + '.txt')
    for line in slptemp.readlines():
        slptemplist.append(line)
    slptemp.close()
    return slptemplist

def listtostr(slptemplist):
    '''Use this after calling the goalsetting() and inserting the
       correct amount of goals'''
    
    slptempcontent = ''.join(slptemplist)
    return slptempcontent

def specifyclient(clientfilespath):
    '''Creates or just opens a current client file if already exists'''
    
    clientfile = input('Input client\'s file name ') + '.txt'
    if os.path.exists(clientfilespath + '\\' + clientfile):
        client  = open(clientfilespath + '\\' + clientfile, 'r')
    else:
        client  = open(clientfilespath + '\\' + clientfile, 'w')
        client.close()
        client  = open(clientfilespath + '\\' + clientfile, 'r')
    client.close()

    
    return (clientfilespath + '\\' + clientfile)

#Dictionary of terms.
slpdict = {'dir' : 'Direct',
           
           'idr' : 'Indirect',
           
           '92507' : 'Individual',
           
           '92508' : 'Group',
           
           'spe' : 'Speech and Sound Production',

           'lan': 'Language, Comprehension and Expression',

           'flu': 'Fluency',
             
           'min': 'required minimal (1x cue or prompt) support to demonstrate the therapy objective behavior.',

           'mod': 'required moderate (2x to 3x cues or prompts) support to demonstrate the therapy objective behavior.',

           'max': 'required maximum (4x+ cues or prompts) support to demonstrate the therapy objective behavior.',

           'hoh': 'required hand-over-hand support to demonstrate the therapy objective behavior.',

           'ind': 'independently demonstrated the therapy objective behavior after initial instruction.',

           'inc': 'As compared to previous measurements, the client required less support despite increased complexity of the task.',

           'dec': 'Progress remains commensurate with previous assessment.  More time is needed for generalization.'}

#Temporary reminder to call the function
print("Call function 'regexsub(template)' to add to chart.")

def goalsetting(slptemplist):

    goalsplaceholder = []
    '''List(from findall regex) -> str
       Enter number of goals to generate.
       '''
    numgoals = input('Enter number of goals to generate. ')
    
    y = 1
    if not numgoals.isdigit() or not int(numgoals) >0:
        return slptemplist
    else:
        
        for i in range(1, int(numgoals) +1):
            enteredgoal = str(i) + '.' + '__Goal ' + str(i) + '__' + '\n'
            slptemplist.insert(slptemplist.index('Goal(s) and Objective(s):\n') + y, enteredgoal)
            y = y + 1

        return slptemplist

def regexsub(slptempcontent, clientfile):
     '''(string)-> string with subs

       Take a string with '__ and __' placeholder and then subs the
       user input into those placeholder positions.'''
     placeholder = []
    
     myregex = re.compile(r'__[^__].*?__')

     goalsregex = re.compile(r'__Goal \d__')

     appendregex = re.compile(r'(_){40}.*?(_){40}', re.DOTALL)

     someregex = myregex.findall(slptempcontent)

     print(someregex)

#Example of extracting text out of '__' placeholder.

 
    #someregex[i] = someregex[i][2:-2]

     for i in range(len(someregex)):
         
         someregex[i] = someregex[i][2:-2]
         
         userinput = input(someregex[i] + ' ')
             
         #finds key and then returns value from slpdict if applicable         
         if userinput.lower() in slpdict.keys():
             
             placeholder.append(slpdict[userinput.lower()])
             
         else:
             
             placeholder.append(userinput)
                 
         #asks user for confirmation
         while input('Is this correct? ').lower() != 'y':
             
             placeholder[i] = input(someregex[i] + ' ')
             
         #subs each occurence in sequence    
         slptempcontent = myregex.sub(placeholder[i], slptempcontent, 1) 
             
     print(slptempcontent)

     aw = input('would you like to append this text to the file or overwrite the contents(a or w)? ')
     #choosing between 2 variables
     while aw.lower() != 'a' and aw.lower() != 'w':
          aw = input('would you like to append this text to the file or overwrite the contents(a or w)? ' )
     
     if aw.lower() == 'w':
          client = open(clientfile, 'w')
          client.write(slptempcontent)
          client.close

     else:
          client  = open(clientfile, 'a')
          stringappend = appendregex.search(slptempcontent)
          stringappend = stringappend.group()
          client.write('\n' + stringappend[40:-40])
          client.close()
#TODO

#1. add in read/write capabilities
     #give user option to open specific files
     #specify the path (i.e "Enter path where you would like to save files")
     
#2. Create dicts for SLP variables DONE

#3. Figure out way to give option of selection more than one var for only one input box

#4. Format text files
          
#5. Cloud save?

#6. Take away choice to append or write
