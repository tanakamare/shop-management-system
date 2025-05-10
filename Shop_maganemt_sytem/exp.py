print("WELCOME TO GREENVIEW SHOPPING CENTER")

items_list = []

def shop_management():
    while True: 
          
        item_name = input("\nEnter Item name: ")
        item_price = float(input("Item Price: R"))
        item_quantity = int(input("Item Quantity: "))
     
        total_price = item_quantity * item_price
    
    
        items_list.append({
            "name": item_name,
            "price": item_price,
            "quantity": item_quantity,
            "total": total_price
        
        })
        
        for item in items_list:
            
            print("\nItem\t\tQty\tPrice\tTotal")
            print("-----\t\t---\t-----\t-----")
            print(f"{item["name"][:15]}\t\t{item["quantity"]}\tR{item["price"]}\tR{item["total"]} ")
            print("--------------------------------------------")  
        
        again_items = input("\nDo you want to Add another Item(Yes/No): ").lower()
        if again_items != "yes":
            break
        
    payment_total = sum(item["total"] for item in items_list)
    
    while True:
        try:
           print(f"\nTotal Amount Due: R{payment_total:.2f}") 
           payment = float(input("Enter payment amount: R")) 
           
           if payment < payment_total:
                      less = payment_total - payment
                      print(f"sorry you're short with: R{less:.2f}") 
                      continue
           break
                 
               
        except ValueError:
            print("Please ender a number")
        
    if payment > payment_total:
        change = payment - payment_total
        print(f"Change: R{change:.2f}")
        
    print("\n======= GREENVIEW SHOPPING RECEIPT =======")
    print("--------------------------------------------")
    print("Item\t\tQty\tPrice\tTotal")
    print("-----\t\t---\t-----\t------------")
    for item in items_list:
        print(f"{item["name"][:15]}\t\t{item["quantity"]}\tR{item["price"]}\tR{item["total"]} ")
    print("--------------------------------------------")    
    print(f"SUB TOTAL:\t\t\tR{payment_total:.2f}")
    print(f"PAYMENT:\t\t\tR{payment:.2f}")
    if payment > payment_total:
            print(f"CHANGE:\t\t\t\tR{change:.2f}")
    print("--------------------------------------------")
    print("THANK YOU FOR SHOPPING WITH US!")
    print("============================================")  
    
         
shop_management()


