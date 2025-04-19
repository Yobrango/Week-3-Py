def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
        
    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        # Apply the discount if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

def main():
    # Prompt the user for inputs
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount = float(input("Enter the discount percentage: "))
        
        # Calculate the final price using the calculate_discount function
        final_price = calculate_discount(original_price, discount)
        
        # Display the results
        if discount >= 20:
            print(f"A {discount}% discount was applied.")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. The discount needs to be at least 20%.")
            print(f"Original price: ${final_price:.2f}")
            
    except ValueError:
        print("Please enter valid numerical values for price and discount.")

# Execute the program
if __name__ == "__main__":
    main()