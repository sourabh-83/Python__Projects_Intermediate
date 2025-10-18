'''from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.forward(100)
timmy.color("red")
my_screen=Screen()
print(my_screen)
my_screen.exitonclick()'''

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["name","age"]
table.add_row(["a", 23])
print(table)