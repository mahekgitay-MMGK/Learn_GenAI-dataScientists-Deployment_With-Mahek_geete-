def calculated_cost(tokens):
    cost=(tokens/1000)*0.002
    return cost
print(calculated_cost(1000))
print(calculated_cost(1500))
print(calculated_cost(2100))
print(calculated_cost(2500))
print(calculated_cost(3100))


#Real GenAI 10,000 users

def check_access_and_cost(user):
    cost=(user["tokens"]/1000)*0.002
    if user["tokens"] >= 1000 and user["is_paid"]== True:
        return f"name : {user["name"]} , tokens : {user["tokens"]} and is_paid : {user["is_paid"]} \n You can access gpt-4 \n cost ${cost:.4f}"
    else:
        return f"name : {user["name"]} , tokens : {user["tokens"]} and is_paid : {user["is_paid"]} \n You can access gpt-3.5 \n cost ${cost:.4f}"


users_data = [
    {"name": "mahek", "tokens": 1500, "is_paid": True},
    {"name": "aarav", "tokens": 820, "is_paid": False},
    {"name": "anaya", "tokens": 2340, "is_paid": True},
    {"name": "arjun", "tokens": 670, "is_paid": False},
    {"name": "diya", "tokens": 1890, "is_paid": True},
    {"name": "vivaan", "tokens": 430, "is_paid": False},
    {"name": "isha", "tokens": 2760, "is_paid": True},
    {"name": "kabir", "tokens": 1120, "is_paid": False},
    {"name": "meera", "tokens": 950, "is_paid": True},
    {"name": "rohan", "tokens": 3180, "is_paid": True},
    {"name": "sana", "tokens": 540, "is_paid": False},
    {"name": "aditya", "tokens": 2070, "is_paid": True},
    {"name": "kiara", "tokens": 760, "is_paid": False},
    {"name": "dev", "tokens": 1430, "is_paid": True},
    {"name": "riya", "tokens": 990, "is_paid": False},
    {"name": "ayaan", "tokens": 2510, "is_paid": True}]

for user in users_data:
    print(check_access_and_cost(user))