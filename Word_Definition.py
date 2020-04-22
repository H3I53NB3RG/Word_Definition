import json
from difflib import get_close_matches

f = open("banner.txt","r")
print(f.read())
f.close()

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input("[-] Do u mean " + get_close_matches(w,data.keys())[0] + " ? Enter Y if yes, or N if no : ").upper()
        if answer == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif answer == "N":
            return "The Word Dosen't Exsist !"
        else:
            return "[-] Sorry, But I Don't Understand What The Fuck Do U Want :("
    else:
        return "The Word Dosen't Exsist !"

word = input("[+] Enter a Word : ")
output = translate(word)
if type(output) == list:
    for item in output:
        print("- " + item)
else:
    print("[-] " + output)
