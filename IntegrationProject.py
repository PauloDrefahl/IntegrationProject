"""" Name: Paulo Henrique Mocelin Drefahl
This is my integration Project for COP1500 - Intro to Computer Science. I have been working on it since our first class
It consists basically in a Quiz about our class, a calculator, and a String operator. To built the graphic interface I
used a library called TKinter.
Main Program"""
__author__ = "Paulo Drefahl"

try:
    from tkinter import *
except ModuleNotFoundError:
    print("You do not have the tkinter library installed. The application will not work")

try:
    import numpy as np
except ModuleNotFoundError:
    print("You do not have the numpy library installed. The application will not work")

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("You do not have the matplotlib library installed. The graph app will not work")


def calcenter():
    """
    Initiate the calculator interface
    :return:
    """
    main_screen.destroy()
    root = Tk()
    root.geometry("500x500+100+100")
    root.title("Calculator COP 1500 - Intro to computer science By Paulo Drefahl")
    MyCalculator(root)
    root.mainloop()


class MyCalculator:
    """
    Configure calculator interface
    """
    def __init__(self, master=None):
        self.widget2 = Frame(master)
        self.widget2.pack()
        self.n1 = DoubleVar()
        self.n2 = DoubleVar()
        self.numbers()

    # Aritmatic Operators
    def sum1(self):
        """

        :return:
        """
        self.result = self.n1.get() + self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def sub1(self):
        """

        :return:
        """
        self.result = self.n1.get() - self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def mult1(self):
        """

        :return:
        """
        self.result = self.n1.get() * self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def exp1(self):
        """

        :return:
        """
        self.result = self.n1.get() ** self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def div1(self):
        """

        :return:
        """
        self.result = self.n1.get() / self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def rest1(self):
        """

        :return:
        """
        self.result = self.n1.get() % self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def comp_div1(self):
        """

        :return:
        """
        self.result = self.n1.get() // self.n2.get()
        self.label1 = Label(self.widget2, text="Result: {}".format(self.result))
        self.label1['font'] = ("Open Sans", "20")
        self.label1.pack()

    def numbers(self):
        """

        :return:
        """
        self.label1 = Label(self.widget2, text="First Number:").pack()
        self.number1 = (Entry(self.widget2, textvar=self.n1).pack())
        self.label2 = Label(self.widget2, text="Second Number").pack()
        self.number2 = (Entry(self.widget2, textvar=self.n2).pack())
        self.plus = Button(text="+", font="Verdana", command=self.sum1).pack()
        self.minus = Button(text="-", font="Verdana", command=self.sub1).pack()
        self.mult = Button(text="*", font="Verdana", command=self.mult1).pack()
        self.expo = Button(text="**", font="Verdana", command=self.exp1).pack()
        self.div = Button(text="/", font="Verdana", command=self.div1).pack()
        self.restof = Button(text="%", font="Verdana", command=self.rest1).pack()
        self.compdiv = Button(text="//", font="Verdana", command=self.comp_div1).pack()


# Quiz Application
def quizenter():
    """

    :return:
    """
    main_screen.destroy()
    root = Tk()
    root.title("Quiz COP 1500 - Intro to computer science By Paulo Drefahl")
    root.geometry("1600x800+100+100")
    Application(root)
    root.mainloop()


