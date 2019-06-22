from tkinter import *
from tkinter import filedialog
file_name = None            #making variable for for creating file
def donothing():            #making dummy function just for no work
    tp = Toplevel(main_obj)
    bt = Button(text="Time pass")
    bt.pack()
def new_file():
    global file_name
    file_name = "Untitled"  #default file
    Text.delete(0.0, END)   #because of this the user can type text on that blank space
def save_file():
    global file_name
    t = Text.get(0.0, END)      #0.0 means row=0 column=0
    file = open(file_name,'w')  #creating file
    file.write()
    file.close()
def saveAs():
    f = filedialog.asksavefilename(mode='w', defaultextention='.txt')   #tkfiledialog change ho k filedialog hogaya
    t = Text.get(0.0, END)
    try:
        f.write(t.rstrip())     #strip is used to cut off the white space under the text we write into the file
    except:
        print("error")
def open_file():
    f = filedialog.askopenfilename(mode='r')
    f.read()
    Text.delete(0.0, END)
    Text.insert(0.0, END)
main_obj = Tk()
main_obj.title("*****CLAY Text Editor*****")
text = Text(width=40,height=20)
text.pack()
menubar = Menu(main_obj)                                             #creating the main menubar object
file_menu1 = Menu(menubar)                                           #creating the object for the first file menu bar
file_menu1.add_command(label="Open",command=open_file)               #giving the menu option functionality
file_menu1.add_command(label="New",command=new_file)
file_menu1.add_command(label="Save",command=save_file)
file_menu1.add_command(label="Save As",command=saveAs)
menubar.add_cascade(label="File",menu=file_menu1)       #giving the menu title and cascading it

file_menu2 = Menu(menubar)                                  #creating the object for the second file menu
file_menu2.add_command(label="Encrypt",command=donothing)
file_menu2.add_command(label="Decrypt",command=donothing)
menubar.add_cascade(label="Features",menu=file_menu2)

file_menu3 = Menu(menubar)
file_menu3.add_command(label="Count letter",command=donothing)
file_menu3.add_command(label="Count Words",command=donothing)
file_menu3.add_command(label="Count Vowels",command=donothing)
file_menu3.add_command(label="Count Article",command=donothing)
menubar.add_cascade(label="Function",menu=file_menu3)

main_obj.config(menu=menubar)           #configuration for menu ***important****
main_obj.mainloop()                     #running the mainloop ***infinite****
