def make_juice(fruit):
    return f"{fruit} + juice"

def add_ice(juice):
    return f"{juice} + ice"

def add_sugar(iced_juice):
    return f"{iced_juice} + sugar"

juice = "apple"
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice, "is the perfect juice")
