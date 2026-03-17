class Base:
    def greet(self):
        print("Hello from Base")

# Derived Class inherited Base
class Derived(Base):
    pass

b = Base()
d = Derived()

b.greet()  # Hello from Base
d.greet()  # Hello from Base (inherited!)