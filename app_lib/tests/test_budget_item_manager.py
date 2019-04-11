from app_lib.accidents_items_manager import BudgetItem
class TestBudgetItemManager:
    budget_item_manager = BudgetItem()

    def test_items_empty_on_initialisation(self):
        assert bool(self.budget_item_manager.budget_item) is False

    def test_add_to_budget_list(self):