import json

def generate_report(data):
    # for the dictionary
    inventory = data
    #used as base value to calculate the total amount of stock
    total_number_of_items_in_stock = 0
    #used as based amount to figure out the highest price
    highest_price = 0
    #used to store any item that is out of stock
    out_of_stock = []
    #used for the individual elements in the dictionary
    for item in inventory:
        #used to stop repeating int(item["stock"])
        stock = int(item["stock"])
        #used to see if the price of the element is bigger then the current value of highest_price
        if int(item["price"]) > highest_price:
            # if it is bigger then highest price it replaces the current one and is used for the next iteration of highest price
            highest_price = int(item["price"])
        # if stock is equal to zero 
        if stock == 0:
            #adds the name of the item to the list of out_of_stock
            out_of_stock.append(item["name"])
    #used to calculate the overall amount of items they have in stock
    total_number_of_items_in_stock += stock
    #prints the report
    print(
        f"Inventory Report\n"
        f"total amount of stock:{total_number_of_items_in_stock}\n"  ,
        f"the most expensive item: £{highest_price}\n" ,
        f"the items out of stock: {out_of_stock} \n"
          )
    
# creates a function
def restock_item(data):
    #takes the dictionary and saves it as a local veriable
    inventory = data 
    #creates a loop
    while True:
        #allows for an error
        try:
            #asks user for an input and makes sure it is a integer
            entered_id = int(input("PLease Enter Product ID"))
            #if it works properly it will end the loop
            break
        #if it doesn't work and causes an error it allows the logic to continue 
        except ValueError:
            #tell the user that they entered the wrong data because they probable entered a string instead of an iniger 
            print("entered characters. needs to be numbers")
    # creates a boolon for later logic
    found_id = False
    # creates a loop for every element in inventory which is the dictionary 
    for item in inventory:
        #checks if the id entered by the user is an id for one of the elements in the dictionary
        if item["id"] == entered_id:
            #if it is it creates a boolon
            found_id = True
            # it then saves that element to a veriable called selected_item
            selected_item = item
            #and ends the loop early to save the system resources running through the rest of the elements
            break
    # if it ran throogh the for loop without finding the right id it prints an error and dosent allow the inventory to be changed 
    if found_id == False:
        print("Error: ID not found")
        return inventory
    # if it did find the correct id 
    elif found_id == True:
        #it creates a for loop
        while True:
            #which allows for an error 
            try:
                #asks for the amount of stock ordered
                amount = int(input("PLease Enter the amount of stock ordered"))
                #if their is no errors entered it will end the loop
                break
            #if their is an error it informs the user and explains why and the loop continues until the user enters the right data
            except ValueError:
                print("entered characters. needs to be numbers")
        #calculates the new amount of stock
        new_amount = int(selected_item["stock"]) + amount
        #assigns the new stock level to the element and updates the dictonary
        selected_item["stock"] = new_amount
        print(f"the new sock: {new_amount}")
        #returns the updated element
        return selected_item
# creates a function to load the original inventory.json data
def load_data():
    #opens the file 
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
            #if thier is no file it creates one
    except FileNotFoundError:
        print("Error: File Not found\n creating file")
        with open("inventory.json", "w") as f:
            json.dump([], f)
    #returns the data inside of the json file        
    return inventory_data

#saves sample to a new file called updated_inventory.json sample being the updated dictonary or original dictionary
def save_inventory(sample):
    with open("updated_inventory.json", "w") as fp:
        json.dump(sample, fp, indent=4)

#starts the program
if __name__ == "__main__":
    #loads the json's data to a veriable called inventory
    inventory = load_data()
    #uses the veraable inventory to generate the report 
    generate_report(inventory)
    #uses inventory to update the stock levels
    restock_item(inventory)
    #saves the inventory to the new file
    save_inventory(inventory)

