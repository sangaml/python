i = 0
defaultlist = ['song1', 'song2']
songlist = [] 
songlist = input("Enter your song name to delete from list (comma(,)seprated):")
for i in songlist:
    print (i)
# rm_item = 
print(defaultlist)
for items in songlist:
    defaultlist.remove(items)
    print(defaultlist)
# for items in defaultlist:
#    defaultlist.remove
    


'''
songlist = input("Enter your song name to delete from list (comma(,)seprated):")
for slist in songlist.split():
    print(slist)
    for oldlist in defaultlist.split():
        print(oldlist)
        if slist == oldlist:
            i += 1
            print (songlist[i])
            del songlist[i]   
            print ("string matches")
'''
