mydict = {
    "Name": "Anna",
    "Age": 23,
    "Course": "Python Django",
    "Location": "Kochi",
    "Skills": ["Python",".Net","Html","Css"]
}

print(mydict)

# add
mydict["College"] = "MES College"
print(mydict)

# Update
mydict["Name"] = "Abin"
print(mydict)

# Delete
del mydict["Age"]
print(mydict)