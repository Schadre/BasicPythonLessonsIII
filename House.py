def thisHouse():
    response = input("What is the length? ")
    response2 = input("What is the Width? ")
    area = int(response) * int(response2)
    return area
print(thisHouse())
