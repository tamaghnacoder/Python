from tkinter import *
root=Tk()
root.title("Fibonacci")
root.geometry("400x400")

label_series=Label(root, text="Fibonacci series:  ")
label_flower=Label(root)
label_spiral=Label(root)

def Fibonacci():
    num=10
    num1=0
    num2=0
    sum=0
    counter=1
    while (counter<=num):
        label_series["text"]+=str(sum)+" "
        counter=counter+1
        num1=num2
        num2=sum
    label_flower["text"]="Flower is fully bloomed"
    label_spiral["text"]="Spirals in right direction are" + str(num1) + " and spirals in left direction are " + str(num2) + "\n. Total spirals are " + str(sum)
     
btn=Button(root, text="Show Fibonacci Series", command=Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()