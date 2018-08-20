import math
import random

#we want to build an id in this format A3C44B

#characters = ["A","B","C","D","1","2","3","4"]
charactersUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charactersLower = "abcdefghijklmnopqrstuvwxyz"
charactersSymbol = "!@#$%^&*"
charactersNumbers = "1234567890"

#Receive user input 
print("Enter Password Length: ")
passLength = int(input())

print ("Should your password include Uppercase Letters? Y/N")
alpha_Uppercase = input()

print (alpha_Uppercase)
print ("Do you want to use Lowercase Alphabets? Y/N ")
alpha_Lowercase = input()

print ("Should we include symbols as well? Y/N")
use_Symbols = input()

#build the character list

mycharacters = ""
if str(alpha_Uppercase.upper) == "Y":
	mycharacters = mycharacters + charactersUpper

if str(alpha_Lowercase.upper) == "Y":
    mycharacters = mycharacters + charactersLower

if str(use_Symbols.upper) == "Y":
    mycharacters = mycharacters + charactersSymbol
		

print (mycharacters)

total_length = len(mycharacters)

final_password = ""

#for y in range(0,passLength):	
	#gen_rand_num = math.floor(random.randrange(1,total_length))
	#gen_rand_num = random.randrange(1,total_length)	

	#build the characters
	#final_password = final_password + mycharacters[gen_rand_num]
	
	
	
#print ("Your Password is: " , final_password)



