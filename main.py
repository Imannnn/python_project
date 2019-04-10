from app_lib.crime_items_manager import BudgetItem

budget = BudgetItem() # s budget is an instance of BudgetItem
budget.add_budget_item("Cornflakes", 7000)
budget.add_budget_item("Nutrigrain bar", 0.25)

budget.save_budget_items()
