"""the join function is the opposite to the split functions it joins all the value is a list with a given character or sequence f characters using them as separators in the list!"""

words = "this is a really big sentence!".split(" ")
print (words)
new_words = " \033[35m<new seperator>\033[37m ".join(words)
print (new_words)