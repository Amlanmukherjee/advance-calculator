"""
*******************************************************************************************
PROJECT : ADVANCED CALCULATOR
AUTHOR NAME : AMLAN MUKHERJEE
*******************************************************************************************
"""

from tkinter import *
import math


class calculator:

    def __init__(self):

        self.root=Tk()

        self.root.title("AMLAN's CALCULATOR")

        self.var = IntVar()

        self.result = Label(self.root, text="0", width="6", height="3",font=30, bg="white", anchor=E)

        self.result.grid(row=0,column=0, columnspan=7,sticky=W+E,pady=1)

        self.result1 = Label(self.root, text="", width="6", height="2", bg="grey94")

        self.result1.grid(row=1, column=0)

        self.result2 = Label(self.root, text="", width="6", height="2", bg="grey94")

        self.result2.grid(row=1, column=1)

        self.result3 = Label(self.root, text="", width="6", height="2", bg="grey94")

        self.result3.grid(row=1, column=2)

        self.note = Label(self.root, text="""#NOTE : for using functions like 'sin,log,...etc' first give a input
like 'eg-45,57.24 ...etc' then directly press on the function of 
your choice to get the result.""" , bg = "white")

        self.note.grid(row=6,column=0, columnspan=7,sticky=W+E)

        self.btn1 = Button(self.root, text="1",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("1")).grid(

            row=4, column=3)

        self.btn2 = Button(self.root, text="2",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("2")).grid(row=4,

                                                                                                             column=4)

        self.btn3 = Button(self.root, text="3",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("3")).grid(row=4,

                                                                                                             column=5)

        self.btnadd = Button(self.root, text="+",border=0,  width="6", height="3", bg="DeepSkyBlue3", command=lambda: self.operator("+")).grid(row=5, column=6)



        self.btn4 = Button(self.root, text="4",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("4")).grid(row=3,

                                                                                                             column=3)

        self.btn5 = Button(self.root, text="5",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("5")).grid(row=3,

                                                                                                             column=4)

        self.btn6 = Button(self.root, text="6",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("6")).grid(row=3,

                                                                                                             column=5)

        self.btnsub = Button(self.root, text="-",border=0,  width="6", height="3", bg="DeepSkyBlue3", command=lambda: self.operator("-")).grid(row=4, column=6)



        self.btn7 = Button(self.root, text="7",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("7")).grid(row=2,

                                                                                                             column=3)

        self.btn8 = Button(self.root, text="8",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("8")).grid(row=2,

                                                                                                             column=4)

        self.btn9 = Button(self.root, text="9",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("9")).grid(row=2,

                                                                                                             column=5)

        self.btnmul = Button(self.root, text="x",border=0,  width="6", height="3", bg="DeepSkyBlue3", command=lambda: self.operator("*")).grid(row=3, column=6)



        self.btn0 = Button(self.root, text="0",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.print_num("0")).grid(row=5,

                                                                                                             column=4)

        self.btndiv = Button(self.root, text="/",border=0,  width="6", height="3", bg="DeepSkyBlue3", command=lambda: self.operator("/")).grid(row=2, column=6)



        self.btnClr = Button(self.root, text="AC",border=0,  width="6", height="3", bg="DeepSkyBlue3", command=lambda: self.clear()).grid(row=1, column=6)



        self.btnEquals = Button(self.root, text="=",border=0,  width="6", height="3", bg="SteelBlue1", command=lambda: self.publish()).grid(row=5, column=5)



        self.btndecimal = Button(self.root, text=".",border=0,  width="6", height="3", bg="SteelBlue1",command=lambda: self.print_num(".")).grid(row=5, column=3)



        self.btnpercent = Button(self.root, text="%",border=0,  width="6", height="3", bg="DeepSkyBlue3",command=lambda: self.publish2("%")).grid(row=1, column=5)

        self.R1 = Radiobutton(self.root, text="deg", variable=self.var,border=0, value=1)
        self.R1.grid( row=1, column=3)

        self.R2 = Radiobutton(self.root, text="rad", variable=self.var,border=0, value=2)
        self.R2.grid( row=1, column=4)

        self.btnln = Button(self.root, text="ln",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish2("ln")).grid(row=2, column=0)



        self.btnlog = Button(self.root, text="log",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish2("log")).grid(row=2, column=1)



        self.btnfac = Button(self.root, text="x!",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish2("x!")).grid(row=2, column=2)



        self.btnsin = Button(self.root, text="sin",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish2("sin")).grid(row=3, column=0)



        self.btncos = Button(self.root, text="cos",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish2("cos")).grid(row=3, column=1)



        self.btntan = Button(self.root, text="tan",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish2("tan")).grid(row=3, column=2)



        self.btne = Button(self.root, text="e",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish3("e")).grid(row=4, column=0)



        self.btnpi = Button(self.root, text="π",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish3("pi")).grid(row=4, column=1)



        self.btnexp = Button(self.root, text="EXP",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish2("EXP")).grid(row=4, column=2)



        self.btnsqrt = Button(self.root, text="√",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish2("sqrt")).grid(row=5, column=0)



        self.btnsq = Button(self.root, text="sq",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.publish2("sq")).grid(row=5, column=1)



        self.btnpow = Button(self.root, text="^",border=0,  width="6", height="3", bg="DeepSkyBlue3",
                             command=lambda: self.operator("^")).grid(row=5, column=2)



        self.root.mainloop()



    def print_num(self,num):

        new_text=self.result['text'] + num

        self.result.configure(text=new_text)



    def clear(self):

        self.result.configure(text="")
        self.result1.configure(text="")
        self.result2.configure(text="")
        self.result3.configure(text="")


    def operator(self,sign):

        self.operator_name=sign

        self.first_num=float(self.result['text'])

        self.result.configure(text="")



    def publish(self):

        self.second_num=float(self.result['text'])

        if self.operator_name=="+":

            self.result.configure(text=str(self.first_num+self.second_num))

            self.result1.configure(text=str(self.first_num))
            self.result2.configure(text=str(self.operator_name))
            self.result3.configure(text=str(self.second_num))

        elif self.operator_name=="-":

            self.result.configure(text=str(self.first_num-self.second_num))

            self.result1.configure(text=str(self.first_num))
            self.result2.configure(text=str(self.operator_name))
            self.result3.configure(text=str(self.second_num))


        elif self.operator_name=="*":

            self.result.configure(text=str(self.first_num*self.second_num))

            self.result1.configure(text=str(self.first_num))
            self.result2.configure(text="x")
            self.result3.configure(text=str(self.second_num))


        elif self.operator_name == "^":

            self.result.configure(text=str(math.pow(self.first_num,self.second_num)))

            self.result1.configure(text=str(self.first_num))
            self.result2.configure(text=str(self.operator_name))
            self.result3.configure(text=str(self.second_num))


        elif self.operator_name == "/":

            try:
                self.result.configure(text=str(self.first_num/self.second_num))

                self.result1.configure(text=str(self.first_num))
                self.result2.configure(text=str(self.operator_name))
                self.result3.configure(text=str(self.second_num))
            except ZeroDivisionError:
                self.result.configure(text="ERROR")


    def publish2(self,sign1):

        self.operator_name1 = sign1

        self.first_num1 = float(self.result['text'])

        self.result.configure(text="")

        if self.operator_name1=="x!":

            self.result.configure(text=str(math.factorial(self.first_num1)))
            self.result1.configure(text=str(self.first_num1))
            self.result2.configure(text="!")

        elif self.operator_name1=="ln":
            try:
                self.result.configure(text=str(math.log(self.first_num1,math.e)))
                self.result2.configure(text=str(self.first_num1))
                self.result1.configure(text="ln")
            except ValueError:
                self.result.configure(text="ERROR")

        elif self.operator_name1=="log":
            try:
                self.result.configure(text=str(math.log10(self.first_num1)))
                self.result2.configure(text=str(self.first_num1))
                self.result1.configure(text="log")
            except ValueError:
                self.result.configure(text="ERROR")

        elif self.operator_name1=="sin":
            if str(self.var.get()) == "1":
                self.result.configure(text=str(round(math.sin(math.radians(self.first_num1)),7)))
                self.result2.configure(text=str(self.first_num1))
                self.result1.configure(text="sin")

            else:
                self.result.configure(text=str(round(math.sin(self.first_num1),7)))
                self.result2.configure(text=str(self.first_num1))
                self.result1.configure(text="sin")


        elif self.operator_name1=="cos":
            if str(self.var.get()) == "1":
                self.result.configure(text=str(round(math.cos(math.radians(self.first_num1)),7)))
                self.result2.configure(text=str(self.first_num1))
                self.result1.configure(text="cos")
            else:
                self.result.configure(text=str(round(math.cos(self.first_num1),7)))
                self.result2.configure(text=str(self.first_num1))
                self.result1.configure(text="cos")

        elif self.operator_name1=="tan":
            if str(self.var.get()) == "1":
                self.result.configure(text=str(round(math.tan(math.radians(self.first_num1)),7)))
                self.result2.configure(text=str(self.first_num1))
                self.result1.configure(text="tan")
            else:
                self.result.configure(text=str(round(math.tan(self.first_num1),7)))
                self.result2.configure(text=str(self.first_num1))
                self.result1.configure(text="tan")

        elif self.operator_name1 == "EXP":
            self.result.configure(text=str(math.exp(self.first_num1)))
            self.result1.configure(text="e^")
            self.result2.configure(text=str(self.first_num1))

        elif self.operator_name1 == "%":
            self.result.configure(text=str(self.first_num1/100))
            self.result1.configure(text=str(self.first_num1))
            self.result2.configure(text="/ 100")

        elif self.operator_name1 == "sqrt":
            self.result.configure(text=str(math.sqrt(self.first_num1)))
            self.result1.configure(text="√")
            self.result2.configure(text=str(self.first_num1))

        elif self.operator_name1 == "sq":
            self.result.configure(text=str(math.pow(self.first_num1,2)))
            self.result2.configure(text="^2")
            self.result1.configure(text=str(self.first_num1))
        else:
            self.result.configure(text="ERROR")


    def publish3(self,sign3):

        self.operator_name3=sign3

        if self.operator_name3 == "pi":
            self.result.configure(text=str(round(math.pi,6)))
            self.result1.configure(text="π")

        elif self.operator_name3 == "e":
            self.result.configure(text=str(round(math.e,6)))
            self.result1.configure(text="e")



obj1=calculator()