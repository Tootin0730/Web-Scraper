player = {
    'name': 'San',
    'age': 18,
    'alive': True,
    'fav_food': ["Pizza","Beef"],
}
player['fav_food'].append("Noodles")
print(player.get('fav_food'))
print(player['fav_food'])