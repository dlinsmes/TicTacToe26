file = "demo text.txt"

#r - read the file
fileContents = open(file, "r")

#classifications of each email - 1 is spam, 0 is not
labels = []

for line in fileContents:
    #append the 0th char of each line as an int
    labels.append(int(line[0]))

print(labels)

#if looping through file contents more than once, need to reset
#the "cursor" after each loop so that it can start over
fileContents.seek(0)

emails = []
for line in fileContents:
    #take everything from the line starting at index 2
    emails.append(line[2:])

print(emails)

#for each loop to iterate through each email
for email in emails:
    print(email)

#save each word in a string to a list
wordlist = emails[0].split()

print(wordlist)

#dictionaries are like lists but you can index by strings rather than by sequence numbers
dictionary = {}

dictionary["potato"] = 5

print(dictionary)

dictionary["banana"] = 7

print(dictionary)

#increment a value stored at the key (index) potato
dictionary["potato"] += 1
print(dictionary)

print(dictionary.keys())

if "james" in dictionary.keys():
    dictionary["james"] += 1
else:
    dictionary["james"] = 10

print(dictionary)

#delete key/value pairs from the dictionary
del dictionary["james"]
del dictionary["potato"]
del dictionary["banana"]

#make a dictionary of the email 0 words where the keys are the different words
#and the values are the number of occurrences of each word
for word in wordlist:
    #check if the word is already a key in the dictionary
    if word in dictionary.keys():
        #increment the value
        dictionary[word] += 1
    else:
        #if not, add the word as a key and give an initial value of 1
        dictionary[word] = 1

#how many keys
print(len(dictionary))

#find the most frequently occurring word in email 0
maxCount = 0
frequentWord = ""
#iterate through a dictionary by key
for word in dictionary:
    if dictionary[word] > maxCount:
        maxCount = dictionary[word]
        frequentWord = word

print(frequentWord, maxCount)
