'''
@Author: Galen Garofalo
Date: 7/24/19
Description: A gui for encryption
Icon made by https://www.flaticon.com/authors/smashicons from www.flaticon.com
'''

from Application import encrypt as cryp
from Application import CryptoGramGui
import wx
import os
import io
import tkinter as tk


'''
A gui that uses wxPython to open a file and encrypt it or decrypt it using 
different utils from encrypt
'''


class AppGui(CryptoGramGui.MainFrame):
    global save
    save = False
    if not os.path.exists('results'):
        os.mkdir("results")

    def __init__(self, parent):
        CryptoGramGui.MainFrame.__init__(self, parent)

    def savefile( self, event ):
        global save
        save = self.savecheck.GetValue()

    def switchtext(self, event):
        print("Switch input/output")
        input1 = self.input.GetValue()
        output1 = self.output.GetValue()
        self.input.SetValue(output1)
        self.output.SetValue("")

    def runCipher(self, event):
        # Run the chosen cipher on the input
        '''
        num = int(self.m_textCtrl1.GetValue())
        self.m_textCtrl2.SetValue (str(num*num))
        '''
        print("------------------------------")
        print("Run Cipher")
        cipher = self.ChooseCipher.GetSelection()
        key = self.password.GetValue()
        input = self.input.GetValue()
        global save

        if cipher == 1:
            print("Caesar Encrypt")
            output1 = cryp.caesarshiften(key, input)
            global save
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("====Caesar Encrypt====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 2:
            print("Caesar Decrypt")
            output1 = cryp.caesarshiftde(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("====Caesar Decrypt====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 3:
            print("Mono Encrypt")
            output1 = cryp.monoalphabeticen(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("======Mono Encrypt=====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 4:
            print("Mono Decrypt")
            output1 = cryp.monoalphabeticde(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("======Mono Decrypt=====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 5:
            print("Poly Encrypt")
            output1 = cryp.polyalphabeticen(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("======Poly Encrypt=====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 6:
            print("Poly Decrypt")
            output1 = cryp.polyalphabeticde(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("======Poly Decrypt=====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 7:
            print("Block Encrypt")
        elif cipher == 8:
            print("Block Decrypt")
        elif cipher == 9:
            print("Stream Encrypt")
        elif cipher == 10:
            print("Stream Decrypt")
        elif cipher == 11:
            print("Caesar Brute Force")
            output1 = cryp.caesarshiftbrute(input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("=====Caesar Brute=====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        else:
            print("Invalid Choice")

# setup the gui
app = wx.App(False)
frame = AppGui(None)
frame.SetIcon(wx.Icon("locked.png"))
frame.Show(True)
# start the applications
app.MainLoop()

#################################
#                               #
#   Nothing Needed After This   #
#                               #
#################################
'''
# the tkinter look for a helloworld
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
'''

'''
# Hello World App
app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop() 
'''

'''
# a simple text editor
class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()  
'''

'''
# a simple text editor in wxPython
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()  # A Status bar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open a file to edit")
        menuAbout= filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", " Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self, e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " A sample editor \n in wxPython", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self, e):
        self.Close(True)  # Close the frame.

    def OnOpen(self, e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()
'''

'''
# an indepth example panel for gui
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.quote = wx.StaticText(self, label="Your quote: ")
        grid.Add(self.quote, pos=(0,0))

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger = wx.TextCtrl(self, size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A button
        self.button =wx.Button(self, label="Save")
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="Your name :")
        grid.Add(self.lblname, pos=(1,0))
        self.editname = wx.TextCtrl(self, value="Enter here your name", size=(140,-1))
        grid.Add(self.editname, pos=(1,1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # the combobox Control
        self.sampleList = ['friends', 'advertising', 'web search', 'Yellow Pages']
        self.lblhear = wx.StaticText(self, label="How did you hear from us ?")
        grid.Add(self.lblhear, pos=(3,0))
        self.edithear = wx.ComboBox(self, size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        grid.Add(self.edithear, pos=(3,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)

        # add a spacer to the sizer
        grid.Add((10, 40), pos=(2,0))

        # Checkbox
        self.insure = wx.CheckBox(self, label="Do you want Insured Shipment ?")
        grid.Add(self.insure, pos=(4,0), span=(1,2), flag=wx.BOTTOM, border=5)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # Radio Boxes
        radioList = ['blue', 'red', 'yellow', 'orange', 'green', 'purple', 'navy blue', 'black', 'gray']
        rb = wx.RadioBox(self, label="What color would you like ?", pos=(20, 210), choices=radioList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        grid.Add(rb, pos=(5,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(self.logger)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(self.button, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)
    def OnClick(self, e):
        dlg = wx.MessageDialog(self, " OnClick", "Example Panel", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.
    def EvtText(self, e):
        dlg = wx.MessageDialog(self, " EvtText", "Example Panel", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.
    def EvtChar(self, e):
        dlg = wx.MessageDialog(self, " EvtChar", "Example Panel", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.
    def EvtComboBox(self, e):
        dlg = wx.MessageDialog(self, " EvtComboBox", "Example Panel", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.
    def EvtCheckBox(self, e):
        dlg = wx.MessageDialog(self, " EvtCheckBox", "Example Panel", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.
    def EvtRadioBox(self, e):
        dlg = wx.MessageDialog(self, " EvtRadioBox", "Example Panel", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

app = wx.App(False)
frame = wx.Frame(None, title="Demo with Notebook")
nb = wx.Notebook(frame)


nb.AddPage(ExamplePanel(nb), "Absolute Positioning")
nb.AddPage(ExamplePanel(nb), "Page Two")
nb.AddPage(ExamplePanel(nb), "Page Three")
frame.Show()
app.MainLoop()
'''

