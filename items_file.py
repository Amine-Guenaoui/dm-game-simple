
import pygame

width, height = 1024, 768

item_width = int(width/12)
item_height = int(height/10)


milk = pygame.image.load("items/milk2.png")
milk = pygame.transform.scale(milk, (item_width, item_height))

cheese = pygame.image.load("items/cheese.png")
cheese = pygame.transform.scale(cheese, (item_width, item_height))

eggs = pygame.image.load("items/eggs.png")
eggs = pygame.transform.scale(eggs, (item_width * 2, item_height))

yogurt = pygame.image.load("items/yogurt.png")
yogurt = pygame.transform.scale(yogurt, (item_width, item_height))

butter = pygame.image.load("items/butter.png")
butter = pygame.transform.scale(butter, (item_width, item_height))

salt = pygame.image.load("items/salt.png")
salt = pygame.transform.scale(salt, (item_width, item_height))

onion = pygame.image.load("items/onions.png")
onion = pygame.transform.scale(onion, (item_width, item_height))

garlic = pygame.image.load("items/garlic2.png")
garlic = pygame.transform.scale(garlic, (item_width, item_height))

sugar = pygame.image.load("items/sugar.png")
sugar = pygame.transform.scale(sugar, (item_width, item_height))

honey = pygame.image.load("items/honey.png")
honey = pygame.transform.scale(honey, (item_width, item_height))

potato = pygame.image.load("items/potato.png")
potato = pygame.transform.scale(potato, (item_width, item_height))

tomato = pygame.image.load("items/tomato.png")
tomato = pygame.transform.scale(tomato, (item_width, item_height))

bread = pygame.image.load("items/bread.png")
bread = pygame.transform.scale(bread, (item_width, item_height))

orange = pygame.image.load("items/orange.png")
orange = pygame.transform.scale(orange, (item_width, item_height))

apple = pygame.image.load("items/apple.png")
apple = pygame.transform.scale(apple, (item_width, item_height))

water = pygame.image.load("items/water.png")
water = pygame.transform.scale(water, (item_width, item_height))

pineapple = pygame.image.load("items/pineapple.png")
pineapple = pygame.transform.scale(pineapple, (item_width, item_height))


items = {'milk': milk,
         'cheese': cheese,
         'eggs': eggs,
         'yogurt': yogurt,
         'butter': butter,
         'salt': salt,
         'onion': onion,
         'garlic': garlic,
         'sugar': sugar,
         'honey': honey,
         'potato': potato,
         'tomato': tomato,
         'bread': bread,
         'orange': orange,
         'apple': apple,
         'water': water,
         'pineapple': pineapple}
