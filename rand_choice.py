import random
import shlex

def choose(string):
    if len(string) <= 8 or string[8:].isspace():
        return "I don't see any choices!"
    string = string[8:]
    if not(',' in string.strip() or ' ' in string.strip() or '\t' in string.strip()):
        return "Only 1 choice is cheating!"
    if ',' in string:
        string = string.split(",")
        for index,element in enumerate(string):
            string[index] = string[index].strip().strip("'").strip('"')
            #.replace("'","").replace('"',"")
            if string[index].strip() == '':
                del string[index]
    else:
        string = shlex.split(string)

    unique = set(string)
    if len(unique) == 1:
        return "Same choice is cheating!"

    return random.choice(string).strip()

# print(choose("!choose don't go to school, 'go to school' "))
# print(choose('!choose don\'t go to school, "go to school" '))
# print(choose("!choice do something, don't do something"))
# print(choose("!choice test,test ,test"))