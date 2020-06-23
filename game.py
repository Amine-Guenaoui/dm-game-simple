import pygame
import random
import characters_file
import items_file
import dialogues_file
from player import Player
from apriori import apriori_items_generator

# initializing
pygame.init()

# screen initializing
width, height = 1024, 768
screen = pygame.display.set_mode((width, height))

# title and icon
pygame.display.set_caption("Grocery Store")
# icon = pygame.image.load("icon.png")
# pygame.display.set_icon(icon)

# game required images -----------
# background
background = pygame.image.load('unnamed.jpg')  # 500x375
background = pygame.transform.scale(background, (width, height))
text_box = pygame.image.load("text_box.png")
text_box = pygame.transform.scale(text_box, (width+200, int(height/2)+200))

pygame.font.init()
font = pygame.font.SysFont("Arial", 32)
hint_font = pygame.font.SysFont("Arial", 16)
textX = -150
textY = 300
# game music
pygame.mixer.init()
background_music = pygame.mixer.music.load("Glimpse - Ambitions.mp3")
pygame.mixer.music.play(-1)

# buttons and interface texts
press_return = "press return to continue .. "
press_answer = "pick the right products (choose a number 1-6) "


# getting appriori items
application = apriori_items_generator()
print("rules")
application.print_rules()
Game_Rules = application.get_rules()


# global variables
X = 0
Y = 0
mood = 2
transitionX = -width
step = 0
boss_d = 0
day = 0
n_c = 0  # number of customers
response = 0
responded = False  # if player reponded

right_answers = []
wrong_answers = []
# according to levels
answers_scores = [[3, -1], [2, -1], [1, -1], [1, 2, -1, -2],
                  [2, 3, -1, -2], [1, 3, -1, -2], [1, 2, 3, -1, -2, -3]]
# the steps are the game plan
# first step is when boss comes , there are 7 steps , which #represent days ,

clock = pygame.time.Clock()
# game loop variables
FPS = 120
running = True

# items to purchase loading images -----
items_names = [
    "milk",
    "cheese",
    "eggs",
    "yogurt",
    "butter",
    "salt",
    "onion",
    "garlic",
    "sugar",
    "honey",
    "potato",
    "tomato",
    "bread",
    "orange",
    "apple",
    "water",
    "pineapple"
]


# items boxes
bought_posx = 0
bought_posy = 0
bought_items_box = pygame.image.load("text_boxes/box.png")
bought_items_box = pygame.transform.scale(
    bought_items_box, (items_file.item_width * 4, items_file.item_height * 4))

# public variables -----


boss_mood = 0
clients_number = len(characters_file.characters)  # per day

# if day is complete and week is complete boss will do a reviewby then a level will be upgraded or not
# -----------------------------------------------------------
# mood can go from 0 to 5
# satisfied happy very_happy , not_satisfied,not_happy,angry


# functions


main_player = Player(0, 0, 1)

# character_name , dialogue ,character , mood


def show_text(text):
    content = font.render(text, False, (255, 255, 255))
    screen.blit(content, (int(width/2), int(height/2)))


def show_and_wait(player, boss_d, boss, mood, dialogue):
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False

        show_Background(background)
        show_character(boss, 0, 0, mood)
        show_dialogue(
            player, dialogue[boss_d])
        show_hint(press_return)
        show_score(main_player)
        pygame.display.update()

# show choices


def show_and_guess(player, n_d, char, mood, dialogue):
    response = 0
    paused = True
    transaction = random.choice(Game_Rules)  # getting  a random transaction
    # shuffle items and positions for the wrong answers
    random.shuffle(items_names)
    num = random.randrange(0, 100, 1)
    while paused:
        show_Background(background)
        show_character(char, 0, 0, mood)
        show_dialogue(player, dialogue[n_d])
        show_bought(transaction, items_file.items)  # testing
        wrong_answers, right_answers = show_choices(
            transaction, items_file.items, main_player.get_level(), num)  # testing
        print(wrong_answers)
        print(right_answers)
        show_hint(press_answer)
        show_score(main_player)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                x = pygame.key.name(event.key)
                if x in ['0', '1', '2', '3', '4', '5', '6']:
                    response = int(x)
                    paused = False
    return response, wrong_answers, right_answers

# shows dialogues


def show_dialogue(player, text):
    screen.blit(text_box, (textX, textY))
    blit_text(screen, player, (50, height - 210),
              font, pygame.Color('lightblue'))
    blit_text(screen, text, (150, height - 150), font)
    pass

# a functino that shows text


def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def show_Background(img):
    screen.blit(img, (0, 0))


def show_character(img, x, y, mood):
    # print(img[mood])
    # print(mood)
    img_t = pygame.transform.scale(img[mood], (width, height))
    screen.blit(img_t, (x, y))

# show all items on screen , for test purpose


def print_all_items():
    posx_item = 0
    posy_item = 0
    for hello in items_file.items:
        get_item(hello, items_file.items, posx_item, posy_item)
        posx_item += items_file.item_width
        if(posx_item > width):
            posx_item = 0
            posy_item += items_file.item_height

