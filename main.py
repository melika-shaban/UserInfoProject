################################################################################
#IGNORE THIS STUFF AND SCROLL DOWN TO LINE 80 TO SEE THE ASSIGNMENT DESCRIPTION#
################################################################################
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

radioButtonYloc = 50
radioButtonXloc = 15
spacingY = 40
fontColour = 'white'        
bgColour = 'dark slate grey'
fontType = 'calibri'
fontSize = 11
LabelFontSize = 13
LabelFontType = 'Calibri Bold'
fNameBoxLocX = 180
lNameBoxLocX = 330
ageBoxLocX = 480
infoBoxesY = radioButtonYloc + spacingY*5 + 5
infoLabelsY = radioButtonYloc + int(spacingY*4.4)
addDelSearchButtonY = y=radioButtonYloc + spacingY*5 + 5

window = tk.Tk()
window.title("User Info Assignment")
window.geometry("600x300")
window['background']=bgColour

sortOption = tk.IntVar(window, value = 0)

textFrame = tk.Frame (window, height = 250, width = 350)
textFrame.place(x=180, y=radioButtonYloc -spacingY)

scroller=tk.Scrollbar(textFrame, orient='vertical')
scroller.pack(side=tk.RIGHT, fill = 'y')

textBox = tk.Text(textFrame, height=13, width=56, wrap='word')
textBox.pack()
#text_box.place(x=180, y=radioButtonYloc -spacingY)
textBox.config(yscrollcommand=scroller.set)
scroller.config(command=textBox.yview)


######## STUFF FOR ADD, DELETE, AND SEARCH USER EXTENSIONS ########
fNameBox = tk.Text(window, height=2, width=20, wrap='word')
fNameBox.place(x=fNameBoxLocX, y=infoBoxesY)

lNameBox = tk.Text(window, height=2, width=20, wrap='word')
lNameBox.place(x=lNameBoxLocX, y=infoBoxesY)

ageBox = tk.Text(window, height=2, width=7, wrap='word')
ageBox.place(x=ageBoxLocX, y=infoBoxesY)

fnameHeading = tk.Label(text="First Name", background=bgColour, fg = fontColour, font=(LabelFontType, LabelFontSize))
fnameHeading.place(x = fNameBoxLocX, y = infoLabelsY)

lnameHeading = tk.Label(text="Last Name", background=bgColour, fg = fontColour, font=(LabelFontType, LabelFontSize))
lnameHeading.place(x = lNameBoxLocX, y = infoLabelsY)

ageHeading = tk.Label(text="Age", background=bgColour, fg = fontColour, font=(LabelFontType, LabelFontSize))
ageHeading.place(x = ageBoxLocX, y = infoLabelsY)



def convert(val):
  if val == 0:
    return "first name"

  elif val == 1:
    return "last name"

  else:
    return "age"

searchButtonImage = Image.open("images/search button.png")
searchButtonImage = ImageTk.PhotoImage(searchButtonImage.resize((34, 34)))



#################################################################
#################################################################
################### ASSIGNMENT DESCRIPTION ######################
#################################################################
#                                                               #
#!!!!   READ ASSIGNMENT DESCRIPTION AND EXAMPLE CAREFULLY   !!!!#
#                                                               #
#################################################################
#click run and have a look at the user interface. Notice the 3 checkboxes and the button that says "Get User Info"

#This program is not finished. When "Get User Info" is clicked, the program should display some user info in the textbox on the right

#To finish this program, you need to finish the SortUsers function (below), 
#SortUsers must read in the user info from the "user info.txt" file and update the string "userInfo" so that it is a string of all of the users separated by the new line character
#each line should be written in the format: firstName lastName, age
#userInfo should be sorted by first name, last name, or age depending on which checkbox is selected in the user interface.


#################### EXAMPLE #########################
#the user info.txt file stores a bunch of user info. 
#Have a look at the file and see how it is formatted

#pretend, for this example, that the user info.txt file contains: 
#Adam, Camp, 20
#Bryan, Baker, 40
#Chelsea, Austin, 30

#if Get User Info is clicked then...
#If sort by first name is selected "userInfo" would need to be assigned the value...
#"Adam Camp, 20\nBryan Baker, 40\nChelsea Austin, 30"

