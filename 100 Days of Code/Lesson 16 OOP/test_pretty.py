from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Role"]
table.add_row(["Johel", "Team Coach"])
table.add_row(["Chattie", "Assistant 🤖"])

print(table)