# Project: Discount Calculator (Python)

## Description

A small command-line program that computes a final price after applying a discount.
If the discount percentage is 20% or more, the discount is applied; otherwise, the original price is returned unchanged.

## Functionality
```python 
calculate_discount(price, discount_percent):
If discount_percent >= 20: returns price * (1 - discount_percent / 100)
Else: returns price
```
## Interactive CLI:
Prompts user to enter the original price
Prompts user to enter the discount percentage
Computes and prints the final price
Usage

## Run the script.
Input the price as an integer when prompted.
Input the discount percentage as an integer when prompted.
The program prints the final price after applying the discount (if applicable).

## Notes

The code uses integer inputs for price and discount_percent, but the calculation yields a float when discount_percent is not a multiple of 100.
If you want to always round to two decimals, consider:
final_price = round(calculate_discount(price, discount_percent), 2)

## Dependencies

Python 3.x

## License

MIT 
