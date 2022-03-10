#Made by: Nipun Bhatnagar and Corey Warden - Timberland High School

#Importing all modules and libraries required to run the program.
#tkinter used to display information on a graphical user interface(GUI).
import tkinter as tk
from tkinter import HORIZONTAL, ttk
from tkinter.constants import CENTER, END
#PILLOW is used in order to convert images into buttons in the GUI.
from PIL import Image, ImageTk
#Requests and BeautifulSoup4 allow to web scrape websites for information on locations and type of locations.
import requests
from bs4 import BeautifulSoup


#Setting up the tkinter environment
root = tk.Tk()
#Making the tkinter window fullscreen
root.attributes('-fullscreen', True)
#Naming the window
root.title("Tourist_Guide")
#Setting the background color to white
root.configure(background='#ffffff')


#These two lists will hold information on all the attractions at a specific location.
attractions = []
attractiontype = []


#Function that closes the GUI.
def quit_gui():
    root.destroy()

#Function that closes the current page and then opens the next page
def nextPage():
    root.destroy()
    import page2

#This function updates that progress bar. As BeautifulSoup scrapes the website for data, the progress bar updates when every new attraction or attraction type is found.
#It updates by 0.5 because the full bar is 100, and there are 100 attractions and 100 attraction types.
def step():
    loading_Bar['value'] += 0.5
    root.update_idletasks()

#This function exits fullscreen
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)


#This is the main function that finds all the attractions and attraction types. It runs when the submit button is pressed on the main screen(page1)
def getstudentname():

    #This if statement checks if the entry bar was left blank when hitting the submit button.
    #If it's not it continues, if it is, then it does nothing.
    if name_entry.get().replace(" ", "") != "EnterCity" and name_entry.get().replace(" ", "") != "":

        #When the submit button is pressed the loading bar is places on the screen.
        loading_Bar.place(relx= .5, rely=.665, anchor=CENTER)

        #This grabs the value of the entry bar and sets it equal to the variable location
        location = name_entry.get()

        #These statements replace the normal formatting of a location into how it would be formatted in a website url. 
        #Specifically for the website Tripbuzz, where we are web scraping from.
        if ". " in location:
            location = location.replace(". ", "-")
        if " " in location:
            location = location.replace(" ", "-")

        #This concatenates the full url with the specific location that the user entered.
        URL = "http://www.tripbuzz.com/things-to-do/"+location+"-mo"

        #These lines set up the url to be used and parsed by BeautifulSoup
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')

        #This for loop checks every webelement that is used for attraction titles on the first page and adds them to the attraction list.
        for i in soup.find_all("h3", {'itemprop': 'name'}, "a"):

            #This if statement checks if the web element is an ad. Ads contain blank space in their title name.
            if "\n\n" in i.text:
                    pass

            #If the webelement title is not an ad, it adds the text element of the webelement(the name of the attraction) to the attraction list.
            else:
                attractions.append(i.text)
                #If the program appends a new item to the list, it tells the progress bar to step or update
                step()


        #This while loop does the same thing as the for loop above, however, it moves to the next page on the website.
        #This x variable is set to 2 because it is added to the url for the second page
        x=2

        #This while loop runs 9 times, for pages 2-10. Page 1 was already scraped in the code above.
        while x < 11:
            root.update() 
            URL = "http://www.tripbuzz.com/things-to-do/"+location+"-mo/page-"+str(x)
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            for i in soup.find_all("h3", {'itemprop': 'name'}, "a"):
                if "\n\n" in i.text:
                    pass
                else:
                    attractions.append(i.text)
                    step()
            x+=1


        #The following loops do the same thing as the for loop and while loop above, however, this time looking for a different webelement which tells us the type of attraction.
        #All of these types are added to a list.
        #If no attractions were found previously, it will not look for types since it would waste time.
        if len(attractions) != 0:
            URL = "http://www.tripbuzz.com/things-to-do/"+location+"-mo"
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            for i in soup.find_all("span", {'class': 'text-blue'}):
                if "\n" in i.text:
                        pass
                else:
                    attractiontype.append(i.text)
                    step()


            x = 2
            while x < 11:
                root.update() 
                URL = "http://www.tripbuzz.com/things-to-do/"+location+"-mo/page-"+str(x)
                r = requests.get(URL)
                soup = BeautifulSoup(r.content, 'html5lib')
                for i in soup.find_all("span", {'class': 'text-blue'}):
                    if "\n" in i.text:
                        pass
                    else:
                        attractiontype.append(i.text)
                        step()
                
                x+=1


        #If the function found attractions, the program will move on to the next page, if not, the program will do nothing
        if len(attractions) != 0:
            nextPage()
        else:
            pass
    



#This opens the background image and displays it on the screen
image_label = Image.open("mainBackground.png")
test = ImageTk.PhotoImage(image_label)
label_img = tk.Label(root, image=test, bg = '#ffffff')
label_img.image = test
#This places the image at a specific point on the screen and anchors it to the middle of the screen
label_img.place(relx=0.5, rely=0.37, anchor=CENTER)


#This configures and places a entry bar for the user to enter a location
name_entry = tk.Entry(root, width=40, borderwidth=0, font = "Helvetica 18 bold")
#This sets up the initial value of the entry bar that shows up inside the entry bar
name_entry.insert(END, "Enter City")
name_entry.place(relx=0.5, rely=0.52,height= 38, anchor=CENTER)


#This segment of code opens the image of the submit button, sets it to the appropriate size, and then binds it to the command getstudentname.
img= (Image.open("submit.png"))
resized_image= img.resize((150,42), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
Submit = tk.Button(root, text="Submit", command=getstudentname, borderwidth=0)
Submit.config(image=new_image)
Submit.place(relx=0.5, rely=0.57, anchor=CENTER)


#This segment of code opens the image of the exit button, sets it to the appropriate size, and then binds it to the command quit_gui.
img2= (Image.open("EXIT.png"))
resized_image2= img2.resize((150,42), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)
Close = tk.Button(root, text="Close", command=quit_gui, borderwidth=0)
Close.config(image=new_image2)
Close.place(relx=0.5, rely=0.62, anchor=CENTER)

#This sets up the progress bar with the appropriate length.
loading_Bar = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')


#This binds the escape key to a function that exits fullscreen mode
root.bind("<Escape>", exit_fullscreen)

#This allows the GUI to continuously update.
root.mainloop()

#This allows the root to destroy when switching to a new page
root.destroy()
