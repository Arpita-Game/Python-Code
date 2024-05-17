#dictionary
'''employee={
    "name":"arpita",
    "age" : 23
}
print(employee.get("name"))'''

#program
text = input("Enter the text:")
words = text.split(' ')
emoji={
    ":)":"😀",
    ":(":"😢",
}
output=" "
for ch in words:
    output += emoji.get(ch,ch)+ " " #not clear
print(output)