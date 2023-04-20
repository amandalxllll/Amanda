PLAYERS = {
    "Karim Benzema": 94,  # The player's name: his rating
    "Robert Lewandowski": 93,
    "Kylian Mbappe": 96,
    "Luka Modric": 90,
    "Pedri": 93,
    "Frenkie de Jong": 88,
}

LEGENDARIES = {
    "Lionel Messi": (99, 1.03),
    # Thelegendary player's name: (his rating, his chemistry booster value)
    "Cristiano Ronaldo": (97, 0.98),
}


class Team:
    """FIFA Ultimate Team.

    Represents a FIFA Ultimate Team, with players, ratings, and functionality to draft players and evaluate team strength.
    """

    def __init__(self, name, initial_players=0):
        self.name = name
        if initial_players == None:
            self.squad = []
        else:
            self.squad = initial_players
        self.rating = 0

    def __str__(self):
        return self.name + "has" + str(self.squad)

    def draft(self, player):
        """Draft a player from PLAYERS and update the team's rating, which is the average rating of the entire current squad.

        Args:
            player (str): The name of the player to be drafted.
        1. List the players you get
        2. sum their ratings
        3. get the average by using sum/numbe of players
        """
        self_player = self.squad.append
        sum = 0
        for n in self_player:
            sum = sum + PLAYERS[n]
            self.ratings = sum / len(self.player)
            return self.ratings

    def draft_legendary(self, player):
        """
        similar with function3.
        add legendary in
        """
        sum = 0
        self_player = self.squad.append
        for n in self_player:
            sum = sum + LEGENDARIES[n]
        self.ratings = sum / len(self.squad + LEGENDARIES)
        return self.ratings

    def match(self, others):
        return self.ratings


#############################################
# Please DO NOT change code in main function!
#############################################
def main():
    real_madrid = Team("Real Madrid", initial_players=["Karim Benzema"])
    barcelona = Team("Barcelona")
    print("Before drafting squad:")
    print(real_madrid)
    print(barcelona)
    print()
    print("After drafting squad:")
    barcelona.draft("Robert Lewandowski")
    real_madrid.draft("Kylian Mbappe")
    barcelona.draft("Pedri")
    real_madrid.draft("Luka Modric")
    barcelona.draft("Frenkie de Jong")
    print(real_madrid)
    print(barcelona)
    print()
    print("Will Barcelona defeat Real Madrid?")
    print(barcelona > real_madrid)
    print()
    print("After drafting legendary:")
    real_madrid.draft_legendary("Cristiano Ronaldo")
    barcelona.draft_legendary("Lionel Messi")
    print(real_madrid)
    print(barcelona)
    print()
    print("Will Barcelona defeat Real Madrid?")
    print(barcelona > real_madrid)


if __name__ == "__main__":
    main()
