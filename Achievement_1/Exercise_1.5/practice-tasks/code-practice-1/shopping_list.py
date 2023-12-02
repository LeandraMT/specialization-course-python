class ShoppingList(object):
    def __init__(self, list_name):
        shopping_list = []
        self.list_name = list_name
        self.shopping_list = shopping_list

    def add_item(self, item):
        self.item = item
        if item in self.shopping_list:
            print("Item is already in the shopping list")
        else:
            self.shopping_list.append(item)
            print("Item has been added to the shopping list")

    def remove_item(self, item):
        self.item = item
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print("Item has been removed from shopping list")
        else:
            print("Item is not in the shopping list")

    def view_list(self):
        print("Shopping list: ", self.shopping_list)
        for item in self.shopping_list:
            print(item)

    def merge_lists(self, obj):
        merged_lists_name = (
            "Merged List - " + str(self.list_name) + " + " + str(obj.list_name)
        )
        merged_lists_obj = ShoppingList(merged_lists_name)

        merged_lists_obj.shopping_list = self.shopping_list.copy()

        for item in obj.shopping_list:
            if not item in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(item)

        return merged_lists_obj
