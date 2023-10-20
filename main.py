import requests as req

# key = UDHFTGHVCJUDI

print("Welcome to Nolan's comment website!\nHere you can see nolan's comments on fruits or grades of people.")
ip=input("what is nolan's ip today?\n>>")
appid = input("What is your key?\n>>")
ask = 0
while ask ==0:
    route = input("Which would you like to access?(fruit/grade) \n>>")
    route=route.lower()
    insert = input("What exact item do you like to see?\n>> ")
    if route != "grade":
        if route != "fruit":
            print("Route does not exist.")
    url_string =f"http://{ip}:8000/{route}s/get_info?{route}={insert}&appid={appid}"

    response =req.get(url=url_string)
    json_data = response.json()


    if "msg" in json_data:
        print(json_data['msg'])
    else:
        if route == "grade":
            json_data['name'] = json_data['name']
            name = json_data['name'].capitalize()
            print(f"{json_data['name']} has the grade of {json_data['Grades']}, and nolan's comment on its gender is {json_data['gender']}.")
        if route == "fruit":
            print(f"{json_data['fruit']} has the color of {json_data['color']}, and nolan's comment on its goodness is {json_data['goodness']}.")
    ask_again = input("Do you want to access another piece of info?(Yes or No)\n>>")
    if ask_again.lower() == "no":
        ask += 1
