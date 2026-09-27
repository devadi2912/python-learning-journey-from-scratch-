# the split functions as we know it works on a string and returns a lsit of words that were seperated by the sspecified characters
# mentiond in the split function .. 

str =  "this is a string seperated by whidespaces,and?qustion-marks and,commas"
# words = str.split(" ?,")    # this will not word it will look for the seperator " ?," and not for " ","?",","



simple_string = "this is a simple string seeprated with just whide spaces!"
words=simple_string.split(" ")
print (words) # this will print the list of words seperated by the specified list of characters 



"""the join funcition is the opposite to the split funcitons it joins all the value is a list with a given character or sequence f characters using them as seperators in the list!"""

new_words = " \033[35m<new seperator>\033[37m ".join(words)
print (new_words)