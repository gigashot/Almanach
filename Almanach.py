
plant1 = {
"Name": "Peashooter",
"Damage": "normal",
"Description": "yapping",
"Cost": 100,
"Recharge": "fast",
}


plant2 = {
"Name": "Squash",
"Damage": "massive",
"Description": "AUUHUGA",
"Cost": 50,
"Recharge": "slow",
}

plant3 = {
"Name": "Sunflower",
"Sun Production": "normal",
"Description": "hihi",
"Cost": 50,
"Recharge": "fast",
}

plant4 = {
"Name": "Tall-nut",
"Toughness": "very high",
"Special":"none",
"Description": "UHUDGIAU",
"Cost": 125,
"Recharge": "slow",
}

plants = {
"PEASHOOTER" : plant1,
"SQUASH" : plant2,
"SUNFLOWER" : plant3,
"TALL-NUT" : plant4
}
for keys in plants:
    print("--------------------------------------------------")
    print(keys)
    for keys2 in plants[keys]:
        print(keys2, ":", plants[keys][keys2])
    