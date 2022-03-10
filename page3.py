#Made by: Nipun Bhatnagar and Corey Warden - Timberland High School
 
#Importing all modules and libraries required to run the program.
#tkinter used to display information on a graphical user interface(GUI).
import tkinter as tk
from tkinter.constants import CENTER
from PIL import Image, ImageTk

#This imports variables from the previous pages that need to be used in this file.
from page2 import typeSelection, attractiontype_dropdown
from page1 import attractions

#This makes a empty list that will fill up with the attractions based on the users selections
result_Page3 = []

#setting tkinter window size
root3 = tk.Tk()
root3.attributes('-fullscreen', True)
root3.title("Tourist_Guide")
root3.configure(background='white')


#This function exits fullscreen
def exit_fullscreen(event):
    root3.attributes('-fullscreen', False)

#Function that closes the GUI.
def quit_gui():
    root3.destroy()


#This sets up the background image for the screen and place it on the screen
image_label = Image.open("gradient2.png")
test = ImageTk.PhotoImage(image_label)
label_img = tk.Label(root3, image=test, bg = '#ffffff')
label_img.place(relx=0.5, rely=0.5, anchor=CENTER)


#This loop runs through the type of attractions(including repeats) and matches the index of them to the name of the attraction
#Then, it adds them to the list of attractions if the attraction type is the same as the users selection
loop_count = 0
for i in attractiontype_dropdown:
    if i == typeSelection:
        result_Page3.append(attractions[loop_count])
    loop_count+=1


#This loop goes through all the attractions in the result_Pag3 list and makes the labels to display on the page
#It also evenly spaces all the attractions for a neat and professional look
loop_count2 = 0
for i in result_Page3:
    labelLocation = tk.Label(root3, text=i, font=('Chivo', 15), bg='#70DEF1')
    labelLocation.place(relx=0.5, rely=((0.2)+(loop_count2/20)), anchor=CENTER)
    loop_count2+=1



#This segment of code opens the image of the exit button, sets it to the appropriate size, and then binds it to the command quit_gui.
img= (Image.open("EXIT.png"))
resized_image= img.resize((150,42), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
Close = tk.Button(root3, text="Close", command=quit_gui, borderwidth=0)
Close.config(image=new_image)
Close.place(relx=0.5, rely=0.9, anchor=CENTER)



#This binds the escape key to a function that exits fullscreen mode
root3.bind("<Escape>", exit_fullscreen)

#This allows the GUI to continuously update
root3.mainloop()
