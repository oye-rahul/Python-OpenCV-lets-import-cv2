productDetailqty = []
GrandT = 0
quityT = 0
bill = []
while True:
    item = input("item name: ")
    qty = int(input("Qty: "))
    price = int(input("Price: "))

    total = qty * price
    GrandT += total
    quityT += qty


    bill.append([item,qty,price,total])

    # productDetailqty.append(qty)
    stop = input("Add more item ? 'yes,no'.")

    if stop == "no":
        break

#print(bill) #[['mm', 5, 5, 25], ['pp', 55, 5, 275]]
print("\n-----------D-mart-----------")
print("item\tQty\tPrice\tTotal")
for i in bill:
    print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t")
print("------------------------------")
print(f"\t{quityT}\t\t{GrandT}")
print("------------------------------")



# print(f"{item} = {qty} x {price} = {total}")
# print("grand total =", gt)
# print("qty total =", qt)
# print("Item", " Qty", " Price")
# print("--------------------------")
# print(item," ", qty," ",price, " = ", total)