#If sort by last name is selected then "userInfo" would need to be...
#"Chelsea Austin, 30\nBryan Baker, 40\nAdam Camp, 20"

#If sort by age is selcted then "userInfo" would need to be...
#"Adam Camp, 20\nChelsea Austin, 30\nBryan Baker, 40"

#recall that \n is the newline character so the string "Adam Camp, 20\nChelsea Austin, 30\nBryan Baker, 40" would actually look like:
#Adam Camp, 20
#Chelsea Austin, 30
#Bryan Baker, 40


#Additional Functionality to Complete
#in this assignment there are 3 other functions to complete. These are the AddUser, DelUser and SearchUser functions can also be completed. Scroll down to find them (they are located just below the SortUsers functio, which is also below)

#feel free to play around/explore and make this your own. You can change the file to display different info, experiment to change up the user interface etc.
#############################


def opener():
  global info
  with open("images/user info.txt", "r") as names_and_age:
    info = names_and_age.readlines()
  index_counter = 0
  for items in info:
    info[index_counter] = info[index_counter].split(',')
    index_counter += 1 


class people:
  def __init__(self, this_is_a_list):
    self.firstname = this_is_a_list[0].strip()
    self.lastname = this_is_a_list[1].strip()
    self.age = this_is_a_list[2].strip()


def a_to_z():
  global another_list
  opener()
  list = info
  holder = list.copy() 
  another_list = [] 
  for i in range(0,len(holder)):
    y = holder[0]
    t = 0
    while t < len(holder):
      if y > holder[t]: 
        y = holder[t] 
      t += 1
    index_of_highest_integer = holder.index(y)
    holder.pop(index_of_highest_integer)
    another_list.append(y)
    if len(holder) == 0:
      break
  return another_list

def last_name_a_to_z(list):
  global last_name_list
  opener()
  list = info
  holder = list.copy() 
  last_name_list = [] 
  for i in range(0,len(holder)):
    y = holder[0]
    t = 0
    while t < len(holder):
      if y[1] > holder[t][1]: 
        y = holder[t] 
      t += 1
    index_of_highest_integer = holder.index(y)
    holder.pop(index_of_highest_integer)
    last_name_list.append(y)
    if len(holder) == 0:
      break
  return last_name_list

def age_small_to_large(list):
  global age_list
  opener()
  list = info
  holder = list.copy() 
  age_list = [] 
  for i in range(0,len(holder)):
    y = holder[0]
    t = 0
    while t < len(holder):
      mm = y[2].strip('\n')
      nn = holder[t][2].strip('\n')
      if int(mm) > int(nn): 
        y = holder[t] 
      t += 1
    index_of_highest_integer = holder.index(y)
    holder.pop(index_of_highest_integer)
    age_list.append(y)
    if len(holder) == 0:
      break
  return age_list




#SortUsers will be called whenever the "Get User Info" button is clicked. This functionality is already built into the program.
def SortUsers():
  global sortOption
  global textBox

  #sortBy is one of: "first name", "last name" or "age"
  #its value depends on which checkbox is selected
  sortBy = convert(sortOption.get())

  #the string you need to update
  userInfo = "You need to update \"userInfo\" with the sorted user info"
  
  ###################### YOUR CODE GOES HERE ###########################
  #all you need to do is read the user info in from the user info file, sort it according to first name, last name, or age, then consolidate it into to a single string and assign that string to the userInfo variable. The existing code will do the rest
  
  #if the first name checkbox is selected...
  if sortBy == "first name":
    a_to_z()
    A = ""
    index_counter = 0
    for items in another_list:
      x = people(another_list[index_counter])
      index_counter += 1
      hello = ""
      hello = x.firstname + " " + x.lastname + ", " + x.age + "\n"
      A = A + hello
    userInfo = A

  #if the last name checkbox is selected...
  elif sortBy == "last name":
    last_name_a_to_z(info)
    A = ""
    index_counter = 0
    for items in last_name_list:
      x = people(last_name_list[index_counter])
      index_counter += 1
      hello = ""
      hello = x.firstname + " " + x.lastname + ", " + x.age + "\n"
      A = A + hello
    userInfo = A



  #if the age checkbox is selected...
  elif sortBy == "age":
    age_small_to_large(info)
    A = ""
    index_counter = 0
    for items in age_list:
      x = people(age_list[index_counter])
      index_counter += 1
      hello = ""
      hello = x.firstname + " " + x.lastname + ", " + x.age + "\n"
      A = A + hello
    userInfo = A




  else:
    userInfo = "something went terribly wrong"
    

  

  ######################### YOUR CODE ENDS HERE ##########################
  
  textBox.delete('1.0', tk.END)
  textBox.insert('1.0', userInfo)






  
