# method overloading and method overriding

# method overloading
class MultiAdd:
    # 2
    def add(self, *args):
        total = 0
        for e in args:
            total += e
        return total
    def add(self, *args):
        total = 0
        for e in args:
            total += e
        return total

# obj
o = MultiAdd()

print(o.add(2, 3))
print(o.add(2, 3, 4))









# method overriding
class Father:
    # sleep
    def sleep(self):
        print("sleeps at 10pm and wakes up at 5am")
    def eat(self):
        print("eating")

class Son(Father):
    # def sleep(self):
    #     print("sleeps at 2am and wakes up at 10am")
    pass


# create and obj based on child
talha = Son()

talha.sleep()



