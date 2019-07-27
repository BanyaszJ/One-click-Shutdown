# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import subprocess

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"1 hour", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        bSizer1.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"2 hours", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button2.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        bSizer1.Add( self.m_button2, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"3 hours", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button3.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        bSizer1.Add( self.m_button3, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button4.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        bSizer1.Add( self.m_button4, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.oneHour )
        self.m_button1.Bind( wx.EVT_RIGHT_UP, self.RightUp )
        self.m_button2.Bind( wx.EVT_BUTTON, self.twoHours )
        self.m_button2.Bind( wx.EVT_RIGHT_UP, self.RightUp )
        self.m_button3.Bind( wx.EVT_BUTTON, self.threeHours )
        self.m_button3.Bind( wx.EVT_RIGHT_UP, self.RightUp )
        self.m_button4.Bind( wx.EVT_BUTTON, self.cancelHours )
        self.m_button4.Bind( wx.EVT_RIGHT_UP, self.RightUp )
        self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyUP)
        self.Bind(wx.EVT_RIGHT_UP, self.RightUp)

    def __del__( self ):
        pass


	# Virtual event handlers, overide them in your derived class
    def RightUp( self, event ):
        self.Close()
    
    def OnKeyUP( self, event ):
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_ESCAPE:
            self.Close()
        event.Skip() 
        
    def oneHour( self, event ):
        subprocess.call(["shutdown", "-s", "-t", "3600"])

    def twoHours( self, event ):
        subprocess.call(["shutdown", "-s", "-t", "7200"])

    def threeHours( self, event ):
        subprocess.call(["shutdown", "-s", "-t", "10800"])

    def cancelHours( self, event ):
        subprocess.call(["shutdown", "-a"])


#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of CalcFrame
frame = MyFrame1(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()