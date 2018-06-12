class Person:
    '''Represents a person'''
    p
    def __init__(self,name):
        self.name=name
    def sayfuck(self):
        print('Hello,how fuck you?'+self.name)
    pass #空代码块
p=Person('你娘')
p.sayfuck()