menue_dict={'Pizza':200,'Pasta':120,'Tea':25,'Cofee':80,'Momos':110,'LemonJuice':30,'FrenchFries':60,}

print("Welcome To Our resturent\n")
print("Menue\n")
print("Pizza:200,\nPasta:120,\nTea:25,\nCoffe:80,\nMomos:110,\nLemonJuice:30,\nFrenchFries:60")


#total
order_total=0

#inputting 1st item
item1=input("enter a food to buy = ")

#checking if item is presnt in menue or not 
if item1 in menue_dict:
   order_total += menue_dict[item1]
   print(f"you order {item1} has been added to bill ") 
else:
   print(f"{item1} is not available in our resturent ")
   exit()


another_order=input("do you want to buy something more(Y/N)")


if another_order == "Y":
    item2=input("enter your second item ")
    if item2 in menue_dict:
       order_total += menue_dict[item2]
       print(f"your bill is ={order_total}")
    else:
       print(f"item not avilable , your bill={order_total}")
else:
   print(f"your total ={order_total}")
      
