import webbrowser
from tkinter import *


class makera():


    
    
    def windowa(self):
        
        root = Tk()

        root.geometry('400x200')

        self.entry1 = Entry(root, width=20)

        self.entry1.pack()

        label1 = Label(root,text="Enter what you would like your page to say!").pack()

        
        b1 = Button(root,text="Start", command=self.htmlb)
        
        b1.pack()


        


        




    def htmlb(self):

        custom_text = self.entry1.get()

        print(custom_text)
        
        x = open("autohtml.html","w")

                       
        b = """</h1></body>
            </html>"""

        w = ("""<!DOCTYPE>
        <html>
        <head></head>
        <body><h1>"""+custom_text+b)
                        

        x.write(w)

        url = "file:///Users/slims/Documents/python_projects/" + "autohtml.html"
                        
                        
        webbrowser.open_new_tab(url)
        
        





if __name__ == '__main__':

    a = makera()
    a.windowa()
    

   
      
        
    



