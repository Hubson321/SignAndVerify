import Alice
import Bob
import easygui


#GUI variables
title = "Choose to be Sender or Receiver"
message =  "Digital signature"
buttons = ["Sender","Receiver","Exit"]


while True:
  choice = easygui.buttonbox(title,message,buttons)
  match choice:
    case "Sender":
      Alice.GUI()
    case "Receiver":
      Bob.GUI()
    case "Exit":
      break  
    
