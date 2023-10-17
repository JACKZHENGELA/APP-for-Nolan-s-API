import requests as req

# key = UDHFTGHVCJUDI

print("Welcome to Nolan's website!")
route = input("Which route would you like to access?(fruit/grade) \n>>")
route=route.lower()
insert = input("What do you like to see?\n>> ")
appid = input("What is your key?\n>>")
if route != "grade":
    if route != "fruit":
        print("Route does not exist.")


url_string =f"http://10.6.20.113:8000/{route}s/get_info?{route}={insert}&appid={appid}"

response =req.get(url=url_string)
json_data = response.json()


if "msg" in json_data:
    print(json_data['msg'])
else:
    if route == "grade":
        print(f"{json_data['name']} has the grade of {json_data['Grades']}, and nolan's comment on its goodness is {json_data['goodness']}.")
    if route == "fruit":
        print(f"{json_data['fruit']} has the color of {json_data['color']}, and nolan's comment on its goodness is {json_data['goodness']}.")
