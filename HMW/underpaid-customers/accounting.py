melon_cost = 1.00

payment_data = open("customer-orders.txt")      #opens the file 


def check_paid_status(payment_data):
    """ Function goes through each line of the file, calculates the cost of melons and determines if the customer underpaid/overpaid for melons"""

    for line in payment_data:                       #Iterates over each line in the file
        parsed_data = line.split("|")               #splits the data into a list(the point of splitting is "|")
        full_name = parsed_data[1]                  #Assign the 1st index value in the list to full name
        first_name = full_name.split(" ")[0]
        print(first_name)

        melon_quantity = float(parsed_data[2])      #Assign the 2nd index value in the list to the # of melon purchased 
        price_paid = float(parsed_data[3])          #Assign the 3rd index value in the list to the amount paid by the customers
        expected_price = melon_cost * melon_quantity#Calculate the expected price of customers orders
        
        #print out the general statement, checks if everything works so far
        print(f"{full_name} purchased {melon_quantity} melons and paid {price_paid}. They were expected to pay {expected_price}")

        if price_paid < expected_price:
            print(f"{full_name} has underpaid for their melons")
        elif price_paid > expected_price:
            print(f"{full_name} has overpaid for their melons") 

    payment_data.close()


check_paid_status(payment_data)






# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
