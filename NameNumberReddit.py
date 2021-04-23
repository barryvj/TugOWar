from tkinter import *

def write_File (name_File, number_File): #Allows for both Team Name and Number to be passed through this write function
	file = open("TugofWar.txt", "a") # "a" restricts the function to only append to the file
	Name = name_File.get() #These two commands get the team name and number entries
	Number = number_File.get()
#	file.write('Game #: ' + Game_Count)
	file.write('Team Name: ' + Name)
	file.write('    Team Number:  ' + Number + '\n') #\n for Next Line
	file.close()
	print(Name + '   ' + Number)

root = Tk()

#In a home screen, need to initialize Game_Count = 0 so it is a defined variable
# Game_Count = Game_Count + 1

#Import Blank Screen
NameNum_Screen = PhotoImage(file='NameNumberReddit.gif')

#Create a canvas so New_Game can be overlayed on image
canvas = Canvas(root, width=1600, height=1200)
canvas.pack()
canvas.create_image(800, 800, anchor='s', image=NameNum_Screen)



# The text color is referenced by HEX Code #F57A13. This is very close to the company theme orange.
name_text = Label(root, text="Enter Team Name:", fg="#F57A13", bg="black", font=('Arial', 24))
name_prompt = canvas.create_window(500, 400, window=name_text)

team_name = StringVar() # In order to be able to retrieve the current text from the entry widget, 
						# must set this option to an instance of the StringVar class
name_entry = Entry(root, textvariable=team_name, bg="white", font= ('Arial', 24))
team_name_window = canvas.create_window(950, 400, window=name_entry)  

number_text = Label(root, text="Enter Team Number:", fg="#F57A13", bg="black", font=('Arial', 24))
number_prompt = canvas.create_window(500, 550, window=number_text)  

team_number = StringVar()
number_entry = Entry(root, textvariable=team_number, bg="white", font= ('Arial', 24))
team_number_window = canvas.create_window(950, 550, window=number_entry)  

Next_Save_btn = Button(root, text = "Next =>", command = lambda: write_File(name_entry, number_entry),	
				fg="#F57A13", bg="black", font=('Arial', 24), border=10) 
# the name and number entries are passed through the write_File function and saved in TugofWar.txt
Next_Save_btn = canvas.create_window(1100, 700, window=Next_Save_btn)  #how does the window=Next_Save_btn work????


#after saving we need to move to the "Tug of War Directions" page


root.mainloop()