class Player:
    def __init__(self, name, level):
        self.__name = name
        self.__level = level
    def GetLevel(self):
        return self.__level
    def SetLevel(self, new_level):
        if new_level > 0 and new_level <= 10:
            self.__level = new_level
            return True
        return False
me = Player("me", 0)
print(me.SetLevel(7))
print(me.GetLevel())

player = [None] * 3
player[0] = Player("a", 1)
player[1] = Player("b", 2)
player[2] = Player("c", 3)
for i in range(3):
    print(player[i].GetLevel())