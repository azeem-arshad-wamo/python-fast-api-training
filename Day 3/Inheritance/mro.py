# Whenever python has to resolve inheritanes.
# It creates the hierarchy into a linear order.
# It follows that order for everything. This order is called mro
# Python internally changes it to something like this [D → B → C → A → object]
# Let's take an example

class A: 
    def speak(self):
        print("Speaking in A")

class B(A):
    def speak(self):
        print("Speaking in B")

class C(A): 
    def speak(self):
        print("Speaking in B")

class D(B, C): 
    pass

# We follow left to right rule. 
# D inherits B first and then C.

# So, if we were to make an object with D
d = D()
# and, we do d.speak()
d.speak()
# It will print "Speaking in B" because D inherts B first. 
# This is the the order python follows.
print(D.mro())