# Step 1: Data Structure

'''
- Save each expense.
- Every expense has 3 data: concept (what we buy), price (cost), category (food, transport, hobbies)
- Using a dict for each expense within a list
'''

# Structure: list of dictionaries
# Each expense is a dict with 3 fields

expenses = []

'''
Example of the data

expenses = [
    {"concept": "coffe", "price": 2.50, "category": "fodd"},
    {"concept": "train", "price": 1.50, "category": "transport"},
    {"concept": "netflix", "price": 12.99, "category": "hobbie"},
]
'''

# Access to each data of the expense
# expenses[0]['concept'] > 'coffe'
# expenses[0]['price'] > '2.50'

# Step 2: Functions

'''
- Each function does one thing
- Modular design
'''

def show_menu():
    """Show available options"""
    print("")
    print("=" * 35)
    print("  GESTOR DE GASTOS PERSONALES")
    print("=" * 35)
    print("  1. Añadir gasto")
    print("  2. Ver todos los gastos")
    print("  3. Resumen por categoría")
    print("  4. Buscar gastos")
    print("  5. Salir")
    print("-" * 35)

def add_expenses(expenses):
    """Ask the expense to the user and add it to the list

    Args:
        data (_type_): _description_
    """

    concept = input("What did u bought? ")
    price = float(input("Price (€): "))

    print("Categories: food, transport, hobbie, home, other")

    category = input("Category: ").lower()

    expense = {
        "concept": concept,
        "price": price,
        "category": category
    }

    expenses.append(expense) # Add it to the list
    print(f"  [OK] Expense Registered: {concept} ({price:.2f}€)")


def show_expenses(expenses: list[dict]):
    """Review all the registered expenses

    Args:
        expenses (list[dict]): List of registered expenses
    """

    if len(expenses) == 0:
        print("No expenses registered yet")
        return

    print("")
    print(f"  {'#':<4}{'concept':<20}{'Price':<12}{'Category'}")
    print("  " + "-" * 50)

    total = 0
    for i in range(len(expenses)):
        g = expenses[i]

        print(f"  {i+1:<4}{g['concept']:<20}{g['price']:<12.2f}{g['category']}")
        total = total + g["price"]

    print("  " + "-" * 50)
    print(f"  TOTAL: {total:.2f}€ ({len(expenses)} expenses)")

def resume_categories(expenses: list[dict]):
    """Show the total balance per categorie

    Args:
        expenses (_type_): _description_
    """

    # cumulative by category

    categories = {}
    for expense in expenses:
        cat = expense['category']

        if cat in categories:
            categories[cat] = categories[cat] + expense['price']
        else:
            categories[cat] = expense['price']

    # Show resume
    print("")
    print("  === RESUMEN POR CATEGORÍA ===")

    total_general = 0
    for cat in categories:
        total_cat = categories[cat]
        total_general = total_general + total_cat
        print(f"  {cat:<15} {total_cat:>8.2f}€")

    print(f"  {'TOTAL':<15} {total_general:>8.2f}€")

def expenses_finder(expenses):
    """Search expenses by category or by lower price

    Args:
        expenses (_type_): _description_
    """

    print("  Buscar por: (1) categoría  (2) importe mínimo")
    option = input("  Opción: ")

    finds = []
    if option == "1":
        cat = input(" Qué categoría?").lower()

        for expense in expenses:
            if expense['category'] == cat:
                finds.append(expense)
    elif option == "2":
        minimum = float(input("  ¿Importe mínimo? (€): "))

        for expense in expenses:
            if expense['price'] > minimum:
                finds.append(expense)

    if len(finds) == 0:
        print("  No se encontraron gastos con esos criterios.")
    else:
        print(f"  Encontrados: {len(finds)} gastos")
        for g in finds:
            print(f"    - {g['concept']}: {g['price']:.2f}€ ({g['category']})")

# Step 3: Main Loop

'''
The heart of the program its a while loop that shows the menu which asks for an option and calls the corresponding function

- It repeats until the user requests the option "Exit"
- This pattern (menu + while + if/eli) its spine of thousand of Terminal programs
  
'''

# Main loop of the program
def menu(expenses):
    while True:
        show_menu()
        opcion = input("  Tu elección (1-5): ")

        if opcion == "1":
            add_expenses(expenses)
        elif opcion == "2":
            show_expenses(expenses)
        elif opcion == "3":
            resume_categories(expenses)
        elif opcion == "4":
            expenses_finder(expenses)
        elif opcion == "5":
            print("")
            print("  ¡Hasta luego! Tus gastos NO se guardan al cerrar.")
            print("  (En Python desde cero aprenderás a guardar en archivo)")
            break
        else:
            print("  [ERROR] Opción no válida. Elige entre 1 y 5.")


if __name__ == "__main__":
    menu([
    {"concept": "coffe", "price": 2.50, "category": "food"},
    {"concept": "train", "price": 1.50, "category": "transport"},
    {"concept": "netflix", "price": 12.99, "category": "hobbie"},
    ])