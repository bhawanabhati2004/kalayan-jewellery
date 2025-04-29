# TASK 3 : mini project : 

# KALYAN JWELLERS : 

# M 
# >  65
# purchase > 2lk - 3lk    20% 
# purchase > 3lk - 5lk 	30% 
# purchase > 5lk  	35% 


# <65
# purchase > 2lk - 3lk    10% 
# purchase > 3lk - 5lk 	20% 
# purchase > 5lk  	25% 



# F
# >  65
# purchase > 2lk - 3lk    25% 
# purchase > 3lk - 5lk 	35% 
# purchase > 5lk  	40% 


# <65
# purchase > 2lk - 3lk    15% 
# purchase > 3lk - 5lk 	25% 
# purchase > 5lk  	30% 


# ------------------------------------------------------------
# Enter your name : 
# Enter gender : 
# Enter age : 

# Enter product : Ring 
# Enter product gram : 20  
# current gold price (1 grm) : 5752

# -------------------------------------
# TOTAL GOLD RATE :  XXXXX 


# Making charges (1 gram)  : 845
# Total Making CHarges :    TOTAL GOLD  X  MAKING CHARGES 

# ---------------------------------------
# TOTAL AMOUNT : GOLD PRICE + TOTAL MAKING CHARG



# DISCOUNT :   25 (AUTOMATIC) 
# DIS- AMOUNT : except (making charges) 
# -----------------------------------------
# total net amount : 

# --------------------------------------------
# HINT : variables , input , conditional statements 

# --------------------------------------------------------------------------------

name=str(input("enter the any name:"))
gender=str(input("enter the gender (M/F):"))
age=int(input("enter the age:"))
product=str(input("enter the product:"))
product_gram=int(input("enter the product gram:"))
gold_price=int(input("enter the price:"))
total_gold_price =gold_price*product_gram
making_charges=845
total_making_charges=product_gram*making_charges

if gender=="M":
    if age>=65:
        if total_gold_price>=21000 and total_gold_price<31000:
            discount =20

        elif total_gold_price>=31000 and total_gold_price<51000:
            discount =30

        elif total_gold_price>=51000:
            discount=35

    elif age<65:
        if total_gold_price>=21000 and total_gold_price<31000:
            discount=10

        elif total_gold_price>=31000 and total_gold_price<51000:
            discount=20

        elif total_gold_price>=51000:
            discount=25

elif gender=="F":
    if age>=65:
        if total_gold_price>=21000 and total_gold_price<31000:
            discount=25

        elif total_gold_price>=31000 and total_gold_price<51000:
            discount=35

        elif total_gold_price>=51000:
            discount=40
    elif age<65:
        if total_gold_price>=21000 and total_gold_price<31000:
            discount=15

        elif total_gold_price>=31000 and total_gold_price<51000:
            discount=25

        elif total_gold_price>=51000:
            discount=30

dis_price =total_gold_price*discount/100
after_dis_amount =total_gold_price-dis_price
net_amount=after_dis_amount+total_making_charges
print(f"""_____________________Kalyan jwellers_________________________
      _____________________________Tax invoice _________________________
      name: {name}
        age:   {age}
        gender  {gender}
        product {product}
        weight  {product_gram}
        _________________________________________________________________
        total gold price {total_gold_price}
        discount ={discount}
        dis price={dis_price}
        making charges per gram={making_charges}
        _________________________________________________________________
        net amount ={net_amount}
         __________________________________________________________________
         have a nice day
        """)


  

   


















