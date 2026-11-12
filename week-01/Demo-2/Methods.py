#Task 02 Clean up a name
Name = " aMNA rAZA "
FinalName = Name.strip().title()
print(f"Welcome {FinalName}! Your Name has {len(Name)} Characters")

#Clean an email. 
email = " Ali.Khan@GMAIL.com "
CleanedEmail = email.strip().lower()
print(f"the cleaned email is:, {CleanedEmail} , {len(CleanedEmail)} characters" )

 #A receipt line. 
ItemName = " wireless MOUSE "
price = 2499
quantity = 3
Final = ItemName.title().strip()
TotalPrice = price * quantity
print(f"{Final} x{quantity} = Rs {TotalPrice}")

#Order codes.
raw_code = " ord-2024-0042 "
Cleaned_code = raw_code.replace("ord-2024-0042","ORD20240042")
print(Cleaned_code)
NewCode = Cleaned_code.strip()
print(f"{NewCode} Has {len(NewCode)} Characters!")

 #Usernames. 

first = " bilal "
last = "QURESHI "
city = "lahore"
firstName = first.strip()
lastName = last.lower().strip()
X = f"{firstName}.{lastName}_{city[0:3]}"
print(X,len(X))

