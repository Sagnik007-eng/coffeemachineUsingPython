from resource import *
w=resources["water"]
m=resources["milk"]
c=resources["coffee"]
money=0
true=True
while(true):
  tot_dol = 0
  i=input("What would you like?(espresso/latte/cappuccino")
  true=(w > 0) and (m > 0) and (c > 0)
  if i=="report":
      print(f'Water: {w}')
      print(f'Milk:{m}')
      print(f'Coffee:{c}')
      print(f'Money:${money}')
  elif i=="espresso":
      while(True):
        print("Please insert coins.")
        qt=float(input("How many quarters?: "))
        dm=float(input("How many dimes?: "))
        nk=float(input("How many nickels?: "))
        pen=float(input("How many pennies?: "))
        tot_dol=(qt * 0.25)+(dm * 0.10)+(nk * 0.05)+(pen * 0.01)+tot_dol
        if tot_dol>=MENU["espresso"]['cost']:
            change=tot_dol - MENU["espresso"]['cost']
            print(f'Here is ${change} in change')
            print('Here is your espresso')
            w=w-MENU["espresso"]["ingredients"]["water"]
            c=c-MENU["espresso"]["ingredients"]["coffee"]
            money=money+MENU["espresso"]['cost']
            break
        else:
            deficit=MENU["espresso"]['cost'] - tot_dol
            print(f'You have a deficit of {deficit}')
            continue
  elif i == "latte":
      while (True):
          print("Please insert coins.")
          qt = float(input("How many quarters?: "))
          dm = float(input("How many dimes?: "))
          nk = float(input("How many nickels?: "))
          pen = float(input("How many pennies?: "))
          tot_dol = (qt * 0.25) + (dm * 0.10) + (nk * 0.05) + (pen * 0.01) + tot_dol
          if tot_dol >= MENU["latte"]['cost']:
              change = tot_dol - MENU["latte"]['cost']
              print(f'Here is ${change} in change')
              print('Here is your latte')
              w = w - MENU["latte"]["ingredients"]["water"]
              c = c - MENU["latte"]["ingredients"]["coffee"]
              m = m - MENU["latte"]["ingredients"]["milk"]
              money = money + MENU["latte"]['cost']
              break
          else:
              deficit = MENU["latte"]['cost'] - tot_dol
              print(f'You have a deficit of {deficit}')
              continue
print("Coffee machine needs a refill")


