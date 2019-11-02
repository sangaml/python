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
    for olist in defaultlist.splist():
        if slist == olist:   
        slist.remove()
    print(defaultlist)

    print ( f"your Favourite songs are {defaultlist}")  


# Accept song name to delete and delet it from the list Consider below data structure and perform list of operations on it.

songlist = input("Enter your song name to delete from list (comma(,)seprated):")
for slist in songlist.split():
    print(slist)
    for oldlist in defaultlist.split():
        print(oldlist)
        if slist == oldlist:
            i += 1
            print (songlist[i])
            songlist[i].remove 
            print ("string matches")





#  Add new persone named 'Ram' with age 11 into this list. 
dic = [{'tim':18}, {'Michel':30}, {'Alex':31}]

Name = input("Enter Name:").lower()
Age = int(input("Enter Age:").lower())
dictionary = {}
dictionary[Name] = Age
dic.append(dictionary)
print(dic)
# Modify Age of Michel to 32 
dic = {'tim':18,'Michel':30,'Alex':31}

Age = int(input("Enter Age:"))
dic['Michel'] = Age

print(dic)

# Delete Alex informtion from this list
dic = {'tim':18,'Michel':30,'Alex':31}
dic.pop('Alex')

print(dic)

# dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
#dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}
# - Find the union of both the Sets
dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}

final = dataScientist.union(dataEngineer)
print(final)

# Sort dataScientist in reverse order
dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
z=[]

for x in dataScientist:
    #print(x)
    z.append(x)
final_op = set(z[::-1])
    
# Driver Code 
print(final_op)

# Add new item into dataEngineer
dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}
data = input("Enter string to add into dataEngineer set:\n")
dataEngineer.add(data)
print(dataEngineer)

# Remove SQL from dataScientist Set.
dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
dataScientist.discard('SQL')
print(dataScientist)

# Define new Set and add Nodejs, ReactJs, ExpressJs, Javascript in it.

def software(data):
    d = data.split(",")
    software = set(d)
    print(software)

software('Nodejs,ReactJs,ExpressJs,Javascript')