import tkinter as tk
import serial
import struct
from PIL import ImageTk,Image
import time


class gui():
	def __init__(self): 
		self.root = tk.Tk()
		#self.port = serial.Serial('/dev/cu.usbmodem14101',9600)
		self.image = ImageTk.PhotoImage(Image.open('/Users/zxy/Desktop/Actuator_Control/arm_image.jpeg'))
		self.btn_icon = Image.open('/Users/zxy/Desktop/Actuator_Control/icon1.jpg')
		self.btn_icon = self.btn_icon.resize((20, 20), Image.ANTIALIAS)
		self.icon = ImageTk.PhotoImage(self.btn_icon.rotate(45))
		self.icon2 = ImageTk.PhotoImage(self.btn_icon.rotate(225))
		self.icon3 = ImageTk.PhotoImage(self.btn_icon.rotate(315))
		self.icon4 = ImageTk.PhotoImage(self.btn_icon.rotate(135))
		self.icon5 = ImageTk.PhotoImage(self.btn_icon.rotate(90))
		self.icon6 = ImageTk.PhotoImage(self.btn_icon.rotate(270))
		self.icon7 = ImageTk.PhotoImage(self.btn_icon.rotate(10))
		self.icon8 = ImageTk.PhotoImage(self.btn_icon.rotate(200))
		self.canvas = tk.Canvas(self.root, width = 800, height = 569)
		self.l1 = tk.Label(self.root,text = 'System Started')
		self.stop_icon = Image.open('/Users/zxy/Desktop/Actuator_Control/stop.jpg')
		self.stop_icon = ImageTk.PhotoImage(self.stop_icon.resize((150, 90), Image.ANTIALIAS))
		self.quit_icon = Image.open('/Users/zxy/Desktop/Actuator_Control/quit.jpg')
		self.quit_icon = ImageTk.PhotoImage(self.quit_icon.resize((30, 30), Image.ANTIALIAS))
		self.title = tk.Label(self.root,text = 'Soft Robotic Arm Control',fg = "white", bg = "dark blue",font = "Helvetica 24 bold italic")
		self.sec1 = tk.Label(self.root,text = 'Section A1',fg = "white", bg = "dark blue", font = '3')
		self.sec2 = tk.Label(self.root,text = 'Section A2',fg = "white", bg = "dark blue", font = '3')
		self.sec3 = tk.Label(self.root,text = 'Section A3',fg = "white", bg = "dark blue", font = '3')
		self.sec4 = tk.Label(self.root,text = 'Section A4',fg = "white", bg = "dark blue", font = '3')

	def frame(self):
		
		self.canvas.create_image(0,0,anchor = 'nw', image = self.image)

		#Actuator Control Buttons 
		btn1 = tk.Button(self.root,text="I_A1", image=self.icon, bd=0, command = lambda: self.inject(1))
		btn1_config = self.canvas.create_window(698, 340, anchor = 'nw',window = btn1)
		btn_r1 = tk.Button(self.root,text="R_A1",image=self.icon2, bd=0, command = lambda: self.retract(3))
		btn_r1_config = self.canvas.create_window(620, 430, anchor = 'nw',window = btn_r1)

		btn2 = tk.Button(self.root,text="I_A2",image=self.icon4, bd=0, command = lambda: self.inject(4))
		btn2_config = self.canvas.create_window(430, 225, anchor = 'nw',window = btn2)
		btn_r2 = tk.Button(self.root,text="R_A2",image=self.icon3, bd=0, command = lambda: self.retract(5))
		btn_r2_config = self.canvas.create_window(595, 325, anchor = 'nw',window = btn_r2)

		btn3 = tk.Button(self.root,text="I_A3",image=self.icon6, bd=0, command = lambda: self.inject(6))
		btn3_config = self.canvas.create_window(160, 140, anchor = 'nw',window = btn3)
		btn_r3 = tk.Button(self.root,text="R_A3",image=self.icon5, bd=0, command = lambda: self.retract(7))
		btn_r3_config = self.canvas.create_window(165, 60, anchor = 'nw',window = btn_r3)

		btn4 = tk.Button(self.root,text="I_A4",image=self.icon7, bd=0, command = lambda: self.inject(8))
		btn4_config = self.canvas.create_window(120, 210, anchor = 'nw',window = btn4)
		btn_r4 = tk.Button(self.root,text="R_A4",image=self.icon8, bd=0, command = lambda: self.retract(9))
		btn_r4_config = self.canvas.create_window(40, 240, anchor = 'nw',window = btn_r4)
		#btn_stop = tk.Button(self.root,text="STOP",width=15,height=5,foreground = 'red',command = lambda: self.stop(2))
		btn_stop = tk.Button(self.root,image = self.stop_icon,relief='raised',command = lambda: self.stop(2))
		btn_stop_config = self.canvas.create_window(555, 80, anchor = 'nw',window = btn_stop)
		
		#GUI Text and Buttons
		l1_config = self.canvas.create_window(630, 180, anchor = 'n',window = self.l1)
		title_config = self.canvas.create_window(400, 20, anchor = 'n',window = self.title)
		self.canvas.create_window(720, 460, anchor = 'n',window = self.sec1)
		self.canvas.create_window(450, 350, anchor = 'n',window = self.sec2)
		self.canvas.create_window(200, 200, anchor = 'n',window = self.sec3)
		self.canvas.create_window(80, 330, anchor = 'n',window = self.sec4)

		#btn_quit = tk.Button(self.root,text="QUIT",relief='raised',bd=4,width=5,height=2,foreground = 'red',command = lambda: self.quit(2))
		btn_quit = tk.Button(self.root,image = self.quit_icon,bd=4,command = lambda: self.quit(2))
		btn_qiut_config = self.canvas.create_window(30, 510, anchor = 'nw',window =btn_quit )
		self.canvas.pack()
			
	def inject(self,s):
		print(s)
		#self.port.write(struct.pack('>B', s))
		section = ''
		if s == 1:
			section = 'A1'
		elif s == 4:
			section = 'A2'
		elif s == 6:
			section = 'A3'
		elif s == 8:
			section = 'A4'	
		
		string = 'Section ' + section + ' Inflation Started,\n Stops When Fully Deployed'

		self.l1.config(text = string)

	def retract(self,s):
		print(s)
		#self.port.write(struct.pack('>B', s))
		self.l1.config(text = 'Retraction Started')
		self.root.update()
		self.root.after(3000,self.stop(2))
		self.root.update()
		self.root.after(1000)
		self.l1.config(text = 'Retraction Completed')

	def stop(self,s):
		print(s)
		#self.port.write(struct.pack('>B', s))
		self.l1.config(text = 'System Stopped')
	
	def quit(self,s):
		self.stop(s)
		self.root.destroy()
	
	def run(self):
		self.root.title("Control")
		#self.root.geometry('800x600')
		self.frame()
		self.root.mainloop()


def main():
	g=gui()
	g.run()
	    
if __name__ == '__main__':
    main()