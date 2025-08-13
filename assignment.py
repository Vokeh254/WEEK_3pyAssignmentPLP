def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price
    
price = int(input("Enter original price: "))
discount_percent = int(input("Enter discount percentage: "))
final_price = calculate_discount(price, discount_percent)
print("Final price after discount:", final_price)