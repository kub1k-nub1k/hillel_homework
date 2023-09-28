apples = int(input("Сколько яблок у вас есть?: "))
students = int(input("Сколько учеников будут яблоки?: "))

# part_app - количество яблок у каждого ученика
part_app = apples // students
# basket - количество яблок оставшихся после разделения между учениками
basket = apples % students

print("Каждому ученику досталось:", part_app)
print("В корзине осталось:", basket)