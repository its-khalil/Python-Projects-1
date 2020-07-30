from datetime import datetime

birthday = input("Insert Your Birthday Party In This Format (eg.: YYYY MM DD): ")
spliting = birthday.split(" ")

print(spliting)

day = int(spliting[2])
month = int(spliting[1])
year = int(spliting[0])

left = datetime(year, month, day) - datetime.now()
 
print(f"Time left from your birthday is : {left.days} days.")



