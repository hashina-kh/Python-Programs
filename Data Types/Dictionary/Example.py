mydict = {
    "ID": "1",
    "Name": "Anna",
    "Age": 23,
    "Mobile": 1234567890,
    "Place": "Kottayam",
    "Course": "Python Django",
    "College": "Luminar TechnoLab"

}
print(mydict)

#add
mydict["Skills"]=["Python", "Html","Java","Css",".Net"]
print("update Skills:",mydict)

#remove
del mydict["Mobile"]
print("Remove Mobile Number:",mydict)