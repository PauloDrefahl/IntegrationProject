#Paulo Drefahl
#This program consists basically in a quiz game made with python using the library Tkinter, it is about our COP1500 class and python. 

from tkinter import *

score = 0

class Application:
    #Confg Window
    def __init__(self,master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.title()
        self.description()
        self.start_button()
        self.frame2 = Frame(self.widget1, width=1300, height=700, bg='#A59F9D', bd=10, relief='ridge').pack(side=BOTTOM)
        self.score = 0

    #Score System
    def add_points(self):
        self.score += 1

    def score_screen(self):
        self.show_score = Label(self.frame2, bg="#BEBEBE", text='Your Score:'+str(self.score)+'/10\n Thank you for test my program!!', bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=680)
        self.quiz_question = Label(self.frame2, bg="#BEBEBE",text="Quiz Finished !!", bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="------", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge').place(x=400, y=550)
        self.button2 = Button(text="------", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge').place(x=850, y=550)
        pass

    #Questions
    def question1(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="The name of our instructor is Guido van Rossum",bd=10,relief='ridge',font="Verdana",width=50, height=4).place(x=550,y=380)
        self.button1 = Button(text="TRUE",font="Verdana", bg="#23E863", width=35, height=3,bd=5,relief='ridge',command=self.question2).place(x=400,y=550)
        self.button2 = Button(text="FALSE",font="Verdana", bg="#F22E24", width=35, height=3,bd=5,relief='ridge',command=lambda:[self.question2(), self.add_points()]).place(x=850,y=550)

    def question2(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="The name of our student assistent is Rachel",bd=10, relief='ridge', font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=lambda:[self.question3(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',command=self.question3).place(x=850, y=550)

    def question3(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="We are learning python in this semester", bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=lambda:[self.question4(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',command=self.question4).place(x=850, y=550)

    def question4(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="Python is considered a low level language", bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=self.question5).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',command=lambda:[self.question5(), self.add_points()]).place(x=850, y=550)

    def question5(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="Python is a OOP language", bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=lambda:[self.question6(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',command=self.question6).place(x=850, y=550)

    def question6(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="Python was created in the late 1980s by Scott Vanselow", bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=self.question7).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',command=lambda:[self.question7(), self.add_points()]).place(x=850, y=550)

    def question7(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="Python supports multiple assignments in one statement", bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=lambda:[self.question8(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',command=self.question8).place(x=850, y=550)

    def question8(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="Functions can't return multiple values", bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=self.question9).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',command=lambda:[self.question9(), self.add_points()]).place(x=850, y=550)

    def question9(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="We can do a Certification Exam to get extra credit", bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=lambda:[self.question10(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',command=self.question10).place(x=850, y=550)

    def question10(self):
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="We need should study 6-9hrs / week outside the class", bd=10, relief='ridge',font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=lambda:[self.add_points(), self.score_screen()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',command=self.score_screen).place(x=850, y=550)

    #Main Screen
    def title(self):
        self.title = Label(self.widget1, text="Quiz COP 1500 Intro to computer science")
        self.title["font"] = ("Open Sans","40","italic","bold")
        self.title.pack()

    def description(self):
        self.about = Label(self.widget1, text="About the quiz:")
        self.about["font"] = ("Open Sans","20","italic","bold")
        self.about.pack()
        self.description = Label(self.widget1,text="""This is my integration project for COP 1500 Intro to computer science. 
        I decided to use Tkinter because I love to create graphic interfaces and see changes in the code reflecting directly in the program
        It was also a way to learn more about this wonderful library and develop my python skills.
        By Paulo Drefahl
        """)
        self.description["font"] = ("Open Sans","15")
        self.description.pack()

    def start_button(self):
        self.start = Button(text="start",font="Verdana", bg="#BEBEBE", width=30, height=3,command=self.question1).place(x=650,y=250)


#Starting Graphic Interface
root = Tk()
root.title("Quiz COP 1500 - Intro to computer science By Paulo Drefahl")
root.geometry("1600x800+100+100")
Application(root)
root.mainloop()
