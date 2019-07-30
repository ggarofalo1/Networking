# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CryptoGram", pos = wx.DefaultPosition, size = wx.Size( 325,525 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.MainMenu = wx.MenuBar( 0 )
		self.File = wx.Menu()
		self.Open = wx.Menu()
		self.File.AppendSubMenu( self.Open, u"Open" )

		self.SaveInput = wx.Menu()
		self.File.AppendSubMenu( self.SaveInput, u"Save Input" )

		self.SaveOutput = wx.Menu()
		self.File.AppendSubMenu( self.SaveOutput, u"Save Output" )

		self.About = wx.Menu()
		self.File.AppendSubMenu( self.About, u"About" )

		self.Exit = wx.Menu()
		self.File.AppendSubMenu( self.Exit, u"Exit" )

		self.MainMenu.Append( self.File, u"File" )

		self.SetMenuBar( self.MainMenu )

		mainsizer = wx.BoxSizer( wx.VERTICAL )

		self.NoteBook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH|wx.NB_NOPAGETHEME )
		self.Main = wx.ScrolledWindow( self.NoteBook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.Main.SetScrollRate( 5, 5 )
		page1sizer = wx.BoxSizer( wx.VERTICAL )

		self.TitleName = wx.StaticText( self.Main, wx.ID_ANY, u"CryptoGram", wx.Point( 0,0 ), wx.DefaultSize, 0 )
		self.TitleName.Wrap( -1 )
		self.TitleName.SetFont( wx.Font( 18, 74, 90, 90, False, "Impact" ) )

		page1sizer.Add( self.TitleName, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		ChooseCipherChoices = [ u"Choose A Cipher", u"Caesar Cipher Encrypt", u"Caesar Cipher Decrypt", u"Monoalphabetic Encrypt", u"Monoalphabetic Decrypt", u"Polyalphabetic Encrypt", u"Polyalphabetic Decrypt", u"Block Cipher Encrypt", u"Block Cipher Decrypt", u"Stream Cipher Encrypt", u"Stream Cipher Decrypt", u"Caesar Brute Force", u"Custom Encrypt", u"Custom Decrypt" ]
		self.ChooseCipher = wx.Choice( self.Main, wx.ID_ANY, wx.Point( 0,1 ), wx.DefaultSize, ChooseCipherChoices, 0 )
		self.ChooseCipher.SetSelection( 0 )
		page1sizer.Add( self.ChooseCipher, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.PassTitle = wx.StaticText( self.Main, wx.ID_ANY, u"Password:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.PassTitle.Wrap( -1 )
		page1sizer.Add( self.PassTitle, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.password = wx.TextCtrl( self.Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		page1sizer.Add( self.password, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.inputTitle = wx.StaticText( self.Main, wx.ID_ANY, u"Input:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputTitle.Wrap( -1 )
		page1sizer.Add( self.inputTitle, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.input = wx.TextCtrl( self.Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.input.SetMaxLength( 9999999 )
		self.input.SetMinSize( wx.Size( 250,75 ) )

		page1sizer.Add( self.input, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.outputTitle = wx.StaticText( self.Main, wx.ID_ANY, u"Output:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.outputTitle.Wrap( -1 )
		page1sizer.Add( self.outputTitle, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.output = wx.TextCtrl( self.Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.output.SetMaxLength( 9999999 )
		self.output.SetMinSize( wx.Size( 250,75 ) )

		page1sizer.Add( self.output, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.run = wx.Button( self.Main, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		page1sizer.Add( self.run, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.switch = wx.Button( self.Main, wx.ID_ANY, u"Switch", wx.DefaultPosition, wx.DefaultSize, 0 )
		page1sizer.Add( self.switch, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.Main.SetSizer( page1sizer )
		self.Main.Layout()
		page1sizer.Fit( self.Main )
		self.NoteBook1.AddPage( self.Main, u"Main", True )
		self.Settings = wx.Panel( self.NoteBook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 2, 2, 10, 10 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.checkboxtitle = wx.StaticText( self.Settings, wx.ID_ANY, u"Save output to a text file:", wx.Point( 0,0 ), wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.checkboxtitle.Wrap( -1 )
		fgSizer1.Add( self.checkboxtitle, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.savecheck = wx.CheckBox( self.Settings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.savecheck, 0, wx.ALL, 10 )

		self.titlesavetext = wx.StaticText( self.Settings, wx.ID_ANY, u"Name of File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titlesavetext.Wrap( -1 )
		fgSizer1.Add( self.titlesavetext, 0, wx.ALL, 10 )

		self.savetext = wx.TextCtrl( self.Settings, wx.ID_ANY, u"CryptoGramResult1", wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		self.savetext.SetMaxLength( 200 )
		fgSizer1.Add( self.savetext, 0, wx.ALL, 10 )


		self.Settings.SetSizer( fgSizer1 )
		self.Settings.Layout()
		fgSizer1.Fit( self.Settings )
		self.NoteBook1.AddPage( self.Settings, u"Settings", False )
		self.Custom = wx.ScrolledWindow( self.NoteBook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.Custom.SetScrollRate( 5, 5 )
		fgSizer2 = wx.FlexGridSizer( 7, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.titlecipher1 = wx.StaticText( self.Custom, wx.ID_ANY, u"Cipher 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titlecipher1.Wrap( -1 )
		fgSizer2.Add( self.titlecipher1, 0, wx.ALL, 10 )

		cipher1Choices = [u"Choose A Cipher", u"Caesar Cipher Encrypt", u"Monoalphabetic Encrypt", u"Polyalphabetic Encrypt", u"Block Cipher Encrypt", u"Stream Cipher Encrypt"]
		self.cipher1 = wx.Choice( self.Custom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cipher1Choices, 0 )
		self.cipher1.SetSelection( 0 )
		fgSizer2.Add( self.cipher1, 0, wx.ALL, 10 )

		self.titlepass1 = wx.StaticText( self.Custom, wx.ID_ANY, u"Password 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titlepass1.Wrap( -1 )
		fgSizer2.Add( self.titlepass1, 0, wx.ALL, 10 )

		self.pass1 = wx.TextCtrl( self.Custom, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
		fgSizer2.Add( self.pass1, 0, wx.ALL, 10 )

		self.titlecipher2 = wx.StaticText( self.Custom, wx.ID_ANY, u"Cipher 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titlecipher2.Wrap( -1 )
		fgSizer2.Add( self.titlecipher2, 0, wx.ALL, 10 )

		cipher2Choices = [u"Choose A Cipher", u"Caesar Cipher Encrypt", u"Monoalphabetic Encrypt", u"Polyalphabetic Encrypt", u"Block Cipher Encrypt", u"Stream Cipher Encrypt"]
		self.cipher2 = wx.Choice( self.Custom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cipher2Choices, 0 )
		self.cipher2.SetSelection( 0 )
		fgSizer2.Add( self.cipher2, 0, wx.ALL, 10 )

		self.titlepass2 = wx.StaticText( self.Custom, wx.ID_ANY, u"Password 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titlepass2.Wrap( -1 )
		fgSizer2.Add( self.titlepass2, 0, wx.ALL, 10 )

		self.pass2 = wx.TextCtrl( self.Custom, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
		fgSizer2.Add( self.pass2, 0, wx.ALL, 10 )

		self.titlecipher3 = wx.StaticText( self.Custom, wx.ID_ANY, u"Cipher 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titlecipher3.Wrap( -1 )
		fgSizer2.Add( self.titlecipher3, 0, wx.ALL, 10 )

		cipher3Choices = [u"Choose A Cipher", u"Caesar Cipher Encrypt", u"Monoalphabetic Encrypt", u"Polyalphabetic Encrypt", u"Block Cipher Encrypt", u"Stream Cipher Encrypt"]
		self.cipher3 = wx.Choice( self.Custom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cipher3Choices, 0 )
		self.cipher3.SetSelection( 0 )
		fgSizer2.Add( self.cipher3, 0, wx.ALL, 10 )

		self.titlepass3 = wx.StaticText( self.Custom, wx.ID_ANY, u"Password 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titlepass3.Wrap( -1 )
		fgSizer2.Add( self.titlepass3, 0, wx.ALL, 10 )

		self.pass3 = wx.TextCtrl( self.Custom, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
		fgSizer2.Add( self.pass3, 0, wx.ALL, 10 )


		self.Custom.SetSizer( fgSizer2 )
		self.Custom.Layout()
		fgSizer2.Fit( self.Custom )
		self.NoteBook1.AddPage( self.Custom, u"Custom", False )

		mainsizer.Add( self.NoteBook1, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )


		self.SetSizer( mainsizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.run.Bind( wx.EVT_BUTTON, self.runCipher )
		self.switch.Bind( wx.EVT_BUTTON, self.switchtext )
		self.savecheck.Bind( wx.EVT_CHECKBOX, self.savefile )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def runCipher( self, event ):
		event.Skip()

	def switchtext( self, event ):
		event.Skip()

	def savefile( self, event ):
		event.Skip()


