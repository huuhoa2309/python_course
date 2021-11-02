class Persion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print('my name is %s, age is %d' % (self.name, self.age))
p=Persion('Hoa', 19)
p.say()