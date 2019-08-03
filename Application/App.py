'''
@Author: Galen Garofalo
Date: 7/24/19
Description: A gui that uses wxPython to open a file and encrypt it or decrypt it using
        different utils from encrypt.py and the gui from CryptoGramGui.py
Icon made by https://www.flaticon.com/authors/smashicons from www.flaticon.com
'''

# Run:
# pyinstaller --onefile App.spec
# For a Python -> .exe file
# For installer might use NSIS or Inno Setup

##############  TO DO:  #################
#                                       #
#  Fix decrypt spits out ~ for \n       #
#  Add Block Cipher                     #
#  Add Stream Cipher                    #
#                                       #
#########################################

import encrypt as cryp
import CryptoGramGui

import wx
import os
import io
import sys


class AppGui(CryptoGramGui.MainFrame):
    global save
    save = False
    if not os.path.exists('results'):
        os.mkdir("results")

    def __init__(self, parent):
        CryptoGramGui.MainFrame.__init__(self, parent)
        self.dirname=''

    def onopen(self, e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.input.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def onabout(self, e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " A program that encrypts simple messages made with Python, wxPython and PyInstaller.\n\n  ", "About CryptoGram", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def onexit(self, e):
        self.Close(True)

    def savefile(self, event):
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

        if len(key) == 0:
                key = "12345"

        input = self.input.GetValue()
        global save
        if cipher == 0:
            cipher = 1
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
                file.write("======Mono Encrypt====\n")
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
                file.write("======Mono Decrypt====\n")
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
                file.write("=====Poly Encrypt=====\n")
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
                file.write("=====Poly Decrypt=====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 7:
            print("Block Encrypt")
            output1 = cryp.blockcipheren(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("=====Block Encrypt====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 8:
            print("Block Decrypt")
            output1 = cryp.blockcipherde(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("=====Block Decrypt====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 9:
            print("Stream Encrypt")
            output1 = cryp.streamcipheren(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("====Stream Encrypt====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        elif cipher == 10:
            print("Stream Decrypt")
            output1 = cryp.streamcipherde(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("====Stream Decrypt====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
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
        elif cipher == 12:
            print("Custom Encrypt")
            cipher1 = self.cipher1.GetSelection()
            cipher2 = self.cipher2.GetSelection()
            cipher3 = self.cipher3.GetSelection()

            pass1 = self.pass1.GetValue()
            pass2 = self.pass2.GetValue()
            pass3 = self.pass3.GetValue()

            if len(pass1) == 0:
                pass1 = "12345"
            if len(pass2) == 0:
                pass2 = "12345"
            if len(pass3) == 0:
                pass3 = "12345"

            output1 = cryp.cipherchoiceen(cipher1, input, pass1)
            output2 = cryp.cipherchoiceen(cipher2, output1, pass2)
            output3 = cryp.cipherchoiceen(cipher3, output2, pass3)

            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("====Custom Encrypt====\n")
                file.write(output3)
                file.close()
            self.output.SetValue(str(output3))

        elif cipher == 13:
            print("Custom Decrypt")
            cipher1 = self.cipher1.GetSelection()
            cipher2 = self.cipher2.GetSelection()
            cipher3 = self.cipher3.GetSelection()

            pass1 = self.pass1.GetValue()
            pass2 = self.pass2.GetValue()
            pass3 = self.pass3.GetValue()

            if len(pass1) == 0:
                pass1 = "12345"
            if len(pass2) == 0:
                pass2 = "12345"
            if len(pass3) == 0:
                pass3 = "12345"

            output1 = cryp.cipherchoicede(cipher3, input, pass3)
            output2 = cryp.cipherchoicede(cipher2, output1, pass2)
            output3 = cryp.cipherchoicede(cipher1, output2, pass1)

            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("====Custom Decrypt====\n")
                file.write(output3)
                file.close()
            self.output.SetValue(str(output3))

        elif cipher == 14:
            print("Vigenere Encrypt")
            output1 = cryp.vigenerecipheren(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("=====Vigenere Encrypt=====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))

        elif cipher == 15:
            print("Vigenere Decrypt")
            output1 = cryp.vigenerecipherde(key, input)
            if(save):
                filename = self.savetext.GetValue()
                file = io.open("results/"+filename, "a+", encoding="utf-8")
                file.write("\n======New Output======\n")
                file.write("=====Vigenere Decrypt=====\n")
                file.write(output1)
                file.close()
            self.output.SetValue(str(output1))
        else:
            print("Invalid Choice")

#get image path
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("img/3dLock.ico")

# setup the gui
app = wx.App(False)
frame = AppGui(None)
frame.SetIcon(wx.Icon(Logo))
frame.Show(True)
# start the applications
app.MainLoop()

