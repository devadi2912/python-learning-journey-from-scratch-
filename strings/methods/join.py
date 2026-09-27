"""the join funcition is the opposite to the split funcitons it joins all the value is a list with a given character or sequence f characters using them as seperators in the list!"""

words = "this is a really big sentence!".split(" ")
print (words)
new_words = " \033[35m<new seperator>\033[37m ".join(words)
print (new_words)