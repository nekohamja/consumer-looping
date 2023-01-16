while True:
    cname = input("Consumer Name: ")
    id = input("Consumer ID: ")
    category = input("Consumer Category (Residential/Commercial): ")
    address = input("Consumer Address: ")
    present = float(input("Present Reading: "))
    previous = float(input("Previous Reading: "))
    crate = float(input("Current Amount Rate: "))
    ddate = str(input("Due Date: "))
    cmu = present - previous
    amount = cmu * crate
    ocr = amount * 0.23
    oc = cmu * ocr
    nbill = amount + oc
    print("\nConsumer Name: ", cname)
    print("Consumer ID: ", id)
    print("Consumer Category: ", category)
    print("Consumer Address: ", address)
    print("CMU: ", cmu)
    print("Net Bill: ", nbill)
    print("Other Charges: ", oc)
    print("Amount Due: ", amount)
    repeat = input("Anoter transaction? (y/n): ")
    if repeat == "n":
        break
    elif repeat == "y":
        continue