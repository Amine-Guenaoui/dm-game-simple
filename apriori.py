from efficient_apriori import apriori
from itertools import combinations


class apriori_items_generator:

    def __init__(self):
        self.items = items = [
            ["milk",
             "cheese",
             "eggs",
             "yougurt",
             "butter"
             ],
            ["onions",
             "garlic",
             "sugar",
             "honey"],
            ["potato",
             "tomato",
             "bread"],
            ["orange",
             "apple",
             "water"]
        ]
        self.transactions = self.generate_items()
        self.itemsets, self.rules = self.generate_rules()

    def rSubset(self, arr, r):
        # return list of all subsets of length r
        # to deal with duplicate subsets use
        # set(list(combinations(arr, r)))
        return list(combinations(arr, r))

    def generate_items(self):
        l = []
        l += self.rSubset(self.items[0], 4)
        l += self.rSubset(self.items[1], 4)
        l += self.rSubset(self.items[2], 4)
        l += self.rSubset(self.items[3], 4)
        return l

    def show_rules(self):
        x = 0
        for i in self.transactions:
            x += len(i)

        print("number of generated rules :"+str(len(self.rules)))
        for i in self.rules:
            print(i)
        print("number of transactions is "+str(x))

    def generate_rules(self):
        itemsets, rules = apriori(self.transactions, min_support=0.2,
                                  min_confidence=0.5, max_length=13)
        return itemsets, rules

    def get_rules(self):
        return self.rules

    pass


application = apriori_items_generator()
application.show_rules()

rules = application.get_rules()

print(rules)
