class User:

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def getfirst_name(self):
        print("меня зовут ", self.first_name)

    def getlast_name(self):
        print("моя фамилия ", self.last_name)
       
    def get_full_name(self):
        print(f"name: {self.first_name} {self.last_name}")
