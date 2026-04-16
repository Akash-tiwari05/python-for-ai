#Functions with logic

def check_weather():
    temperature = 25 # local scope vaiable
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather()