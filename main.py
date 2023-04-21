player = {
    'name': 'San',
    'age': 18,
    'alive': True,
    'fav_food': ["Pizza","Beef"],
    'friend': {
        'name': 'Will',
        'fav_food': ["Apple"],
    }
}

player['fav_food'] = "apple"
player.pop("alive")
player["friend"]['fav_food'].append("Banana")

print(player)