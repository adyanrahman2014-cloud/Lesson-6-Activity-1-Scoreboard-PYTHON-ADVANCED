class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Cricket - Player: {self.__player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} Hits a Six!")

    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score Cannot Be Negative.")


class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Cricket - Player: {self.__player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} Scores A Wonderful GOAL!!!")

    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score Cannot Be Negative.")


cricket = Cricket("John", 67)
football = Football("Messi", 3)

print("=== Sports ScoreBoard ===\n")
for sport in (cricket, football):
    sport.info()
    sport.play()
    print()

print("--- Direct change attempt ---")
cricket.__score = 999
print(f"get_score() still shows: {cricket.get_score()}")

print("\n--- Updating scores ---")
cricket.set_score(100)
football.set_score(5)