class Application:
    """
    Quiz Interface configuration
    """
    # Confg quiz Application
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.title()
        self.description()
        self.start_button()
        self.frame2 = Frame(self.widget1, width=1300, height=700, bg='#A59F9D', bd=10, relief='ridge').pack(side=BOTTOM)
        self.score = 0

    # Score System
    def add_points(self):
        """

        :return:
        """
        self.score += 1

    def score_screen(self):
        """

        :return:
        """
        self.show_score = Label(self.frame2, bg="#BEBEBE",
                                text='Your Score:' + str(self.score) + '/10\n Thank you for testing my program!!',
                                bd=10, relief='ridge', font="Verdana", width=50, height=4).place(x=550, y=680)
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="Quiz Finished !!", bd=10, relief='ridge',
                                   font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="------", font="Verdana", bg="#23E863", width=35, height=3, bd=5,
                              relief='ridge').place(x=400, y=550)
        self.button2 = Button(text="------", font="Verdana", bg="#F22E24", width=35, height=3, bd=5,
                              relief='ridge').place(x=850, y=550)
        pass

    # Questions
    def question1(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="The name of our instructor is Guido van Rossum",
                                   bd=10, relief='ridge', font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=self.question2).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.question2(), self.add_points()]).place(x=850, y=550)

    def question2(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="The name of our student assistent is Rachel", bd=10,
                                   relief='ridge', font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.question3(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=self.question3).place(x=850, y=550)

    def question3(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="We are learning python in this semester", bd=10,
                                   relief='ridge', font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.question4(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=self.question4).place(x=850, y=550)

    def question4(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="Python is considered a low level language", bd=10,
                                   relief='ridge', font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=self.question5).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.question5(), self.add_points()]).place(x=850, y=550)

    def question5(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="Python is a OOP language", bd=10, relief='ridge',
                                   font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.question6(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=self.question6).place(x=850, y=550)

    def question6(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE",
                                   text="Python was created in the late 1980s by Scott Vanselow", bd=10, relief='ridge',
                                   font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=self.question7).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.question7(), self.add_points()]).place(x=850, y=550)

    def question7(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE",
                                   text="Python supports multiple assignments in one statement", bd=10, relief='ridge',
                                   font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.question8(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=self.question8).place(x=850, y=550)

    def question8(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="Functions can't return multiple values", bd=10,
                                   relief='ridge', font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=self.question9).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.question9(), self.add_points()]).place(x=850, y=550)

    def question9(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE", text="We can do a Certification Exam to get extra credit",
                                   bd=10, relief='ridge', font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.question10(), self.add_points()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=self.question10).place(x=850, y=550)

    def question10(self):
        """

        :return:
        """
        self.quiz_question = Label(self.frame2, bg="#BEBEBE",
                                   text="We need should study 6-9hrs / week outside the class", bd=10, relief='ridge',
                                   font="Verdana", width=50, height=4).place(x=550, y=380)
        self.button1 = Button(text="TRUE", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                              command=lambda: [self.add_points(), self.score_screen()]).place(x=400, y=550)
        self.button2 = Button(text="FALSE", font="Verdana", bg="#F22E24", width=35, height=3, bd=5, relief='ridge',
                              command=self.score_screen).place(x=850, y=550)

    # Quiz Widgets
    def title(self):
        """

        :return:
        """
        self.title = Label(self.widget1, text="Quiz COP 1500 Intro to computer science")
        self.title["font"] = ("Open Sans", "40", "italic", "bold")
        self.title.pack()

    def description(self):
        """

        :return:
        """
        self.about = Label(self.widget1, text="About the quiz:")
        self.about["font"] = ("Open Sans", "20", "italic", "bold")
        self.about.pack()
        self.description = Label(self.widget1, text="""This is my integration project 
        for COP 1500 Intro to computer science. 
        I decided to use Tkinter because I love to create graphic interfaces and see 
        changes in the code reflecting directly in the program
        It was also a way to learn more about this wonderful library and develop my
        python skills. By Paulo Drefahl
        """)
        self.description["font"] = ("Open Sans", "15")
        self.description.pack()

    def start_button(self):
        """

        :return:
        """
        self.start = Button(text="start", font="Verdana", bg="#BEBEBE", width=30, height=3,
                            command=self.question1).place(x=650, y=250)


# String operators Application
def stringenter():
    """

    :return:
    """
    main_screen.destroy()
    root = Tk()
    root.geometry("500x500+100+100")
    root.title("String operator COP 1500 - Intro to computer science By Paulo Drefahl")
    StringApplication(root)
    root.mainloop()


class StringApplication:
    """
    Configure String Operator Interface
    """
    def __init__(self, master=None):
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
        self.buttonrep = Button(text="Enter", font="Verdana", command=self.repete).pack()

    def repete(self):
        """

        :return:
        """
        self.result_rep = (self.str1.get() + self.str2.get()) * self.n_rep.get()
        self.final_str = Label(self.widget3, text="Result:\n {}".format(self.result_rep)).pack()


# Data Analyzer Application

def dataenter():
    """

    :return:
    """
    main_screen.destroy()
    root = Tk()
    root.geometry("500x500+100+100")
    root.title("String operator COP 1500 - Intro to computer science By Paulo Drefahl")
    DataanalyzerApplication(root)
    root.mainloop()


