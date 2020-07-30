msg = "Enter your Periodic Number here in this format(eg. 10.1234), note: don't repeat what's after the comma"
msg2 = "For example if your number is: 10.123412341234 write: 10.1234:"

def pn(var):
    split = var.split(".")
    first_part = split[0]
    second_part = split[1]
    lenghth = len(second_part)
    x = int("9"*lenghth)
    first_part = int(first_part)
    second_part = int(second_part)
    denominator = x
    numerator = x * first_part + second_part
    fraction = f"The fraction is: {numerator} / {denominator}" 

    return fraction

print(msg)
print(msg2)
user_input = input("--> ")
print(pn(user_input))