from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import datetime as DT
import time
import os
import sys

class popupManager(simpledialog.Dialog):

	def body(self, master):

		Label(master, text="Enter Description:").grid(row=0)
		Label(master, text="Enter Time (h:mm AM/PM:").grid(row=1)

		self.e1 = Entry(master)
		self.e2 = Entry(master)
		print(self.e1.get())

		self.e1.grid(row=0, column=1)
		self.e2.grid(row=1, column=1)
		
		eventDescription = self.e1.get()
		eventTime = self.e2.get()
		
		return self.e1 # initial focus

	def apply(self):
		eventDescription = str(self.e1.get())
		eventTime = str(self.e2.get())

		#Calculate time
		hours, minutes = eventTime.split(":")
		minutes, shift = minutes.split(" ")
		if (shift == "PM"):
			hours = int(hours,10) + 12
		now = DT.datetime.now()
		target = DT.datetime.combine(DT.date.today(), DT.time(hour=hours, minute=int(minutes,10)))
		if target < now:
			target += DT.timedelta(days=1)

		seconds = (target-now).total_seconds()
		time.sleep(seconds)

		messagebox.showinfo("Reminder", eventDescription)

root = Tk()
root.withdraw()
popupManager(root)