# Function using kwargs

def print_details(**info):
    for key, value in info.items():
        print(key, ":", value)
        
print_details(name="Ravi", age=22, city="HYD")