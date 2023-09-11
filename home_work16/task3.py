def update_hero(**kwargs):
    with open('hero.ini', 'r') as file:
        lines = file.readlines()

    hero_data = {}

    for line in lines:
        key, value = line.strip().split('=')
        hero_data[key.strip()] = value.strip()

    for key, value in kwargs.items():
        if key in hero_data:
            hero_data[key] = str(value)

    with open('hero.ini', 'w') as file:
        for key, value in hero_data.items():
            file.write(f'{key}={value}\n')
        print("Hero updated")

update_hero(hero="Hulk", power=450, Y=2.3)
