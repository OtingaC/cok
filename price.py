def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percentage: "))

#Final price
final_price = calculate_discount(price, discount_percent)

print(f"Final price: {final_price}")