# what was bought by a customer


def show_bought(transaction, items):

    print(transaction)
    length = len(transaction.lhs)
    ix = width - items_file.item_width * 3
    posx = ix
    posy = 50
    index = 0
    screen.blit(bought_items_box, (posx - items_file.item_width, 0))
    for i in transaction.lhs:
        get_item(i, items, posx, posy)
        posx += items_file.item_width
        index += 1
        if index >= length/2 or "eggs" in transaction.lhs:
            posx = ix
            posy += items_file.item_height

    # if level == 1:
    # show only two items and score is 3
    # get_item(transaction.rhs, items, width/2 + width/4, height/2)

# show item on screen depnding on position


def show_choices(transaction, items, level, num):
    wrong_answers = []
    right_answers = []
    #print("showing choices ")
    if level == 1:  # show two choices with score of 3
        # setting the right answers
        posx1 = int(width/2) + items_file.item_width * 4
        posx2 = int(width/2) - items_file.item_width * 4
        posy = height/2 - items_file.item_height
        if num > 50:
            get_item(items_names[0], items_file.items,
                     posx1, posy)  # wrong answer
            get_item(transaction.rhs[0], items_file.items, posx2, posy)
            #print("right ones  ")
            # the left are wrong and right ones are right
            wrong_answers = [1, 2, 3]
            right_answers = [4, 5, 6]
        else:
            get_item(transaction.rhs[0], items_file.items, posx1, posy)
            get_item(items_names[0], items_file.items, posx2, posy)
            #print("left ones  ")
            right_answers = [3, 2, 1]
            wrong_answers = [4, 5, 6]

    return wrong_answers, right_answers


def get_item(name, items, x=0, y=0):

    screen.blit(items[name], (int(x), int(y)))


def show_hint(text):
    hint_text_posx = width - int(width/3)
    hint_text_posy = height - 70
    blit_text(screen, text, (hint_text_posx, hint_text_posy),
              hint_font, pygame.Color('white'))


def show_score(player):
    red_points = player.get_redPoints()
    green_points = player.get_greenPoints()
    level = player.get_level()
    blit_text(screen, "red " + str(red_points), (10, 0),
              font, pygame.Color('red'))
    blit_text(screen, "green " + str(green_points), (10, 30),
              font, pygame.Color('green'))
    blit_text(screen, "level " + str(level), (10, 60),
              font, pygame.Color('purple'))


def score_by_level(response, right_answers, wrong_answers, level):
    mood = 0  # neutral , or satisfied
    if level == 1:
        if response in right_answers:
            main_player.add_greenpoints(answers_scores[level-1][0])
            mood = 1
        else:
            main_player.add_redpoints(-answers_scores[level-1][1])
            mood = 3
    return mood


while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background filling ( must make it gradient)

    if X > 254:  # game starts here
        show_Background(background)

        if step == 0:
            show_character(characters_file.boss, transitionX, 0, mood)

            if transitionX < 0:
                transitionX += 10
            else:

                # pygame.time.wait(6000)
                show_and_wait("Boss", boss_d, characters_file.boss, mood,
                              dialogues_file.boss_dialogues_step_1)
                boss_d += 1
                mood += 1
                if mood > 3:
                    mood = 0
                if boss_d == len(dialogues_file.boss_dialogues_step_1):
                    step = 1
                    boss_d = 0  # will convo too
                    transitionX = -width
                    print("changed step")
        if step == 1:
            wrong_answers, right_answers = [], []
            # change_step()
            # responses are set to 6
            # characters dialogues responde depending on responses
            # show first customer

            # show_and_wait("Customer " + str(n_c), 0, characters[n_c],
            #               0, characterts_dialogues)
            if responded == False:
                show_character(
                    characters_file.characters[n_c], transitionX, 0, 0)
                while transitionX < 0:
                    transitionX += 10

                print("take your guess (choose a number)")
                response, wrong_answers, right_answers = show_and_guess("Customer : " + str(n_c), 0, characters_file.characters[n_c],
                                                                        0, dialogues_file.characterts_dialogues)
                print()
                print(response in right_answers)
                responded = True
            if responded:
                print("result : " + str(response))
                print(response in right_answers)
                mood = score_by_level(
                    response, right_answers, wrong_answers, main_player.get_level())
                show_and_wait("Customer " + str(n_c), mood, characters_file.characters[n_c],
                              response-1, dialogues_file.characterts_dialogues)
                responded = False

            # print("response = "+str(response))
            n_c += 1
            if n_c == len(characters_file.characters):
                step = 0  # it's time for boss to visit
                n_c = 0  # reset the customers
                transitionX = -width  # boss is comimg back home
                if main_player.promote():
                    print("level upgrade")
                    # jump to boss happy , and resens step
                else:
                    print("keep trying ")
                    # jump to boss unhappy

    else:
        # print(X)
        screen.fill([X, X, X])
        text = "The Grocery Store"
        blit_text(screen, text,
                  (int(width/2 - len(text)), int(height/2)), font, pygame.Color('black'))
        X += 1

    pygame.display.update()

    # adding an image