#######################################################################
######## UNCOMMENT FOR ADD, DELETE, AND SEARCH USER EXTENSIONS ########
#######################################################################
def AddUser():
  global fNameBox
  global lNameBox
  global ageBox
  global textBox  
  FName = fNameBox.get('1.0', 'end-1c')
  LName = lNameBox.get('1.0', 'end-1c')
  age = ageBox.get('1.0', 'end-1c')
  userInfo = textBox.get('1.0', 'end-1c')
  text_for_file = FName + ", " + LName + ", " + age
  with open("images/user info.txt", "r") as reading_file:
    names = reading_file.readlines()
  bool_value = True
  for info in names:
    if text_for_file == info:
      bool_value = False
  if FName.isspace() == True or FName == "" or LName.isspace() == True or LName == "" or age.isspace() == True or age == "":
    bool_value = False
  if bool_value:
    with open("images/user info.txt", "a") as adding_user:
      adding_user.write("\n" + text_for_file)
    userInfo = ""
  if not bool_value:
    userInfo = "This information is already stored, or it is not a valid input."

  ########### YOUR CODE GOES HERE ##########
  #you will need to update the contents of the file so that a new user is added with the first name, last name and age that are in the First Name Last Name and Age text boxes in the GUI. You can access that text from the following strings:
  #FName contains the text in the First Name box
  #LName contains the text in the Last Name box
  #age contains the text in the Age box
#make sure to check if a person with the exact same first name, last name and age already exists and if so don't add. Also, don't add if one of the boxes is empty. Display an appropriate error message if the user couldn't be added. Recall that userInfo stores the text that goes in the main display box. Alternatively, you can print it to the console.



  ##########################################
  
  textBox.delete('1.0', tk.END)
  textBox.insert('1.0', userInfo)


def DelUser():
  global fNameBox
  global lNameBox
  global ageBox
  global textBox
  FName = fNameBox.get('1.0', 'end-1c')
  LName = lNameBox.get('1.0', 'end-1c')
  age = ageBox.get('1.0', 'end-1c')
  userInfo = textBox.get('1.0', 'end-1c')
  text_for_file = FName + ", " + LName + ", " + age
  with open("images/user info.txt", "r") as reading_file:
    names = reading_file.readlines()
  bool_value = True
  another_bool = False
  for info in names:
    if text_for_file == info:
      another_bool = True
  if not another_bool:
    bool_value = False
  if FName.isspace() == True or FName == "" or LName.isspace() == True or LName == "" or age.isspace() == True or age == "":
    bool_value = False
  for information in names:
    if information.strip('\n')== text_for_file:
      index_holder = names.index(information)
      names.pop(index_holder)
  with open("images/user info.txt", "w") as writing_file:
    for items in names:
      if items != names[0]:
        writing_file.write("\n" + items.strip('\n'))
      else:
        writing_file.write(items.strip('\n'))
  userInfo = ""
  if bool_value == False:
    userInfo = "This user does not exit, or the data is not a valid input."
    
  ########### YOUR CODE GOES HERE ##########
#access the text from the boxes in the same way as for the add function. Only delete a user if first name last name and age are all a match. Display a message indicating whether the deletion wasa successful or not. Recall that userInfo stores the text that goes in the main display box. Alternatively, you can print it to the console.



  ##########################################

  textBox.delete('1.0', tk.END)
  textBox.insert('1.0', userInfo)


