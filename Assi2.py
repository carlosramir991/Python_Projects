class sports:
    name = "Basketball"
    field = "Madison Square Garden"
    tname = "Bulls"
    
    def part(self):
        pname = input("What is your name?")
        exp = input("how man years of experience do you have?")
        print("{}, you will be playing {} with the {} in {}. It's great that you have {} of experience.".format(pname,self.name,self.tname,self.field,exp))



class baseball(sports):
        name = "Baseball"
        field = "Madison Square Garden"
        tname = "Angels"

        def part(self):
            pname = input("What is your name?")
            exp = input("how man years of experience do you have?")
            print("{}, you will be playing {} with the {} in {}. It's great that you have {} of experience.".format(pname,self.name,self.tname,self.field,exp))





class soccer(sports):
        name = "Soccer"
        field = "Madison Square Garden"
        tname = "Chivas"

        def part(self):
            pname = input("What is your name?")
            exp = input("how man years of experience do you have?")
            print("{}, you will be playing {} with the {} in {}. It's great that you have {} of experience.".format(pname,self.name,self.tname,self.field,exp))
    

if __name__ == "__main__":
     b = baseball()
     s = soccer()

     b.part()
     s.part()


    
    
 
        
        






    
