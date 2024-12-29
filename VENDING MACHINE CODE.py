# Vending Machine code
#------------------------------------------------------------------------------------------------------------------------------------------------------------------  
# List of items in the vending machine
Vending_machine_items = {"Coca-Cola":"1A", "Pepsi":"1B", "Gatorade":"1C", "Sprite":"1D", "Red Bull":"1E",
                         "Doritos":"2A", "Snickers":"2B", "Cheetos":"2C", "Lays":"2D", "Pocky":"2E",
                         "Purell":"3A", "Tylenol":"3B", "Colgate":"3C", "Kleenex":"3D", "Disposable Mask":"3E"}
# Price
Vending_machine_prices = {
    "Coca-Cola": "$2.00", "Pepsi": "$1.50", "Gatorade": "$2.50", "Sprite": "$1.50", "Red Bull": "$3.50",
    "Doritos": "$1.30", "Snickers": "$1.00", "Cheetos": "$1.25", "Lays": "$1.25", "Pocky": "$1.70",
    "Purell": "$2.70", "Tylenol": "$2.90", "Colgate": "$2.00", "Kleenex": "$1.60", "Disposable Mask": "$0.50"}
# The amount of items available in the vending machine
Vending_machine_stocks = {"Coca-Cola": 10, "Pepsi": 10, "Gatorade": 10, "Sprite": 10, "Red Bull": 10,
    "Doritos": 10, "Snickers": 15, "Cheetos": 10, "Lays": 10, "Pocky": 20,
    "Purell": 5, "Tylenol": 5, "Colgate": 10, "Kleenex": 5, "Disposable Mask": 20}
# Catergorize Items
Vending_machine_categories = {"Drinks": ["Coca-Cola", "Pepsi", "Gatorade", "Sprite", "Red Bull"],
                              "Snacks": ["Doritos", "Snickers", "Cheetos", "Lays", "Pocky"],
                              "Daily Essentials": ["Purell", "Tylenol", "Colgate", "Kleenax", "Disposable Mask"]}
#------------------------------------------------------------------------------------------------------------------------------------------------------------------  
#To display the list of items of the vending machine, prices & code
def displayItems():
    print("\nList of items\n")
    for item, code in Vending_machine_items.items():
        price = Vending_machine_prices.get(item)
        stocks = Vending_machine_stocks.get(item, 0)
        print(f"Item: {item}, Code: {code}, Price: {price}, Stocks: {stocks}")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------  
# this will calculate the total of the selected items
def Get_total(selected_items):
    total = 0
    # this will calculate the sum of the selected items
    for item in selected_items:
        price = Vending_machine_prices.get(item).strip("$") # .strip($) is a must as we only need numbers for calculations
        total += float(price)
    return total
#------------------------------------------------------------------------------------------------------------------------------------------------------------------  
# Recommend items based on user selection
def recommend_items(selected_items):
    # Determine the categories the user selected items from
    selected_categories = set()
    for item in selected_items:
        for category, items in Vending_machine_categories.items():
            if item in items:
                selected_categories.add(category)

    # Find a category not selected by the user
    unselected_categories = [
        category for category in Vending_machine_categories if category not in selected_categories
    ]

    # Recommend items from the first unselected category
    if unselected_categories:
        recommendation_category = unselected_categories[0]
        recommendations = Vending_machine_categories[recommendation_category][:3]  # Recommend up to 3 items
        print(f"\nYou might also like these items from {recommendation_category}: {', '.join(recommendations)}")
    else:
        print("\nThank you for your selection!")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# the main code for the vending machine to work
def Main_Code():
    while True:
        displayItems()  # To display the list of items of the vending machine, prices & code
        selected_items = [] # the list to store the selected items
        
        # loop that will allow user to select multiple items
        while True:
            code = input("\nEnter the item code to select the item(Enter 'done' to finish your selection): ")
            item = next((item for item, item_code in Vending_machine_items.items() if item_code == code),None)
            if code == 'done':
                break   # exiting the loop for selecting items
            elif item:
                if Vending_machine_stocks.get(item, 0) > 0: #checks stock items
                    selected_items.append(item) # Add selected items to the list(selection)
                    Vending_machine_stocks[item] -= 1 # Reduces the stock by 1
                    print(f"{item} has been added to you selection. Remaining stocks: {Vending_machine_stocks[item]}.")
                else:
                    print(f"Sorry, {item}, is out of stock")
            else:
                print("INVALID CODE")

        # If no items were selected cancel order & redirect it back to the menu
        if not selected_items:
            print("\nNo items were selected, Order cancelled,")
            continue

        # Display the user selected items and their total sum
        print("\nItems selected")
        for item in selected_items:
            print(f"{item} - {Vending_machine_prices[item]}")
        
        Total_amount = Get_total(selected_items)
        print(f"Total Amount: ${Total_amount:.2f}")

        # Provide recommendations
        recommend_items(selected_items)

        # If the user wants to cancel order midway or if user doesn't want the selected items
        Confirm = input("Proceed with order? (Yes/No): ")
        if Confirm != 'Yes':
            print("\nOrder cancelled")
            for item in selected_items:
                Vending_machine_stocks[item] += 1 # this will bring back the items selected back
            continue


        #Payment
        while True:

            try:
                #user input money
                payment = float(input(f"Enter payment amount (total: ${Total_amount:.2f}): "))
                if payment < Total_amount:
                    print("Insufficent")
                else:
                    change = payment - Total_amount
                    print(f"Payment successful\nChange: ${change:.2f}")
                    break
            except:
                #if payment is invalid
                print("Invalid Input, Try again")        
        order_again = input("Do you want to order again? (Yes/No): ")
        if order_again != "Yes":
            print("Thanks for you purchase!")
            break # To end the loop
#Run the program
Main_Code()