def SearchUsers():
  global fNameBox
  global lNameBox
  global ageBox
  global textBox
  FName = fNameBox.get('1.0', 'end-1c')
  LName = lNameBox.get('1.0', 'end-1c')
  age = ageBox.get('1.0', 'end-1c')
  userInfo = textBox.get('1.0', 'end-1c')

  text_for_file = FName + ", " + LName + ", " + age
  with open("images/user info.txt", "r") as the_names:
    names = the_names.readlines()
  bool_value = False
  for items in names:
    if items.strip('\n') == text_for_file:
      userInfo = names[names.index(items)].strip('\n') + " was found"
      bool_value = True
    k = items.strip('\n').split(',')
    if k[0].strip() == FName:
      if LName == "" and age == "":
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
      if k[1].strip() == LName and age == "":
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
      if k[2].strip() == age and LName == "":
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
    if k[1].strip() == LName:
      if FName == "" and age == "":
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
      if k[0].strip() == FName and age == "":
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
      if k[2].strip() == age and FName == "":
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
    if k[2].strip() == age:
      if FName == "" and LName == "":
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
      if k[0].strip() == FName and LName == "":
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
      if k[1].strip() == LName and FName == "":
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
        userInfo = names[names.index(items)].strip('\n') + " was found"
        bool_value = True
  if bool_value == False:
    userInfo = "User not found or invalid input."
          

  ########### YOUR CODE GOES HERE ##########
#access the text from the boxes in the same way as for the add function
  #search the contents of the file for a user matching the first name last name and age in the boxes. If nothing is enterd in one of the boxes, then search the search should find a match as long as the text in the box(es) that are filled in has a match in the user info.txt file. Display the found user's first name last name and age, or display "user not found". Recall that userInfo stores the text that goes in the main display box.
  



  ##########################################
  
  textBox.delete('1.0', tk.END)
  textBox.insert('1.0', userInfo)
  
#############################################################



  


  
#################### YOU DON'T NEED TO READ OR UNDERSTAND THIS ####################

SortHeading = tk.Label(text="Sort By", background=bgColour, fg = fontColour, font=(LabelFontType, LabelFontSize))
SortHeading.place(x = radioButtonXloc, y = radioButtonYloc-spacingY)

R1 = ttk.Radiobutton(window, text="First Name", variable=sortOption,  value=0)
R1.place(x=radioButtonXloc, y=radioButtonYloc)

R2 = ttk.Radiobutton(window, text="Last Name", variable=sortOption, value=1)
R2.place( x=radioButtonXloc, y=radioButtonYloc + spacingY*1)

R3 = ttk.Radiobutton(window, text="Age", variable=sortOption, value=2)
R3.place(x=radioButtonXloc, y=radioButtonYloc + spacingY*2)


style = ttk.Style(window)
style_name = R1.winfo_class()

style.configure(style_name, foreground=fontColour, background=bgColour, indicatorcolor=bgColour, font=(fontType, fontSize))

style.map(style_name, 
          foreground = [('disabled', fontColour), ('pressed', fontColour), ('active', fontColour)], 
          background = [('disabled', bgColour),('pressed', '!focus', bgColour), ('active', bgColour)], 
          indicatorcolor=[('selected', fontColour), ('pressed', fontColour)])




button = tk.Button(text="Get User Info", background=bgColour, fg = fontColour, font=(LabelFontType, LabelFontSize), command=SortUsers)
button.place(x = radioButtonXloc, y=radioButtonYloc + spacingY*3 + 5)




######## UNCOMMENT FOR ADD, DELETE, AND SEARCH USER EXTENSIONS ########
addUserBtn = tk.Button(text="Add", background=bgColour, fg = fontColour, font=(LabelFontType, LabelFontSize), command=AddUser)
addUserBtn.place(x = radioButtonXloc, y=addDelSearchButtonY)

delUserBtn = tk.Button(text="Del", background=bgColour, fg = fontColour, font=(LabelFontType, LabelFontSize), command=DelUser)
delUserBtn.place(x = radioButtonXloc + 85, y=addDelSearchButtonY)

SearchButton = tk.Button(master = window, relief=tk.FLAT, background = bgColour, border = "0", image=searchButtonImage, activebackground=bgColour, command=SearchUsers)
SearchButton.place(x = 550, y=addDelSearchButtonY-1)

######################################################




tk.mainloop()