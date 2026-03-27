from enum import Enum

# You can also restraint path parameters by making an class that inherts ENUM
class Dessert(str, Enum):
    cake = "cake"
    icecream = "ice cream"
    pie = "pie"

# This is an example from the docs
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"