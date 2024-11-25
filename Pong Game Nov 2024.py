from tkinter import *
import time

window = Tk()

window.geometry('800x600')
window.title ('Pong Game')
canvas=Canvas(window, width=800, height=600)
canvas.pack()

class Ball:
    def __init__(self, i_paddle, i_color):
        self.platform1 = i_paddle # adding the paddle object to be able to access it
        self.id = canvas.create_oval(10,10,25,25,fill=i_color)
        self.x = 10
        self.y = 10
        canvas.move(self.id,self.x,self.y)

    def update_position(self):
        canvas.move(self.id, self.x, self.y)
        pos = canvas.coords (self.id)
        #make the ball bounce on the edge
        if pos[1]<0:  
            self.y=1
        if pos[3]>canvas.winfo_height():
            self.y=-1
        if pos[0] <=0:
            self.x= 3 #initially x = -3 so if it hits the left wall x needs to change to positive
        if pos[2]>=canvas.winfo_width():
            self.x=-3 #if ball hits the right wall x needs to change to negative number.
        if self.hit_platform():
           self.y = self.y*-1

    def hit_platform (self):
        ball_pos = canvas.coords(self.id)
        paddle_pos=canvas.coords(self.platform1.id)
        return (ball_pos[2]>=paddle_pos[0] 
            and ball_pos[0]<paddle_pos[2] 
            and ball_pos[3]>=paddle_pos[1] 
            and ball_pos[1]<paddle_pos[3])
  

class Paddle:
    def __init__(self, i_color):
       self.id = canvas.create_rectangle(0,0,100,10,fill=i_color)
       canvas.move(self.id,200,300)
       self.x = 3
       canvas.bind_all("<Any-KeyPress>", self.moving)

    def update_position(self):
        canvas.move(self.id, self.x, 0)
        pos = canvas.coords (self.id)
        if pos[0] <=0:
            self.x= 3
        if pos[2] >= canvas.winfo_width():
            self.x = -3

    def moving (self,event):
        if event.keysym == 'Right':
            self.x = 2
        elif event.keysym == 'Left':
            self.x = -2

paddle = Paddle('blue')
ball=Ball(paddle,'red')


while 1:
 ball.update_position()
 paddle.update_position()
 window.update()
 time.sleep(0.01)
