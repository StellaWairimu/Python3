fName = "Stella"
lName = " Wairimu"
username = fName + lName

fullName = input("Enter the username here : ")

#print(f"Hello my name is" + "\n" + fName) 


if fullName == username:
     print("Welcome to ChapChap")

else :
   
    print("Incorrect username , please enter the details again")

payment = ["cash" ,"card","mobile money"]

print(f"Available payment options" )
print(payment)

modeOfPayment = input("enter prefered mode of payment: ")

if modeOfPayment in payment:
    print ("Proceed to checkout")
else:
    print(f"You entered" + " " +  modeOfPayment + " " + "not accepted here, please enter any of the 3 available options")
    print(payment)

 

   
    


