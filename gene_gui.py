#from gene_finder import gene_finder
from load import load_seq
import wx
import os

class Dialog_Window(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(800,600))
		self.control = wx.Button(self)
app = wx.App()		
frame = wx.Frame(None, -1, 'testing', style =wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.CAPTION | wx.CLOSE_BOX)
frame.Show()
app.MainLoop()