sname = "arpita game"
      #  012345678910
#-10-9-8-7-6-5-4-3-2-1  
#slicing 

print(sname[ : ])      
print(sname[1: ])
print(sname[ :10])
print(sname[ -6: -1])
print(sname[0 : 8])
print(sname[1:8])
print(len(sname))

#string operations
print("arpita" in sname)   #boolean values
print("Arpita" in sname)
print(sname.__len__())
print(sname.capitalize())
print(sname.upper())
print(sname.lower())
print(sname.find('r'))
print(sname.replace('a', 'P'))


