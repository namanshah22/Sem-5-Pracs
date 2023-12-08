class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Creating an instance of Person
p1 = Person('Naman', 'Shah')
p1.printname()

print("Modification")
p1.firstname = 'Kamlesh'
p1.printname()

print("Deletion:")
del p1  
p1.printname()  


