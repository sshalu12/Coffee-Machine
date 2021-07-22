MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


    


def report():
  for key,value in resources.items():
    print(f"{key}: {value}ml ")

def check(a,resources,MENU):
  if resources["water"]>MENU[a]["ingredients"]["water"] :
    
    if resources["milk"]>MENU[a]["ingredients"]["milk"] :
      
      if resources["coffee"]>MENU[a]["ingredients"]["coffee"] :
        
        resources["water"] -=MENU[a]["ingredients"]["water"]
        
        resources["milk"] -=MENU[a]["ingredients"]["milk"]
        
        resources["coffee"] -= MENU[a]["ingredients"]["coffee"]
        return 1

      else:
        print("Sorry there is not enough coffee.🙂")
        return 0
    else:
      print("Sorry there is not enough Milk.🙂")
      return 0
  
  else:
    print("Sorry there is not enough water.🙂")
    return 0

def cost(q,d,n,p):
  c=0.25*q + 0.1*d + 0.05*n + 0.01*p 
  return c

def cost_check(total_cost,MENU,a):
  if total_cost >= MENU[a]["cost"]:
    change=total_cost-MENU[a]["cost"]
    print(f"Here is ${round(change,2)} in change.")
    return change
  else:
    print("Sorry that's not enough money. Money Refunded")
    return 0

end=True
money=0
while end:
  a=input("What would you like? (espresso,cappuccino,latte)☕: ").lower()

  if a=="report":
    report()
    print(f"Money: ${money}")    

  elif a=="off":
    end=False
  elif a=="espresso" or "cappuccino" or "latte":
    b=check(a,resources,MENU)
    if(b==1):
      print("Please insert coins. ")
      q=int(input("how many quarters?: "))
      d=int(input("how many dimes?: "))
      n=int(input("how many nickles?: "))
      p=int(input("how many pennies?: "))
      total_cost=cost(q,d,n,p)
      m=cost_check(total_cost, MENU, a)
      if (m==0):
        end=True
      else:
        print(f"Here is your {a} ☕  Enjoy!")
        money +=MENU[a]["cost"]
    else:
      end=False
  
 