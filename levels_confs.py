import items_file
import game


# functions
def show_choices(transaction, items, level, num):
    wrong_answers = []
    right_answers = []
    posxr1 = int(game.width/2) + items_file.item_width * 2
    posxr2 = int(game.width/2) + items_file.item_width * 4
    posxl1 = int(game.width/2) - items_file.item_width * 4
    posxl2 = int(game.width/2) - items_file.item_width * 2
    posy = game.height/2 - items_file.item_height
    #print("showing choices ")
    if level == 1:  # show two choices with score of 3
        # setting the right answers

        posy = game.height/2 - items_file.item_height
        if num > 50:
            game.get_item(game.items_names[0], items,
                          posxr1, posy)  # wrong answer
            game.get_item(transaction.rhs[0], items, posxl1, posy)
            #print("right ones  ")
            # the left are wrong and right ones are right
            wrong_answers = [1, 2, 3]
            right_answers = [4, 5, 6]
        else:
            game.get_item(transaction.rhs[0], items, posxl1, posy)
            game.get_item(game.items_names[0], items, posxr1, posy)
            #print("left ones  ")
            right_answers = [3, 2, 1]
            wrong_answers = [4, 5, 6]
    if level == 2:

        if num < 25:
            game.get_item(transaction.rhs[0], items,
                          posxl1, posy)  # wrong answer
            game.get_item(game.items_names[0], items, posxr2, posy)
            game.get_item(transaction.rhs[1], items,
                          posxr2, posy + items_file.item_height)  # wrong answer
            game.get_item(game.items_names[1], items, posxr2,
                          posy + items_file.item_height)
            right_answers = [2, 4]
            wrong_answers = [3, 5, 6, 1]
        elif num > 25 and num < 50:
            game.get_item(game.items_names[0], items,
                          posxl1, posy)  # wrong answer
            game.get_item(transaction.rhs[0], items, posxr2,
                          posy + items_file.item_height)
            game.get_item(transaction.rhs[1], items,
                          posxr2, posy)  # wrong answer
            game.get_item(game.items_names[1], items, posxr2,
                          posy + items_file.item_height)
            right_answers = [3, 4]
            wrong_answers = [2, 5, 6, 1]

        elif num > 50 and num < 75:
            game.get_item(game.items_names[0], items,
                          posxl1, posy)  # wrong answer
            game.get_item(transaction.rhs[0], items, posxr2,
                          posy + items_file.item_height)
            game.get_item(game.items_names[0], items,
                          posxr2, posy)  # wrong answer
            game.get_item(transaction.rhs[1], items, posxr2,
                          posy + items_file.item_height)
            right_answers = [3, 5]
            wrong_answers = [2, 4, 6, 1]

        elif num > 75:
            game.get_item(game.items_names[0], items,
                          posxl1, posy)  # wrong answer
            game.get_item(game.items_names[1], items, posxr2,
                          posy + items_file.item_height)
            game.get_item(transaction.rhs[0], items,
                          posxr2, posy)  # wrong answer
            game.get_item(transaction.rhs[1], items, posxr2,
                          posy + items_file.item_height)
            right_answers = [4, 5]
            wrong_answers = [2, 3, 6, 1]

    return wrong_answers, right_answers
