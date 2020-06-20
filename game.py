import pygame
from player import Player
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

pygame.font.init()
font = pygame.font.SysFont("Arial", 32)
textX = 10
textY = width - 100

pygame.mixer.init()
background_music = pygame.mixer.music.load("Glimpse - Ambitions.mp3")
pygame.mixer.music.play(-1)
# characters
boss = [
    pygame.image.load('Characters/Boss_character2/satisfied.png'),
    pygame.image.load('Characters/Boss_character2/happy.png'),
    pygame.image.load('Characters/Boss_character2/very_happy.png'),
    pygame.image.load('Characters/Boss_character2/not_satisfied.png'),
    pygame.image.load('Characters/Boss_character2/not_happy.png'),
    pygame.image.load('Characters/Client_man/angry.png'),
]

client_man = [
    pygame.image.load('Characters/Client_man/satisfied.png'),
    pygame.image.load('Characters/Client_man/happy.png'),
    pygame.image.load('Characters/Client_man/very_happy.png'),
    pygame.image.load('Characters/Client_man/not_satisfied.png'),
    pygame.image.load('Characters/Client_man/not_happy.png'),
    pygame.image.load('Characters/Client_man/angry.png')

]

client_old_man_1 = [
    pygame.image.load('Characters/Client_Old_man_1/satisfied.png'),
    pygame.image.load('Characters/Client_Old_man_1/happy.png'),
    pygame.image.load('Characters/Client_Old_man_1/very_happy.png'),
    pygame.image.load('Characters/Client_Old_man_1/not_satisfied.png'),
    pygame.image.load('Characters/Client_Old_man_1/not_happy.png'),
    pygame.image.load('Characters/Client_Old_man_1/angry.png'),

]

client_old_woman = [
    pygame.image.load('Characters/client_old_woman/satisfied.png'),
    pygame.image.load('Characters/client_old_woman/happy.png'),
    pygame.image.load('Characters/client_old_woman/very_happy.png'),
    pygame.image.load('Characters/client_old_woman/not_satisfied.png'),
    pygame.image.load('Characters/client_old_woman/not_happy.png'),
    pygame.image.load('Characters/client_old_woman/angry.png'),

]

client_old_woman_2 = [
    pygame.image.load('Characters/client_old_woman_2/satisfied.png'),
    pygame.image.load('Characters/client_old_woman_2/happy.png'),
    pygame.image.load('Characters/client_old_woman_2/very_happy.png'),
    pygame.image.load('Characters/client_old_woman_2/not_satisfied.png'),
    pygame.image.load('Characters/client_old_woman_2/not_happy.png'),
    pygame.image.load('Characters/client_old_woman_2/angry.png'),

]

client_young = [
    pygame.image.load('Characters/Client_Young/satisfied.png'),
    pygame.image.load('Characters/Client_Young/happy.png'),
    pygame.image.load('Characters/Client_Young/very_happy.png'),
    pygame.image.load('Characters/Client_Young/not_satisfied.png'),
    pygame.image.load('Characters/Client_Young/not_happy.png'),
    pygame.image.load('Characters/Client_Young/angry.png'),

]

client_young_2 = [
    pygame.image.load('Characters/Client_Young2/satisfied.png'),
    pygame.image.load('Characters/Client_Young2/happy.png'),
    pygame.image.load('Characters/Client_Young2/very_happy.png'),
    pygame.image.load('Characters/Client_Young2/not_satisfied.png'),
    pygame.image.load('Characters/Client_Young2/not_happy.png'),
    pygame.image.load('Characters/Client_Young2/angry.png'),

]
# items to purchase -----
items = [
    "milk",
    "cheese",
    "eggs",
    "yougurt",
    "butter",
    "onions",
    "garlic",
    "sugar",
    "honey",
    "potato",
    "tomato",
    "bread"
]

# public variables -----
# dialogues

boss_dialogues_step_1 = [
    "Hello , we're happy that you started working in our store ...",
    "if you have worked here or somewhere else you must know \n that there is a diffrence here ...",
    ", if you can manage to guess what people will buy, they will be happy,if they become happy , i'll be glad to promote you .",
    "But if you make them unhappy ,cause i won't be happy and you may cause me to fire you",
    "Allright , see you at the end of the week ,  goodluck !"


]

