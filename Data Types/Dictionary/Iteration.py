mydict = {
    "Name": "Anna",
    "Age": 23,
    "Course": "Python Django",
    "Location": "Kochi"
}

print(mydict)
#Only Keys print

# for i in mydict:
#     print(i)

# for i in mydict.keys():
#     print(i)

#Only values print

# for i in mydict.values():
#     print(i)

#Keys and Values print akkan
for i in mydict.items():
    print(i)
