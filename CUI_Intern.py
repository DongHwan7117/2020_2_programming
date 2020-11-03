dsdsd
IS it Okay?

class three(cryptography):
    def return_value(self):
         self.value= self.number**3
         return self.value

class four(cryptography):
    def return_value(self):
          self.value= self.number**4
          return self.value
class five(cryptography):
    def return_value(self):
          self.value= self.number**5
          return self.value

class six(cryptography):
    def return_value(self):
          self.value= self.number**6
          return self.value

class seven(cryptography):
    def return_value(self):
          self.value= self.number**7
          return self.value

class eight(cryptography):
    def return_value(self):
          self.value= self.number**8
          return self.value

class nine(cryptography):
    def return_value(self):
          self.value= self.number**9
          return self.value



key=[]
changer=[]
for i in range(10) :
    key.append(randint(1,9))
    changer.append(randint(1,9))


value=0

for i in range(10) :
    if changer[i] == 1:
        value=value+one(key[i]).return_value()
    elif changer[i] == 2:
        value=value+two(key[i]).return_value()
    elif changer[i] == 3:
        value=value+three(key[i]).return_value()
    elif changer[i] == 4:
        value=value+four(key[i]).return_value()
    elif changer[i] == 5:
        value=value+five(key[i]).return_value()
    elif changer[i] == 6:
        value=value+six(key[i]).return_value()
    elif changer[i] == 7:
        value=value+seven(key[i]).return_value()
    elif changer[i] == 8:
        value=value+eight(key[i]).return_value()
    elif changer[i] == 9:
        value=value+nine(key[i]).return_value()

print(value)

for i in key:
    print(i, end="")

print("")
for i in changer:
    print(i, end="")
















