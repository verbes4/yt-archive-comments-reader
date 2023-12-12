import os
import json
import pprint

#creates a list, then uses os.walk to add all files in current directory (getcwd) to it.
#i stole it from stackoverflow and just modified it to use getcwd so idk how it rlly works.
files = []
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    files.extend(filenames)
    break

#remove main.py from the list
while ("main.py" in files):
    files.remove("main.py")

#tell the user how many JSON's there are
print("There are", len(files), "JSON's.")
print(files)

#ask them which one they want by picking a number
lenOfFilesStr = str(len(files))
picked = int(input("\nWhat one do you want? Pick between 1 - " + lenOfFilesStr + ": "))
picked=picked-1
print("You picked", files[picked])

#opens the json file
file = open(files[picked])
#loads it as a list in python
loaded = json.load(file)
#prints how many comments there are
print("\nThere are", len(loaded), "comments.")
#asks which one they want, -1 bc python lists start at 0
commentPicked = int(input("Which one do you want: ")) - 1

#will load the comment as a dictionary so can use key shit
comment = loaded[commentPicked]
#loads authors details in a seperate list cuz easy
authorStuff = comment['author']
#print(comment)
#prints all the comment stuff yay
print("\nThis comment reads: ")
print(comment['commentText'])
print("Written by:", authorStuff['title'])
#splits date and time lol
splitDate = comment['commentDate'].split("T")
print("Date:", splitDate[0])
print("Time", splitDate[1])
print("Likes:", comment['likes'])
print("Replies:", comment['replyCount'])
print("Commenters PFP:", authorStuff['thumbUrl'])
