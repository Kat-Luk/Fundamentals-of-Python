from car import Car
car1 = Car("101","Volkswagen Golf",25000,"available")
car2 = Car("102","BMW M3",60000,"available")
print("Current cars for sale:")
car1.introduce()
car2.introduce()
ID = input("Enter the ID of the car you want to mark as sold:")
if ID == "101":
    car1.mark_as_sold()
    car2.introduce()
elif ID == "102":
    car1.introduce()
    car2.mark_as_sold()
    
