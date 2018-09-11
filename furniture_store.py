#adding the store "Lovely Loveseat" description
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or White."

#Create a price for the loveseat
lovely_loveseat_price = 254.00

#Add to inventory characteristic piece of furniture
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches highx 54.75 inches wide x 28 inches deep. Black."

#create price for the stylish settee
stylish_settee_price = 180.50

#Creatign another item and its price
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

#Creating sales tax
sales_tax = 0.088

#Creating a tally for the first customer
customer_one_total = 0

#Description of things purchased
customer_one_itemization =""

#customer purchase
customer_one_total += lovely_loveseat_price

#Description added to customer purchase
customer_one_itemization += lovely_loveseat_description

#adding luxurious lamp purchase
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#Calculating sales tax
customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

#Printing up receipt
print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)

#Creating tally for the second customer
customer_two_total = 0
customer_two_itemization = ""

#Customer purchase
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description

#purchase of luxurious lamp
customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description

#Calculating sales tax for customer two
customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

#Printing up receipt for customer two
print("Customer Two Items: ")
print(customer_two_itemization)
print("Customer Two Total: ")
print(customer_two_total)
