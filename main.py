# import another_module
#
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("orange")
# timmy.forward(300)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()


table.field_names = ["poketmon name", "type"]
table.add_row(["pikachu", "electric"])
table.add_row(["squrtle", "water"])
table.add_row(["charmander", "fire"])

print(table)