characterts_dialogues = [
    "Good Day ! , i don't usally see you here ",
    "hmmm , thank you ! (satisfied)",
    "haha ! , yeah you are good (happy)",
    "Oh wow ! , how could you guess that , Thank you very much (very happy )!!",
    "euh , no thanks (not satisfied)",
    "i wouldn't do that if i were you (not happy) ",
    "i will never comeback again (angry)"
]

characters = [
    client_man,
    client_old_man_1,
    client_old_woman,
    client_old_woman_2,
    client_young,
    client_young_2
]

boss_mood = 0
clients_number = len(characters)  # per day
# if day is complete and week is complete boss will do a reviewby then a level will be upgraded or not
# -----------------------------------------------------------
# mood can go from 0 to 5
# satisfied happy very_happy , not_satisfied,not_happy,angry


# functions


main_player = Player(0, 0, 0)

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
        blit_text(screen, "press return", (0, 20), font, pygame.Color('white'))
        show_Background(background)
        show_character(boss, 0, 0, mood)
        show_dialogue(
            player, dialogue[boss_d])
        pygame.display.update()


def show_and_guess(player, n_d, char, mood, dialogue):
    response = 0
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                x = pygame.key.name(event.key)
                if x in ['0', '1', '2', '3', '4', '5', '6']:
                    response = int(x)
                    paused = False
        blit_text(screen, "choose an answer", (0, 20),
                  font, pygame.Color('white'))
        show_Background(background)
        show_character(char, 0, 0, mood)
        show_dialogue(
            player, dialogue[n_d])
        pygame.display.update()

    return response


def guess():
    # guess clients purchases
    pass


def client_enter():
    # generates clients purchases
    pass


def show_dialogue(player, text):
    screen.fill(pygame.Color('blue'), rect=[
                0, height - 100, width, height-100])
    blit_text(screen, player, (10, height - 100),
              font, pygame.Color('lightblue'))
    blit_text(screen, text, (150, height - 100), font)

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


def show_items():
    pass


def show_Background(img):
    screen.blit(img, (0, 0))


def show_Character(img, x, y, mood):
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x, y))


def show_character(img, x, y, mood):
    # print(img[mood])
    # print(mood)
    img_t = pygame.transform.scale(img[mood], (width, height))
    screen.blit(img_t, (x, y))


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
# the steps are the game plan
# first step is when boss comes , there are 7 steps , which #represent days ,

clock = pygame.time.Clock()
# game loop
FPS = 120
running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background filling ( must make it gradient)

    if X > 254:  # game starts here
        show_Background(background)

        if step == 0:
            show_character(boss, transitionX, 0, mood)
            if transitionX < 0:
                transitionX += 5
            else:

                # pygame.time.wait(6000)
                show_and_wait("boss", boss_d, boss, mood,
                              boss_dialogues_step_1)

                boss_d += 1
                mood += 1
                if mood > 3:
                    mood = 0
                if boss_d == len(boss_dialogues_step_1):
                    step = 1
                    boss_d = 0  # will convo too
                    print("changed step")
        if step == 1:
            # change_step()
            # responses are set to 6
            # characters dialogues responde depending on responses
            # show first customer

            # show_and_wait("Customer " + str(n_c), 0, characters[n_c],
            #               0, characterts_dialogues)
            if responded == False:
                print("take your guess (choose a number)")
                response = show_and_guess("Customer " + str(n_c), 0, characters[n_c],
                                          0, characterts_dialogues)
                responded = True
            if responded:
                print("result : " + str(response))
                show_and_wait("Customer " + str(n_c), response, characters[n_c],
                              response-1, characterts_dialogues)
                responded = False

            # print("response = "+str(response))
            n_c += 1
            if n_c == len(characters):
                step = 0  # it's time for boss to visit
                n_c = 0  # reset the customers

    else:
        # print(X)
        screen.fill([X, X, X])
        text = "The Grocery Store"
        blit_text(screen, text,
                  (int(width/2 - len(text)), int(height/2)), font, pygame.Color('black'))
        X += 1

    pygame.display.update()

    # adding an image
