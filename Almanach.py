
plant1 = {
"NAME": "Peashooter",
"DAMAGE": "normal",
"DESCRIPTION": "yapping",
"COST": 100,
"RECHARGE": "fast",
}


plant2 = {
"NAME": "Squash",
"DAMAGE": "massive",
"DESCRIPTION": "AUUHUGA",
"COST": 50,
"RECHARGE": "slow",
}

plant3 = {
"NAME": "Sunflower",
"SUN_PRODUCTION": "normal",
"DESCRIPTION": "hihi",
"COST": 50,
"RECHARGE": "fast",
}

plant4 = {
"NAME": "Tall-nut",
"Toughness": "very high",
"SPECIAL":"none",
"DESCRIPTION": "UHUDGIAU",
"COST": 125,
"RECHARGE": "slow",
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
    