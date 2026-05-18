#Library book tracker
books={
    "fire wings":25,
    "radhe krishna":50,
    "friendship":33
}
books["the jungle book"]=58
books["radhe krishna"]-=25
books["fire wings"]+=25
for item,qty in books.items():
    print(item,":",qty)



#simple shopping cart program 
stuffs={
    "chocolates":100,
    "icecreams":250,
    "chips":500
}
stuffs["juice"]=45
stuffs["chips"]-=500
stuffs["icecreams"]+=500
for item,qty in stuffs.items():
    print(item,";",qty)




#flight tracker 
flights = {
    "AI202": {"Destination": "Delhi", "Time": "10:30", "Status": "On Time"},
    "EK101": {"Destination": "Dubai", "Time": "12:00", "Status": "Delayed"}
}
flights["SQ505"] = {"Destination": "Singapore", "Time": "16:00", "Status": "On Time"}

flights["AI202"]["Status"] = "Delayed"

print("EK101:", flights.get("EK101", "Not Found"))

for num, info in flights.items():
    print(num, "→", info)

