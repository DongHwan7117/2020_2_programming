class Airplane:
    def __init__(self, name):
        self.name = name
    
    def get_info(self):
        print (self.name)

class Zet(Airplane):
    def get_info(self):
        print (self.name, 'Velcity: Upper than Mach')

        
class Boeing707(Airplane):
    def get_info(self):
        print (self.name, 'Velocity: Lower than Mach')

zetairplane = Zet('dave')
Boeing = Boeing707('david')
print (zetairplane.get_info(), Boeing.get_info())