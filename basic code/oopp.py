# class Factory:         #this is class
#     a = 15
#     b = 20  # attribut

#     def machine_circal(self):  # method
#         print("helo this run by funtion")

#     print("helo ji kese ho")

# print(Factory().a)
# Factory().machine_circal()

# obj = Factory()  # iska matalab h jo bhi chije factory class m h vo sab ab obj m chali gai
# print(obj.a)
# obj.show()

# ------------------------ example --------------------------
class Four_wheelar:
    def __init__ (self,CarName, Door, Color):
        self.CarName = CarName
        self.Door = Door
        self.Color = Color

    def show(self):
        print(f"The name of car is {self.CarName}, that have a {self.Door} Door, and color is {self.Color} ")

Tata = Four_wheelar("Nano", 4, "White")
Rolls_Royal = Four_wheelar("Chiron", 2, "Nevy Blue")
Honda = Four_wheelar("Aura", 4, "Black")

Tata.show()
# ------------------------ example --------------------------






