def create_empty_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def display_board(board):
    for row in board:
        print(' '.join(row))
    print()

def place_ship(board, x, y, ship_size, orientation):
    if orientation == 'H':
        for i in range(ship_size):
            board[y][x + i] = 'X'
    elif orientation == 'V':
        for i in range(ship_size):
            board[y + i][x] = 'X'

def main():
    size = 10
    player_board = create_empty_board(size)

    ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    for ship_size in ship_sizes:
        display_board(player_board)
        print(f'Розмістіть корабель розміром {ship_size}:')
        while True:
            try:
                x, y = map(int, input('Введіть координати (наприклад, 0 0): ').split())
                orientation = input('Введіть орієнтацію (H - горизонтальна, V - вертикальна): ').strip().upper()

                if x < 0 or x >= size or y < 0 or y >= size:
                    raise ValueError('Недопустимі координати!')

                if orientation not in ('H', 'V'):
                    raise ValueError('Недопустима орієнтація! Введіть H або V.')

                # Перевірка можливості розміщення корабля
                if orientation == 'H':
                    if x + ship_size > size:
                        raise ValueError('Корабель не поміщається на полі!')
                    for i in range(ship_size):
                        if player_board[y][x + i] != ' ':
                            raise ValueError('Корабель перекриває інший корабель!')
                elif orientation == 'V':
                    if y + ship_size > size:
                        raise ValueError('Корабель не поміщається на полі!')
                    for i in range(ship_size):
                        if player_board[y + i][x] != ' ':
                            raise ValueError('Корабель перекриває інший корабель!')

                place_ship(player_board, x, y, ship_size, orientation)
                break
            except (ValueError, IndexError):
                print('Недопустимі координати або розташування корабля. Спробуйте ще раз.')

    display_board(player_board)
    print('Ви розмістили всі кораблі!')

if __name__ == "__main__":
    main()
