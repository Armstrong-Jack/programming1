#collects the users inputs
users_name =input("please enter your name")
username =input("please enter your username")
location =input("please enter your current location")

#ascii art peices
cornor = "+"
vertical_wall = "|"
horizontal_wall ="-"
space = " "
title_length = "-------------"

#finds the longer user entry for the ascaii art
if len(users_name) >= len(username):
    print("1") # for debugging
    horizontal_wall *= len(users_name) # if username is longest it will create a horizontall wall of ascii in that length
elif len(username) >= len(location): 
    print("2") # debugging
    horizontal_wall *= len(username) # if username is the longest it will create the horizontal wall that size
else: # if neither of them are the longest it leaves location to be the longest
    print("3") # debuging
    horizontal_wall *= len(location)# creates the horizontal wall as long as location





#creates the whitespace for the ascii art to line up correctly for thr last horizontal wall

#space 1 will give 0 if username is the longest value as it needs no whitespace but if it isn't
# it will give whitspace of the differance of the longest user input and the username input  
space1 = len(horizontal_wall) - len(username)
#will create the deadspace
space1 *= space
# it will create the deadspace between the differance of the horizontal wall and the users_name
space2 = len(horizontal_wall) - len(users_name)
space2 *= space # actully creates the deadspace
#will see how big the variable for required whitspace is by calculating the differance between the horizontal wall and location
space3 = len(horizontal_wall) - len(location)
space3 *= space # will create that whitespace

#this is for the title length when it is acctully rinted covering the Data type names 
horizontal_wall += title_length 

#displays the ascii art and the users inputerd data and the data field names
print(cornor, horizontal_wall, cornor)
print(vertical_wall, "name:      ", users_name, space2,  vertical_wall,)
print(vertical_wall, "username:  ", username, space1,  vertical_wall)
print(vertical_wall, "location:  ", location, space3, vertical_wall)
print(cornor, horizontal_wall, cornor)