class DataanalyzerApplication:
    """
    Configure Data Analyzer Interface
    """
    def analize_it(self):
        """

        :return:
        """
        self.emplabel = Label(text="").pack()
        self.labeldataapp2 = Label(text="Information About '{}':".format(self.main_data.get()))
        self.labeldataapp2["font"] = ("Open Sans", "15")
        self.labeldataapp2.pack()

        # Analize Number
        try:
            if isinstance(int(self.main_data.get()), int):
                self.labeldataapp2 = Label(text="It is a number")
                self.labeldataapp2["font"] = ("Open Sans", "15")
                self.labeldataapp2.pack()

            if 1 < int(self.main_data.get()) < 100:
                self.labeldataapp3 = Label(text="This number is between 1 and 100")
                self.labeldataapp3["font"] = ("Open Sans", "15")
                self.labeldataapp3.pack()
            else:
                self.labeldataapp3 = Label(text="This number is not between 1 and 100")
                self.labeldataapp3["font"] = ("Open Sans", "15")
                self.labeldataapp3.pack()

            if int(self.main_data.get()) % 2 == 0:
                self.labeldataapp4 = Label(text="This number is even")
                self.labeldataapp4["font"] = ("Open Sans", "15")
                self.labeldataapp4.pack()
            else:
                self.labeldataapp4 = Label(text="This number is odd")
                self.labeldataapp4["font"] = ("Open Sans", "15")
                self.labeldataapp4.pack()

            if 150 <= int(self.main_data.get()) or int(self.main_data.get()) <= -150:
                self.labeldataapp5 = Label(text="This number bigger/igual 150\nor it is less/igual -150")
                self.labeldataapp5["font"] = ("Open Sans", "15")
                self.labeldataapp5.pack()
            else:
                self.labeldataapp5 = Label(text="This number is neither bigger/igual 150\nor less/igual -150")
                self.labeldataapp5["font"] = ("Open Sans", "15")
                self.labeldataapp5.pack()

            if int(self.main_data.get()) != 0:
                self.labeldataapp6 = Label(text="It is different than 0")
                self.labeldataapp6["font"] = ("Open Sans", "15")
                self.labeldataapp6.pack()
            else:
                self.labeldataapp6 = Label(text="It is igual 0")
                self.labeldataapp6["font"] = ("Open Sans", "15")
                self.labeldataapp6.pack()

        # Analize String
        except ValueError:
            self.labeldataapp2 = Label(text="It is a string")
            self.labeldataapp2["font"] = ("Open Sans", "15")
            self.labeldataapp2.pack()

            if self.main_data.get().count('a') < 1:
                self.labeldataapp2 = Label(text="There is no letter 'a'")
                self.labeldataapp2["font"] = ("Open Sans", "15")
                self.labeldataapp2.pack()
            else:
                self.labeldataapp2 = Label(text="There is the letter 'a'")
                self.labeldataapp2["font"] = ("Open Sans", "15")
                self.labeldataapp2.pack()

            if self.main_data.get().isalpha():
                self.labeldataapp3 = Label(text="There are no numbers")
                self.labeldataapp3["font"] = ("Open Sans", "15")
                self.labeldataapp3.pack()
            else:
                self.labeldataapp3 = Label(text="There are numbers")
                self.labeldataapp3["font"] = ("Open Sans", "15")
                self.labeldataapp3.pack()

            self.labeldataapp4 = Label(text="There are {} characters".format(len(self.main_data.get())))
            self.labeldataapp4["font"] = ("Open Sans", "15")
            self.labeldataapp4.pack()

            if not self.main_data.get() == "apple":
                self.labeldataapp4 = Label(text="This string is not 'apple'")
                self.labeldataapp4["font"] = ("Open Sans", "15")
                self.labeldataapp4.pack()
            else:
                self.labeldataapp4 = Label(text="This string is the same as 'apple'")
                self.labeldataapp4["font"] = ("Open Sans", "15")
                self.labeldataapp4.pack()

    def __init__(self, master=None):
        self.widget4 = Frame(master)
        self.widget4.pack()
        self.labeldataapp = Label(text="type anything:")
        self.labeldataapp["font"] = ("Open Sans", "15")
        self.labeldataapp.pack()
        self.main_data = StringVar()
        self.dataentry = (Entry(textvar=self.main_data).pack())
        self.analyzebutton = Button(text="Analyze Data", font="Verdana", bg="#A59F9D", width=15, height=2, bd=5,
                                    relief='ridge', command=self.analize_it).pack()
        self.labeldataapp1 = Label(text="type anything:")
        self.labeldataapp1["font"] = ("Open Sans", "15")


# starting Graphing Calculator Application

def funcenter():
    """

    :return:
    """
    main_screen.destroy()
    root = Tk()
    root.geometry("500x500+100+100")
    root.title("String operator COP 1500 - Intro to computer science By Paulo Drefahl")
    GraphFuncApplication(root)
    root.mainloop()


