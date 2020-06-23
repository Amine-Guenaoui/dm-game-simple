from efficient_apriori import apriori
from itertools import combinations


class apriori_items_generator:

    def __init__(self):
        self.items = items = [
            ["milk",
             "cheese",
             "eggs",
             "yogurt",
             "butter",
             "salt"
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
             "water",
             "pineapple"]
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
        l += self.rSubset(self.items[0], 5)
        l += self.rSubset(self.items[1], 5)
        l += self.rSubset(self.items[2], 5)
        l += self.rSubset(self.items[3], 5)
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

    def print_rules(self):
        line = 1
        for i in rules:
            # print(i)
            # print(i.__dict__)
            #print(str(i.lhs) + " =>" + str(i.rhs))
            for j in i.lhs:
                print(j, end=" ")
            print("", end=" => ")
            for j in i.rhs:
                print(j, end=" ")
            print(line)
            line += 1
            # print(k)
            # print()


application = apriori_items_generator()
application.show_rules()

rules = application.get_rules()
application.print_rules()

# print(rules)
