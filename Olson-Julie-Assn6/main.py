import random
def verb_pick():
    verb = ["chop", "pan-fry", "cool", "stir", "sautee", "caramelize", "marinate", "plate", "wash", "roast"]
    return random.choice(verb)

def adj_pick():
    adj = ["flavorful", "colorful", "crisp", "crunchy", "glazed", "savory", "fresh", "garlicky", "spicy", "pickled"]
    return random.choice(adj)

def noun_pick():
   noun = ["mushrooms", "steak", "carrots", "rice", "noodles", "scallions", "water chestnuts", "baby corn", "broccoli", "pork belly"]
   return random.choice(noun)


print("\n\n")
print("Bibimbap Instruction Generator\n")

i = 1

for i in range(1, 11):
    print(str(i) + " - " + verb_pick() + " the " + adj_pick() + " " + noun_pick())
    i += 1
print("\n\n")

