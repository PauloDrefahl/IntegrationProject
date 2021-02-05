from tkinter import *
#Name: Paulo Henrique Mocelin Drefahl
#This is my integration Project for COP1500 - Intro to Computer Science. I have been working on it since our first class
#It consists basically in a Quiz about our class, a calculator, and a String operator. To built the graphic interface I
#used a library called TKinter.

#Instructions: 1 - Run the code.
# 2- Now, Write your name and click on "greetings" button.
# 3- Then, choose an application and test it. To test more the other applications, close and run the .py file again


#Main Program

#Calculator Application
def calcenter():
    main_screen.destroy()
    root = Tk()
    root.geometry("500x500+100+100")
    root.title("Calculator COP 1500 - Intro to computer science By Paulo Drefahl")
    calculator(root)
    root.mainloop()
class calculator:
    def __init__(self,master=None):
        self.widget2 = Frame(master)
        self.widget2.pack()
        self.n1 = DoubleVar()
        self.n2 = DoubleVar()
        self.numbers()

#Aritmatic Operators
    def sum1(self):
        self.result = self.n1.get() + self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans","20")
        self.label1.pack()

    def sub1(self):
        self.result = self.n1.get() - self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def mult1(self):
        self.result = self.n1.get() * self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def exp1(self):
        self.result = self.n1.get() ** self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def div1(self):
        self.result = self.n1.get() / self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def rest1(self):
        self.result = self.n1.get() % self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def comp_div1(self):
        self.result = self.n1.get() // self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def numbers(self):
        self.label1 = Label(self.widget2, text="First Number:").pack()
        self.number1 = (Entry(self.widget2, textvar=self.n1).pack())
        self.label2 = Label(self.widget2, text="Second Number").pack()
        self.number2 = (Entry(self.widget2, textvar=self.n2).pack())
        self.plus = Button(text="+",font="Verdana",command=self.sum1).pack()
        self.minus = Button(text="-",font="Verdana",command=self.sub1).pack()
        self.mult = Button(text="*",font="Verdana",command=self.mult1).pack()
        self.expo = Button(text="**",font="Verdana",command=self.exp1).pack()
        self.div = Button(text="/",font="Verdana",command=self.div1).pack()
        self.restof = Button(text="%",font="Verdana",command=self.rest1).pack()
        self.compdiv = Button(text="//",font="Verdana",command=self.comp_div1).pack()


#Quiz Application
def quizenter():
    main_screen.destroy()
    root = Tk()
    root.title("Quiz COP 1500 - Intro to computer science By Paulo Drefahl")
    root.geometry("1600x800+100+100")
    Application(root)
    root.mainloop()
class Application:

    #Confg quiz Application
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

    #Quiz Widgets
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


#String operators Application
def stringenter():
    main_screen.destroy()
    root = Tk()
    root.geometry("500x500+100+100")
    root.title("String operator COP 1500 - Intro to computer science By Paulo Drefahl")
    string_application(root)
    root.mainloop()
class string_application:
    def __init__(self,master=None):
        self.str1 = StringVar()
        self.str2 = StringVar()
        self.n_rep = IntVar()
        self.widget3 = Frame(master)
        self.widget3.pack()
        self.labelstr = Label(self.widget3, text="Type a String").pack()
        self.string1 = (Entry(self.widget3, textvar=self.str1).pack())
        self.labelstr1 = Label(self.widget3, text="+").pack()
        self.labelstr2 = Label(self.widget3, text="Type another String").pack()
        self.string2 = (Entry(self.widget3, textvar=self.str2).pack())
        self.times = Label(self.widget3, text="Number of repetitions (integer)").pack()
        self.rep = (Entry(self.widget3, textvar=self.n_rep).pack())
        self.buttonrep = Button(text="Enter",font="Verdana",command=self.repete).pack()

    def repete(self):
        self.result_rep = (self.str1.get() + self.str2.get()) * self.n_rep.get()
        self.final_str = Label(self.widget3, text="Result:\n {}".format(self.result_rep)).pack()




#Starting Main Graphic Interface and Global variables
main_screen = Tk()
main_screen.geometry("420x400+100+100")
main_screen.title("COP 1500 - integration project by Paulo Drefahl")
score = 0

#Greetings
def greetings():
    labelgret['text'] = "Welcome {}!".format(username.get())
usernameLbl = Label(text="Name:")
usernameLbl["font"] = ("Open Sans","15")
usernameLbl.pack()
initLabel = Label(text="Choose the Application:")
username = StringVar()
usernameentry = (Entry(textvar=username).pack())
labelgret = Label(text="")
labelgret["font"] = ("Open Sans","20")
labelgret.pack()
Greetings =  Button(text="Greetings", font="Verdana", command=greetings).pack()
initLabel["font"] = ("Open Sans","20")
initLabel.pack()



#Buttons to Choose Aplication
buttonquiz = Button(text="Quiz", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',command=quizenter).pack()
buttoncal = Button(text="Calculator", font="Verdana", bg="#33B8EB", width=35, height=3, bd=5, relief='ridge',command=calcenter).pack()
buttonstring = Button(text="String Operator", font="Verdana", bg="red", width=35, height=3, bd=5, relief='ridge',command=stringenter).pack()
main_screen.mainloop()

#sources: "Curso em video - Udemy (portuguese Brazil)", "Python docummentation", "Tkinter docummentation"
