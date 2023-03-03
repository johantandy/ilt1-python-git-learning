# hour = 13

# if hour < 12:
#     print("good morning")

# else :
#     print("telat")

def check(number):
    if number > 0 :
        return "positive"
    elif number == 0:
        return "Zero"
    else:
        return "negative"
    
print(check(1))
print(check(-1))
print(check(0))