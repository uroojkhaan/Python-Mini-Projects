# Shopping discount calculator - Conditions (PKR)

# A warm welcome for user :
print("                                      ")
print("Welcome to our  Mart Billing Counter !")
print("                                      ")
print("Get the best discounts on your shopping today ! ")
print("-" * 50 )

# Taking User Input / total bill :
total_bill = int(input("Enter Your Total Bill Amount : \n "))

# Asking the user for payment method :
payment_method = input(" Enter your payment method : \n (Cash / Credit Card or Debit Card )").strip().lower()

# Discount Conditions :
discount = 0
if total_bill <= 10000 :
    discount = total_bill * 0.10
elif total_bill <= 20000 :
    discount = total_bill * 0.20
elif total_bill <= 50000 :
    discount = total_bill * 0.30
else :
    print(" No Discount")

# Final Bill
Final_Bill = total_bill - discount
print(f" Your Total Bill After discount is {Final_Bill} ")


gst = 0 # Default value

# Additional charges (for Card Payments ):
if payment_method.strip().lower() in ["credit card" , "debit card"] :
    print(" GST condition triggered ! ")
# Assuming 5% GST
    gst = Final_Bill * 0.05
    print(f"GST Applied (5%) : {gst} PKR")
    print(f"Total Payable Amount After GST : {Final_Bill + gst} PKR")

print("=" * 40 )
print("\n Thank you for shopping with us ! Have a great day ! :)")
