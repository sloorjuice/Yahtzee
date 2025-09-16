import tkinter as tk
 
window = tk.Tk()
 
#CODE GO HERE
 
def print_hello(argument = None):
    print(f"HI, :3 {argument}")
 
my_label = tk.Label(window, text = "\nGUI Label\n                                                                                                                                     ", bg = "blanched almond")
my_label.pack()
 
check1variable = tk.IntVar()
check2variable = tk.IntVar()
check3variable = tk.IntVar()
 
my_button1 = tk.Button(window, text="Pay 100 pounds here", bg="red", command=lambda:print_hello(1))
my_button1.pack()
my_button2 = tk.Button(window, text="Pay 100 pounds here", bg="red", command=lambda:print_hello(2))
my_button2.pack()
 
check_button1 = tk.Checkbutton(window, text="option1", onvalue=1,offvalue=0,variable = check1variable)
check_button1.pack()
check_button2 = tk.Checkbutton(window, text="option2", onvalue=1,offvalue=0,variable = check2variable)
check_button2.pack()
check_button3 = tk.Checkbutton(window, text="option3", onvalue=1,offvalue=0,variable = check3variable)
check_button3.pack()
 
space = tk.Text(window)
 
 
def on_submit():
    print(check1variable.get())
    print(check2variable.get())
    print(check3variable.get())
 
space.pack()
 
submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.pack()
window.mainloop()