class_1 = int(input("Сколько учеников в классе №1?: "))
class_2 = int(input("Сколько учеников в классе №2?: "))
class_3 = int(input("Сколько учеников в классе №3?: "))


quantity_class_1 = class_1 // 2 + class_1 % 2
quantity_class_2 = class_2 // 2 + class_2 % 2
quantity_class_3 = class_3 // 2 + class_3 % 2

need_desk = quantity_class_1 + quantity_class_2 + quantity_class_3

print("Для 3-х классов нужно купить:", need_desk, "парт")

