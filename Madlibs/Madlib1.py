## string concatenation (aka how to put string together)
## suppose we want to create a string that says "subscribe to ____ "
#youtuber = "Peter Rusak" # some string varaiable
#
## a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

noun1 = input("Noun: ")
adj1 = input("Adj: ")
noun2 = input("Noun: ")
adj2 = input("Adj: ")
adj3 = input("Adj: ")
noun3 = input("Noun: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
adj4 = input("Adj: ")

madlib = f"Being a network administrator is like being a {noun1}. No one likes being a {noun1} because it is {adj1}. Work starts off by consoling into the {noun2}. Some people call this the phone port, but they are fucking {adj2}. The next step is copying and pasting MNOC {adj3} dogshit {noun3}s we call templates. We {verb1} these templates until we can't anymore, then we just {verb2} ourselves. Never be a networker, or you will end up {adj4}."

print(madlib) 


