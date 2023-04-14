def tax_cal(money):
    return money * 0.35

def pay_tax(tax):
    print("thanks you for paying", tax)

pay_tax(tax_cal(15000))