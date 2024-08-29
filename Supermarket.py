from datetime import datetime

name = input("enter your name:")
lists = '''
Rice   Rs 20/kg
Sugar  Rs 30/kg
Salt   Rs 20/kg
Oil    Rs 80/liter
Paneer Rs 110/kg
Maggi  Rs 50/kg
Boost  Rs 90/each
colgateRS 85/each
'''
price = 0
pricelist = []
totalprice = 0
Finalfinalprice = 0
ilist = []
qlist = []
plist = []

#rates for items
items={'rice':20,
'sugar':30,
'salt':20,
'Oil':80,
'paneer':110,
'maggi':50,
'boost':90,
'colgate':85}
option = int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item = input("enter required items:")
        quantity = int(input("enter quantity:"))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount = gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp = input("can i bill the items yes or no:")
    if inp == 'yes':
        pass
        if finalamount!=0:
            for i in range(len(pricelist)):
                print("\n\n",25*"=","Chaithanya supermarker",25*"=")
                print(28*" ","wanaparthy")
                print("Name:",name,30*" ","Date:",datetime.now())
                print(75*"-")
                print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
                for i in range(len(pricelist)):
                    print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
                print(75*"-")
                print(50*" ",'TotalAmount:','RS',totalprice)
                print("gst amount",40*" ",'Rs',gst)
                print(75*"-")
                print(50*" ",'finalAmount:','Rs',finalamount)
                print(50*"-")
                print(20*" ","Thanks for visiting")
                print(75*"-")
 
           
 """       #OUTPUT

enter your name: chaithanya
for list of items press 1: 1

Rice   Rs 20/kg
Sugar  Rs 30/kg
Salt   Rs 20/kg
Oil    Rs 80/liter
Paneer Rs 110/kg
Maggi  Rs 50/kg
Boost  Rs 90/each
colgateRS 85/each

if you want to buy press 1 or 2 for exit: 1
enter required items: rice
enter quantity: 5
can i bill the items yes or no: yes


 ========================= Chaithanya supermarker =========================
                             wanaparthy
Name: chaithanya                                Date: 2024-04-24 02:38:40.676610
---------------------------------------------------------------------------
sno          items          Quantity     price
0                rice     5          100
---------------------------------------------------------------------------
                                                   TotalAmount: RS 100
gst amount                                          Rs 5.0
---------------------------------------------------------------------------
                                                   finalAmount: Rs 105.0
--------------------------------------------------
                     Thanks for visiting
---------------------------------------------------------------------------
if you want to buy press 1 or 2 for exit: 2   ""'







