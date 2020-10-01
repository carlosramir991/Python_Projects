class sports:
    sport = "Basketball"
    stadium = "Madison Square Garden"
    team = "Bulls"
    
    def part(self):
        pname = input("What is your name?")
        exp = input("how man years of experience do you have?")
        print("{}, you will be playing {} with the {} in {}. It's great that you have {} of experience.".format(pname,self.sport,self.team,self.stadium,exp))



class baseball(sports):
        sport = "Baseball"
        city = "San Diego" 
        wins = 12

        def part(self):
            print("It's great that you've decided to join our team at the {} Field! We have had {} wins so far!".format(self.city,self.wins))





class soccer(sports):
        sport = "Soccer"
        field = "Sacramento Field"
        loses = 1

        def part(self):
            print("Please join us at the {} for practice at 7:00 pm. We have lost \n{} time this season.".format(self.field,self.loses))
    

if __name__ == "__main__":
     b = baseball()
     s = soccer()

     b.part()
     s.part()


    
    
 
        
        






    
