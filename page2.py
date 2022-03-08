#Made by: Nipun Bhatnagar, Corey Warden, and Ivan Ou Yang - Timberland High School

#Importing all modules and libraries required to run the program.
#tkinter used to display information on a graphical user interface(GUI).
import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER
from PIL import Image, ImageTk

#This imports variables from the previous page that need to be used in this file.
from page1 import attractiontype


#Sets up the tkinter environment
root2 = tk.Tk()
#setting tkinter window size, name, and background color.
root2.attributes('-fullscreen', True)
root2.title("Tourist_Guide")
root2.configure(background='white')

attractiontype_dropdown = attractiontype
#This removes repeats in the type of attraction because there could be multiple attractions of the same type
dropdownList = (set(attractiontype))
dropdownList = list(dict.fromkeys(dropdownList))
#This sorts the list in alphabetical order so when they display, it's easier for the user to find.
dropdownList = sorted(dropdownList)



#This function gets the value in the dropdown menu and then destroys the current page and moves on to the next page
#However, if the dropdown menu is empty(the user didn't select anything) it doesn't do anything
def next_page():
    global typeSelection
    if combo.get() != "":
        typeSelection = combo.get()
        root2.destroy()
        import page3
    else:
        pass
    
    
#This function exits fullscreen
def exit_fullscreen(event):
    root2.attributes('-fullscreen', False)


#This function is used to close the current window
def quit_gui():
    root2.destroy()



#This sets up the background image for the screen and place it on the screen
image_label = Image.open("gradient.png")
test = ImageTk.PhotoImage(image_label)
label_img = tk.Label(root2, image=test, bg = '#ffffff')
label_img.place(relx=0.5, rely=0.5, anchor=CENTER)

#This sets up the dropdown menu and then places it on the screen.
#The options of the menu and from "mylist"
combo = ttk.Combobox(root2, width=50, font="Chivo 16 bold", state="readonly")
combo['values'] = (dropdownList)
combo.place(relx=.5, rely=.5, anchor=CENTER)


#This segment of code opens the image of the submit button, sets it to the appropriate size, and then binds it to the command next_page.
img= (Image.open("submit.png"))
resized_image= img.resize((150,42), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
Submit = tk.Button(root2, text="Submit", command=next_page, borderwidth=0)
Submit.config(image=new_image)
Submit.place(relx=0.5, rely=0.57, anchor=CENTER)


#This segment of code opens the image of the exit button, sets it to the appropriate size, and then binds it to the command quit_gui.
img2= (Image.open("EXIT.png"))
resized_image2= img2.resize((150,42), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)
Close = tk.Button(root2, text="Close", command=quit_gui, borderwidth=0)
Close.config(image=new_image2)
Close.place(relx=0.5, rely=0.62, anchor=CENTER)


#This binds the escape key to the function exit_fullscreen
root2.bind("<Escape>", exit_fullscreen)

#This allows the GUI to continuously update.
root2.mainloop()

