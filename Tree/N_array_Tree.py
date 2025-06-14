
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        space = " " * self.get_level() * 3
        print(space, self.data)
        for child in self.children:
            child.print_tree()


if __name__ == "__main__":
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    cell_phone = TreeNode("Cell Phone")
    television = TreeNode("Television")

    root.add_child(child=laptop)
    root.add_child(child=cell_phone)
    root.add_child(child=television)

    mac_book = TreeNode("Mac Book")
    samsung_book = TreeNode("Samsung Laptop")
    hp_book = TreeNode("HP Laptop")

    laptop.add_child(child=mac_book)
    laptop.add_child(child=samsung_book)
    laptop.add_child(child=hp_book)

    iphone = TreeNode("I Phone")
    samsung_phone = TreeNode("Samsung S 25 Ultra")

    cell_phone.add_child(child=iphone)
    cell_phone.add_child(child=samsung_phone)

    lg_tv = TreeNode("LG TV")
    onida = TreeNode("Onida TV")

    television.add_child(child=lg_tv)
    television.add_child(child=onida)

    root.print_tree()