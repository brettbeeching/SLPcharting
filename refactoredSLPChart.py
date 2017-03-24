from tkinter import *

from tkinter import ttk,  filedialog, messagebox

import re, os


class SlpChart(object):



    
    
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

    def __init__(self):
        
        #self.window = Tk()
        self.filewindow = Tk()
        self.filewindow.title('Template Phase')
        self.filename = StringVar()
        self.someregexvar = StringVar()
        self.templatestatus = StringVar()
        self.templatestatus.set('Awaiting template')
        self.slptempcontent = ''
        self.slptemplist = []
        
            
        #self.goalwindow = Tk()
        #self.someregex = None  # All attributes should be initialize in init
        #self.createsomeregex()
        #self.create_goalwidget()
        self.create_widgets()


    def startogoal(self):
        self.filewindow.destroy()
        self.window = Tk()
        self.window.title('Goal Phase')
        self.create_goalwidget()
        return
        
    def openDirectory(self):
        self.browse = filedialog.askopenfile(defaultextension = '.txt')
        self.slptempfile = self.browse
        self.slptempcontent = self.slptempfile.read()
        self.templatestatus.set('Template Imported!')
        self.browse.close()
        return
    
    #def createsomeregex(self):
        
        
        
    def create_goalwidget(self):
              
        add_goal_label = ttk.Label(self.window, text = 'Add a goal?', relief = 'flat').grid(row = 0,column = 1, columnspan = 3, ipadx = 5, ipady = 5)
        add_goal_button = ttk.Button(self.window, text = 'YES', command = self.goalyes).grid(row = 4, column = 0)
        no_goal_button = ttk.Button(self.window, text = 'NO', command = self.goalno).grid(row = 4, column = 5)
        
    def create_widgets(self):
        
        #file dialog buttons
        ttk.Label(self.filewindow, text = 'Browse for template').grid()
        openfile = ttk.Button(self.filewindow, text = 'Browse', command = self.openDirectory).grid()
        ttk.Label(self.filewindow, textvariable = self.templatestatus).grid()
        ttk.Button(self.filewindow, text = 'Continue to next step?', command = self.startogoal).grid(padx = 5, pady = 5)

##        self.someregex = ttk.Entry(self.window, textvariable=self.someregexvar)
##        self.someregex.grid(row=0, column=0)
##
##        increment_button = ttk.Button(self.window, text="Proceed")
##        increment_button.grid(row=1, column=0)
        #increment_button['command'] = self.goalornot
    
##        
##            
##        quit_button = ttk.Button(self.window, text="Quit")
##        quit_button.grid(row=6, column=0)
##        quit_button['command'] = self.window.destroy
##
##        self.someregex.focus()
        

    def clientfilespathfunc(self):
        '''Creates directory for output files.'''
    
        self.clientfilespath = 'C:\\python\\clientfiles'
        
        if not os.path.exists(self.clientfilespath):
            os.makedirs(self.clientfilespath)

        return self.clientfilespath
    

    def openslp(self):
        '''Opens template and reads to an object'''

        #adding filedialog
        #self.template = template
            
        self.slptemp = open(self.filename.get())
        self.slptempcontent = self.slptemp.read()
        self.slptemp.close()
        return self.slptempcontent
    

    def listslp(self):
        '''Use to turn the template into a list. Need to insert specific
           number of goals'''
        slptemplocal = self.slptempcontent

        self.slptemplist = self.slptempcontent.split('\n')

        
        return
       
      
    

    def listtostr(self):
        '''Use this after calling the goalsetting() and inserting the
           correct amount of goals'''

        self.slptemplist
        #self.slptemplist.insert(5, 'Test to see if this is modifying SLPTEMPCONTENT')
        self.slptempcontent = ''
        # deprecated? self.slptempcontent = ''.join(self.slptemplist)
        for i in self.slptemplist:
            self.slptempcontent += i + '\n' #rejoins list with proper spacing.
            
        return
    

    def specifyclient(self):
        '''Creates or just opens a current client file if already exists'''

        clientfilespath = self.clientfilespathfunc()
        
        self.clientfile = input('Input client\'s file name ') + '.txt'
        if os.path.exists(self.clientfilespath + '\\' + self.clientfile):
            self.client  = open(clientfilespath + '\\' + self.clientfile, 'r')
        else:
            self.client  = open(clientfilespath + '\\' + clientfile, 'w')
            self.client.close()
            self.client  = open(clientfilespath + '\\' + clientfile, 'r')
            
        self.client.close()

        
        return (self.clientfilespath + '\\' + self.clientfile)


    def goalyes(self):
        '''Asks if the user needs to add goals and how many.'''

        self.listslp()

        print(self.slptemplist)

##        self.slptemplistgoal = self.goalsetting(self.slptemplist)
##
##        self.slptempcontent = self.listtostr(self.slptemplistgoal)

        
##
##        return self.slptempcontent
##        

    def goalno(self):

        self.slptempcontent = self.openslp('slptemp1')

        return self.slptempcontent

    

s = SlpChart()
