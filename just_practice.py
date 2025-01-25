# class creation 
class musapeace:
    def __init__ (self, name):
        self.name = name
    
    def musa_name(self):
        return "muhammad mubarak musa"
    
    def musa_name2(self):
        return "muhammad musa"

musapeace1 = musapeace("muhammad")   
musapeace2 = musapeace("mubarak")
    
    # accessing object   
print(f"{musapeace1.name} is also {musapeace1.musa_name()}")
print(f"{musapeace2.name} ca also be call {musapeace2.musa_name2()}")
