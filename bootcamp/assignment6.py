# Write a program to create a list of your favourite songs and add them to a list. 

defaultlist = ("song1, song2, ")
for slist in defaultlist.split():
    print ( f"your Favourite songs are {slist}")

# Accept new song from the user as input and add it to the list.  
allsong = []
defaultlist = ("song1, song2, ")
songlist = input("Enter your Favourite songs (comma(,)seprated):")
for slist in songlist.split():
    allsong.append(defaultlist + slist)
    allsong.sort()
    print ( f"your Favourite songs are {allsong}")


# Accept song name as input from the user and new song name to replace and perform update operation on the list  
defaultlist = ['song1', 'song2']
songlist = input("Enter your Favourite songs (comma(,)seprated):")
for slist in songlist.split():
    defaultlist = slist[:]

    print ( f"your Favourite songs are {defaultlist}")  


# Accept song name to delete and delet it from the list Consider below data structure and perform list of operations on it.







#  Add new persone named 'Ram' with age 11 into this list. 


# Modify Age of Michel to 32 


# Delete Alex informtion from this list


# dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
#dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}
# - Find the union of both the Sets


# Sort dataScientist in reverse order


# Add new item into dataEngineer

# Remove SQL from dataScientist Set.


# Define new Set and add Nodejs, ReactJs, ExpressJs, Javascript in it.