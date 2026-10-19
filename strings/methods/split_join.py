# the split functions as we know it works on a string and returns a list of words that were separated by the specified characters
# mentioned in the split function ..

str =  "this is a string seperated by whidespaces,and?qustion-marks and,commas"
# words = str.split(" ?,")    # this will not work it will look for the separator " ?," and not for " ","?",","



simple_string = "this is a simple string seeprated with just whide spaces!"
words=simple_string.split(" ")
print (words) # this will print the list of words separated by the specified list of characters



"""the join function is the opposite to the split functions it joins all the value is a list with a given character or sequence f characters using them as separators in the list!"""

new_words = " \033[35m<new seperator>\033[37m ".join(words)
print (new_words)