class GraphFuncApplication:
    """
    Configure GraphCalculator Interface
    """
    def graphthis(self):
        """

        :return:
        """
        x = np.linspace(0, 10, 11)
        m = float(self.mvalue.get())
        b = float(self.bvalue.get())
        plt.plot(x, m * x + b)
        plt.ylabel('Graph: y = mx + b')
        plt.show()

    def graphthisparabola(self):
        """

        :return:
        """
        x = np.linspace(-15, 15, 1000)
        y = float(self.avalue.get()) * x ** 2 + float(self.b1value.get()) * x + float(self.cvalue.get())
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()

    def __init__(self, master=None):
        self.widget5 = Frame(master)
        self.widget5.pack()

        # Line intercept Equation

        self.equation = Label(text="y = mx + b")
        self.equation["font"] = ("Open Sans", "25")
        self.equation.pack()
        self.mvalue = StringVar()
        self.bvalue = StringVar()
        self.m = Label(text="type a value for m:")
        self.m["font"] = ("Open Sans", "15")
        self.m.pack()
        self.mentry = (Entry(textvar=self.mvalue).pack())
        self.b = Label(text="type a value for b:")
        self.b["font"] = ("Open Sans", "15")
        self.b.pack()
        self.mentry = (Entry(textvar=self.bvalue).pack())
        self.graphbutton = Button(text="graph", font="Verdana", bg="#A59F9D", width=15, height=2, bd=5, relief='ridge',
                                  command=self.graphthis).pack()

        # Quadratic Equation

        self.equation = Label(text="y = ax2 + bx + c")
        self.equation["font"] = ("Open Sans", "25")
        self.equation.pack()
        self.avalue = StringVar()
        self.b1value = StringVar()
        self.cvalue = StringVar()
        self.a = Label(text="type a value for a:")
        self.a["font"] = ("Open Sans", "15")
        self.a.pack()
        self.aentry = (Entry(textvar=self.avalue).pack())
        self.b1 = Label(text="type a value for b:")
        self.b1["font"] = ("Open Sans", "15")
        self.b1.pack()
        self.b1entry = (Entry(textvar=self.b1value).pack())
        self.c = Label(text="type a value for c:")
        self.c["font"] = ("Open Sans", "15")
        self.c.pack()
        self.centry = (Entry(textvar=self.cvalue).pack())
        self.graphparabolabutton = Button(text="graph", font="Verdana", bg="#A59F9D", width=15, height=2, bd=5,
                                          relief='ridge',
                                          command=self.graphthisparabola).pack()


# Starting Main Graphic Interface and Global variables
main_screen = Tk()
main_screen.geometry("420x600+100+100")
main_screen.title("COP 1500 - integration project by Paulo Drefahl")
score = 0


# Greetings Function at the top of Application
def greetings():
    """

    :return:
    """
    labelgret['text'] = "Welcome {}!".format(username.get())


usernameLbl = Label(text="Name:")
usernameLbl["font"] = ("Open Sans", "15")
usernameLbl.pack()
initLabel = Label(text="Choose the Application:")
username = StringVar()
usernameentry = (Entry(textvar=username).pack())
labelgret = Label(text="")
labelgret["font"] = ("Open Sans", "20")
labelgret.pack()
Greetings = Button(text="Greetings", font="Verdana", command=greetings).pack()
initLabel["font"] = ("Open Sans", "20")
initLabel.pack()

# Buttons to Choose Aplication

buttonquiz = Button(text="Quiz", font="Verdana", bg="#23E863", width=35, height=3, bd=5, relief='ridge',
                    command=quizenter).pack()
buttoncal = Button(text="Calculator", font="Verdana", bg="#33B8EB", width=35, height=3, bd=5, relief='ridge',
                   command=calcenter).pack()
buttonstring = Button(text="String Operator", font="Verdana", bg="red", width=35, height=3, bd=5, relief='ridge',
                      command=stringenter).pack()
buttonanalyzer = Button(text="Data Analyzer", font="Verdana", bg="grey", width=35, height=3, bd=5, relief='ridge',
                        command=dataenter).pack()
buttonfuncgraph = Button(text="Graph Tool", font="Verdana", bg="orange", width=35, height=3, bd=5, relief='ridge',
                         command=funcenter).pack()
main_screen.mainloop()

# sources: "Curso em video - Udemy (portuguese Brazil)", "Python docummentation", "Tkinter docummentation"
