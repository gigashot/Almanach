
plant1 = {
"Name": "Peashooter",
"Damage": "normal",
"Toughness": "low",
"Special":"none",
"Description": "A green Pea-plant that shoots a pea every few seconds.",
"Cost": 100,
"Recharge": "fast",
}


plant2 = {
"Name": "Squash",
"Damage": "massive",
"Toughness": "low",
"Special":"none",
"Description": "An angry Squash that crushes anything that gets close.",
"Cost": 50,
"Recharge": "slow",
}

plant3 = {
"Name": "Sunflower",
"Damage": "none",
"Toughness": "low",
"Special":"sun production",
"Description": "A happy Sunflower that produces sun over time.",
"Cost": 50,
"Recharge": "fast",
}

plant4 = {
"Name": "Tall-nut",
"Damage": "none",
"Toughness": "very high",
"Special":"Can't be vaulted or jumped over",
"Description": "A tall Wall-nut that protects plants behind him with his own body.",
"Cost": 125,
"Recharge": "slow",
}

plants = {
"PEASHOOTER" : plant1,
"SQUASH" : plant2,
"SUNFLOWER" : plant3,
"TALL-NUT" : plant4
}

def add_New_Plant():
    new_plant = {}

    new_plant["Name"] = input("Enter the plant name: ")
    new_plant["Damage"] = input("Enter the damage type: ")
    new_plant["Toughness"] = input("Enter the toughness level: ")
    new_plant["Special"] = input("Enter any special ability: ")
    new_plant["Description"] = input("Enter the plant description: ")
    new_plant["Cost"] = int(input("Enter the cost: "))
    new_plant["Recharge"] = input("Enter the recharge time: ")

    plants[new_plant["Name"].upper()] = new_plant


def show_All_Plants():
    for keys in plants:
        print("--------------------------------------------------")
        print(keys)
        for keys2 in plants[keys]:
            print(keys2, ":", plants[keys][keys2])

def action_Choose():
    print("Vyberte si funkci co chcete provést: ")
    print("1) přidat novou rostilu")
    print("2) ukázat všechny rostliny")
    print("3) ukončit program")
    chosen_Option = int(input(""))
    if chosen_Option == 1:
        add_New_Plant()
        action_Choose()
    elif chosen_Option == 2:
        show_All_Plants()
        action_Choose()
    elif chosen_Option == 3:
        return print("program ukončen")
    else:
        action_Choose()
action_Choose()
