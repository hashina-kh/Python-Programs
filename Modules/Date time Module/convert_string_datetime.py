import datetime

x = datetime.datetime.now()
print("----------Current date-------------")
print(x)

print("---------datetime convert to string format------------------")
print(x.strftime("%a"))  # Day te aprehesion form  eg:- mon
print(x.strftime("%A"))  # Day te full form eg:- monday

print(x.strftime("%d"))    # only the date  eg:- 20
print(x.strftime("%D"))   # full version of date  05/25/2024

print(x.strftime("%x"))   # same as %D
print(x.strftime("%X"))   # Full Version of time
print(x.strftime("%b"))   # Month te abrvehesion form  eg:- jan
print(x.strftime("%B"))   # Month te full form eg:- Janvary



