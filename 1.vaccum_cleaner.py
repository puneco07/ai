def vaccum_agent(location,status):
    if status== "Dirty":
        return "Suck"
    elif location=="A":
        return "Right"
    else:
        return 'Left'

rooms={"A":"Dirty","B":"Dirty"}
location="A"

print("Initial Envoirment:",rooms)

for i in range(5):
    status=rooms[location]
    action=vaccum_agent(location,status)

    print("Location:",location)
    print("Status:",status)
    print("Action:",action)
    
    if action=="Suck":
        rooms[location]="Clean"
    if action=="Right":
        location="B"
    if action=="Left":
        location="A"
    
    print("Updated Enviorment:",rooms)

    if rooms["A"]=="Clean" and rooms["B"]=="Clean":
        print("All rooms are clean.")
        break

