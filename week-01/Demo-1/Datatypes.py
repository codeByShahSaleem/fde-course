import math
#Task 01 Delivery Charge
LAMPS = 2400
Quantity = 3
TotalLampCharges = LAMPS * Quantity
DELIVERY_CHARGES = 350
TOTAL_COST = TotalLampCharges+DELIVERY_CHARGES
print(TOTAL_COST)

SubTotal = 7200
SaleTax = 18/100
TaxAmount = SaleTax * SubTotal
print("The Tax amount is :",TaxAmount)
print(type(TaxAmount))
#Due to division
##Splitting a bill
TotalBill = 4750
TotalFriends = 4
AmountPerPerson = TotalBill/TotalFriends
print("The Bill per perosn", AmountPerPerson)
AmountPerPerson = TotalBill//TotalFriends
print("The Bill per perosn after floor division", AmountPerPerson)
AmountPerPerson = TotalBill%AmountPerPerson
print("The Bill per perosn after using % division", AmountPerPerson)




#Discount and tax
PhoneTotalCost = 15000
Discount = 10/100
DiscountAmount = Discount * PhoneTotalCost
AfterDiscount = PhoneTotalCost-DiscountAmount
print("the phone discount amount", DiscountAmount)
print("The Phone Price After Discount:", AfterDiscount)
Tax=18/100
TaxAmount = Tax*AfterDiscount
print("The Tax Amount is:" ,TaxAmount)
Total = TaxAmount + AfterDiscount
print("the total amount after tax", Total)

#In other way Same question part B
PhoneCost = 15000
Discount = 18/100
DiscountedRate = Discount*PhoneCost
print("Discounted Amount:", DiscountedRate)
Phone_Remain_Amount = PhoneCost-DiscountedRate
print("after Discount", Phone_Remain_Amount)


TaxPercentage = 10/100
Tax_Amount = TaxPercentage * Phone_Remain_Amount

print("phone Tax Amount:", Tax_Amount)
totalPhoneCost = Phone_Remain_Amount + Tax_Amount
print ("The Phone Price after added Tax 10% is ", totalPhoneCost)

#Packing boxes
Total_Items = 23
BoxCapacity = 6
BoxNeeded = int(Total_Items/BoxCapacity)
print("The Number of Boxes Needed:", BoxNeeded)
ItemsLeft = Total_Items%BoxCapacity
print("The Number of Items left:",ItemsLeft)
TotalBoxNeeded = math.ceil(Total_Items/BoxCapacity)
print("The Number of Boxes needed with partially filled items", TotalBoxNeeded)

ShippingCost = 120
TotalShippingCost = ShippingCost * Total_Items
print("The total cost need to shift items:", TotalShippingCost)