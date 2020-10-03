class calories:

    def maint(self,calories):
        print("Your maintenance calories today will be {}!".format(calories))

    def lose(self,calories):
        calories = (calories -250)
        print("In order to lose weight you need to eat {} calories!".format(calories))

        
obj = calories()
obj.maint(2000)
obj.lose(2000)
