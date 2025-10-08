

from turtle import Turtle, Screen

# joe = Turtle()
# joe.shape("turtle")
# joe.color('DarkCyan')
# joe.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable() # This instances an object: constructor 
table.field_names = ['Breed', 'Dog Name', 'Weight (Kgs)']
table.add_rows([ # With the methods, I can modify the object
    ['Zaguate', 'Nacho', 26],
    ['Australian Cattledog', 'Eros', 25]
    ])
table.align = "l"   
'''
With the align attribute, I can change the global alignment setting of all columns in the table 
'''
table.border = True
table.header_style = 'upper'

print(table)


table2 = PrettyTable()
table2.add_column("Pokemon", ["Pikachu", "Charmander"], align="l", valign="m")
table2.add_column("Type", ["Electric", "Fire"], align="r")
'''
If I declare the alignment inside the add_column() method,
it will apply only to that specific column, not to the others.
'''
table2.header_style = 'lower'
print(table2)




'''
In these 2 cases, I created 2 objects from the PrettyTable() class.
Calling PrettyTable() invokes the constructor (__init__) of the class,
which initializes the object.
With the methods, I was able to add columns and/or rows to that object.
'''
print(type(PrettyTable()))

