class vehicle:
    make = "Scion"
    model = "Tc"
    year = 2006

class person(vehicle):
    name = "Carlos Ramirez"
    country = "The United States"

def disp():
    print("The user {} born in {} and has a {} model {} \nmanufactured in {}".format(person.name,person.country,vehicle.make,vehicle.model,vehicle.year))
    
    

    


    
if __name__ == "__main__":
    disp()
    
