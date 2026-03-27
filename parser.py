import json

def update_values():
    data = {
        "Bandicoot": 10, "Buffalo": 20, "Cat": 15, "Chick": 5, "Chicken": 5,
        "Dog": 25, "Otter": 18, "Pumpkin": 8, "Robin": 12, "Tasmanian Tiger": 60,
        "Mouse": 3, "Ant": 1, "Green Snake": 7, "Coyote": 20, "Sandfish": 4,
        "Armadillo": 22, "Sado Mole": 13, "Beluga Whale": 200, "Ghost": 50,
        "Bluebottle Fly": 2, "Cockroach": 1, "Mosquito": 1, "Piranha": 12,
        "Dugong": 40, "Brachiosaurus": 500, "Mongoose": 15, "Maleo Bird": 18,
        "Bali Starling": 25, "Malaysian Tapir": 35, "Flying Fish": 10, "Bullfrog": 8,
        "Wolpertinger": 50, "Stingray": 45, "Liger": 60, "Kid Goat": 10, "Angelfish": 5,
        "Show Pony": 30, "Ash Zebra": 40, "Bat": 7, "Black Panther": 80, "Blue Dog": 25,
        "Capybara": 15, "Chocolate Labrador": 35, "Dingo": 18, "Fennec Fox": 20,
        "Glyptodon": 50, "Meerkat": 12, "Pink Cat": 15, "Puma": 45, "Silly Duck": 5,
        "Snow Cat": 40, "Camel": 35, "Donkey": 25, "Tawny Frogmouth": 10, "Rock Pigeon": 5,
        "Borhyaena Gigantica": 80, "Angler Fish": 12, "Snowman": 50, "Stegosaurus": 300,
        "Triceratops": 350, "Wild Boar": 40, "Wolf": 45, "Fossa": 20, "Mahi Mahi": 10,
        "Arctic Hare": 15, "Black Mummy Cat": 25, "Raccoon": 10, "Rattle Snake": 8,
        "Gila Monster": 12, "Possum": 5, "Rhino Beetle": 18, "Tanuki": 15,
        "Banded Palm Civet": 20, "Yellow Lipped Sea Krait": 10, "Hermit Crab": 5,
        "Lobster": 12, "Arctic Tern": 15, "Frogspawn": 3, "Red Cardinal": 8, "Kirin": 250,
        "Slug": 1, "Blue Scorpion": 20, "Scarecrow": 5, "Mole": 5, "Velociraptor": 400,
        "Poodle": 30, "Cute-A-Cabra": 10, "Eggnog Dog": 15, "Harp Seal": 25,
        "Rock": 1, "Warthog": 20, "Amami Rabbit": 12, "Eel": 5, "Ermine": 10,
        "Crab": 3, "Dolphin": 50, "Quokka": 15, "Canadian Goose": 8,
        "Birthday Butterfly 2023": 5, "2022 Uplift Butterfly": 5, "2021 Uplift Butterfly": 5,
        "Snow Leopard": 80, "Chickatrice": 100, "Therapy Dog": 25, "Dylan": 50,
        "River": 40, "Pistachio": 20, "Australian Kelpie": 30, "Beaver": 15, "Bunny": 5,
        "Cow": 20, "Dilophosaurus": 200, "Elephant": 150, "Elf Shrew": 10, "Emu": 15,
        "Hyena": 25, "Lynx": 30, "Monkey": 12, "Musk Ox": 50, "Narwhal": 100, "Ox": 50,
        "Pig": 20, "Polar Bear": 120, "Pterodactyl": 350, "Rabbit": 5, "Rat": 3,
        "Reindeer": 60, "Rhino": 100, "Seahorse": 8, "Snow Puma": 90, "Swan": 12,
        "Woolly Mammoth": 500, "Abyssinian Cat": 20, "Albino Bat": 15, "Arctic Fox": 40,
        "Black Scarab": 50, "Blue Scarab": 50, "Brown Bear": 60, "Business Monkey": 25,
        "Butterfly": 2, "Crocodile": 35, "Dalmatian": 30, "Evil Dachshund": 18,
        "Flamingo": 12, "Frog": 5, "Hedgehog": 10, "Husky": 25, "Koala": 15, "Lamb": 8,
        "Lion": 80, "Llama": 20, "Platypus": 15, "Puffin": 8, "Red Squirrel": 5,
        "Skele-Dog": 50, "St. Bernard": 35, "Toy Monkey": 10, "Turkey": 5, "White Tiger": 90,
        "Zombie Buffalo": 40, "Albino Monkey": 15, "Arctic Reindeer": 60, "Axolotl": 5,
        "Bat Dragon": 200, "Cerberus": 300, "Chameleon": 12, "Cobra": 15, "Crow": 5,
        "Dancing Dragon": 400, "Diamond Dragon": 500, "Diamond Griffin": 450,
        "Diamond Lady Bug": 100, "Diamond Unicorn": 550, "Dodo": 30, "Dragon": 350,
        "Evil Unicorn": 300, "Frost Dragon": 400, "Frost Fury": 450, "Ghost Dragon": 250,
        "Giraffe": 80, "Gold Dragon": 500, "Gold Griffin": 450, "Gold Mummy Cat": 50,
        "Gold Penguin": 40, "Gold Scarab": 50, "Gold Tiger": 80, "Gold Unicorn": 550,
        "Gold Walrus": 60, "Golden Lady Bug": 100, "Golden Rat": 15, "Goldhorn": 500,
        "Griffin": 400, "Ice Golem": 350, "King Bee": 60, "King Monkey": 80, "Kitsune": 300,
        "Lavender Dragon": 450, "Lion Guardian": 500, "Ninja Monkey": 50, "Octopus": 8,
        "Owl": 12, "Parrot": 10, "Peacock": 25, "Phoenix": 500, "Queen Bee": 80,
        "Robodog": 60, "Shadow Dragon": 500, "Shark": 45, "Skele-Rex": 400, "Snow Owl": 40,
        "Squid": 10, "Steel Ox": 350, "T-Rex": 500, "Turtle": 12, "Unicorn": 450
    }

    with open("values.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print("Values updated")