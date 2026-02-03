import requests
import json

# Take user input
count = int(input("Enter number of users to fetch: "))

url = f"https://randomuser.me/api/?results={count}"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        users_list = []

        print("\nUser Details:\n")

        for user in data["results"]:
            name = user["name"]
            location = user["location"]

            user_info = {
                "full_name": f"{name['title']} {name['first']} {name['last']}",
                "email": user["email"],
                "gender": user["gender"],
                "country": location["country"]
            }

            users_list.append(user_info)

            print("Name:", user_info["full_name"])
            print("Email:", user_info["email"])
            print("Gender:", user_info["gender"])
            print("Country:", user_info["country"])
            print("-" * 30)

        # Save to file
        with open("user_data.json", "w") as file:
            json.dump(users_list, file, indent=4)

        print("\nData saved to user_data.json")

    else:
        print("Failed to fetch data. Status code:", response.status_code)

except Exception as e:
    print("Error occurred:", e)
