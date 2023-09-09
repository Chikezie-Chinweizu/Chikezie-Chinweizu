class footballer:

    def __init__(self, n,c,cl):
        self.name= n
        self.country= c
        self.club = cl

    def talk(self):
        print("Hi, i'm", self.name)

    def eligible(self):
        if self.country != "Europe":
            print("I do not play in Europe")
        else:
            print("I Play in Europe.")

obj1= footballer("Alexia", "Africa", "Eyimba")
obj2= footballer("Messi", "Europe", "Barcelona")
obj3= footballer("Kez", "America", "Miami")

obj1.talk()
obj1.eligible()

obj2.talk()
obj2.eligible()

obj3.talk()
obj3.eligible()
