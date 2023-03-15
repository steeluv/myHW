games = []
game = input("Введите название игры: ")

while game != "0":
    if game not in games:
        games.append(game)
    else:
        print("Эта игра уже добавлена.")
    game = input("Введите название игры: ")

print(', '.join(sorted(games)))