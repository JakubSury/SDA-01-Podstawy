position_list = []  # List which contains numbers of free fields. If the field is not free - value " "
game_list = []  # List which contains o, x on the fields
player = ("o", "x")
turn = False  # Index of the player tuple, player[False]="o", player[True]="x"
winning_list = [player[turn], player[turn], player[turn]]  # Winning list ["o", "o", "o"] or ["x", "x", "x"] - depends on the actual turn
game_on = True  # True if the game is not ended
game_won = False  # True if a player won the game


def printing_two_boards_3x3(left_board, right_board):
    print()
    for i in range(0, 9, 3):
        print(
            f"| {left_board[i]} | {left_board[i + 1]} | {left_board[i + 2]} |      | {right_board[i]} | {right_board[i + 1]} | {right_board[i + 2]} |")
    print()


for i in range(9):
    position_list.append(i + 1)  # [1, 2, 3, ..., 9]
    game_list.append(" ")  # [" ", " ", ..., " "]

while game_on:

    printing_two_boards_3x3(game_list, position_list)

    print(f"Kolej gracza '{player[turn]}'")

    while True:
        chosen_field = input("Wybierz pole: ")
        try:
            chosen_field = int(chosen_field)
        except ValueError:
            print("Błędny typ")
            continue
        if chosen_field not in range(1, 10):
            print("Liczba spoza zakresu od 1 do 9 włącznie\n")
        else:
            break

    # dodać sprawdzanie, czy dobra wartość

    chosen_field = int(chosen_field) - 1
    if game_list[chosen_field] != " ":
        print("Pole jest zajęte")
        continue

    else:
        game_list[chosen_field] = player[turn]
        position_list[chosen_field] = " "

        if game_list[0:9:4] == winning_list:  # diagonal [0, 4, 8]
            game_on = False
            game_won = True

        elif game_list[2:7:2] == winning_list:  # diagonal [2, 4, 6]
            game_on = False
            game_won = True

        else:
            for i in range(3):
                index_vertical = 0  # 0, 3, 6
                index_horizontal = 0  # 0, 1, 2 - same as i, but new variable used for clarity

                if game_list[index_vertical:index_vertical + 3] == winning_list:  # [0, 1, 2] [3, 4, 5] [6, 7, 8]
                    game_on = False
                    game_won = True
                    break

                elif game_list[
                     index_horizontal:index_horizontal + 7:3] == winning_list:  # [0, 3, 6] [1, 4, 7] [2, 5, 8]
                    game_on = False
                    game_won = True
                    break

        if " " not in game_list:  # if all fields are occupied
            game_on = False

        if game_on == False:  # if the game is over
            printing_two_boards_3x3(game_list, position_list)

            if game_won == True:  # if sb won
                print(f"Gratulacje, wygrywa gracz: {player[turn]}")

            else:  # there is no winner
                print("Remis")

        else:  # when the game is not over - change of turn
            turn = not turn