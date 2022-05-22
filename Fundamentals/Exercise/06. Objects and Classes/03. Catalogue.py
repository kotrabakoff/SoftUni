class Catalogue:
    products = []
    def __init__(self, name):
        self.name = name

    def add_product(self,product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):

        new_list = []
        for i in self.products:
            if i[0] == first_letter:
                new_list.append(i)

        return new_list

    def __repr__(self):
        nl = "\n"
        return f"Items in the {self.name} catalogue:{nl}{nl.join(sorted(self.products))}"

# Example:

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

