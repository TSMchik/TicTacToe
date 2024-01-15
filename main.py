# игровое поле
playingfield = [1, 2, 3,
                4, 5, 6,
                7, 8, 9]

# победные комбинации
winline = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


# выводим поле на экран
def print_maps():
	print(playingfield[0], end=" ")
	print(playingfield[1], end=" ")
	print(playingfield[2])

	print(playingfield[3], end=" ")
	print(playingfield[4], end=" ")
	print(playingfield[5])

	print(playingfield[6], end=" ")
	print(playingfield[7], end=" ")
	print(playingfield[8])


# Сделать ход в ячейку
def step_maps(step, symbol):
	ind = playingfield.index(step)
	playingfield[ind] = symbol


# Получить текущий результат игры, после каждого ходы мы должны это проверять, есть ли 3 икса или 3 нуля
def get_result():
	win = ""
	for i in winline:
		if playingfield[i[0]] == "X" and playingfield[i[1]] == "X" and playingfield[i[2]] == "X":
			win = "X"
		if playingfield[i[0]] == "O" and playingfield[i[1]] == "O" and playingfield[i[2]] == "O":
			win = "O"
	return win


# Игра
game_over = False
player1 = True

while not game_over:

	print_maps()

	if player1:
		symbol = "X"
		step = int(input("Игрок 1, ваш ход: "))
	else:
		symbol = "O"
		step = int(input("Игрок 2, ваш ход: "))

	step_maps(step, symbol)  # делаем ход в указанную ячейку
	win = get_result()  # определим победителя
	if win != "":
		game_over = True
	else:
		game_over = False

	player1 = not player1

	print("Победил", win)
