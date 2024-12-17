# Part 1: Countries
class Country:
    def __init__(self, capital_name: str, language_spoken: str):
        self.capital_name = capital_name
        self.language_spoken = language_spoken
    
    def display_capital(self):
        print(f"Capital: {self.capital_name}")
    
    def display_language(self):
        print(f"Language: {self.language_spoken}")

class UK(Country):
    def __init__(self):
        super().__init__("London", "English")
    
    def language(self):
        print("Many different languages are spoken but the main language is English")

class Italy(Country):
    def __init__(self):
        super().__init__("Rome", "Italian")
    
    def language(self):
        print("Italian is the main language")

class Qatar(Country):
    def __init__(self):
        super().__init__("Doha", "Arabic")
    
    def language(self):
        print("Arabic is the main language")

# Part 2: Football Players
class FootballPlayer:
    def __init__(self, name: str, age: int, team: str, position: str):
        self.name = name
        self.age = age
        self.team = team
        self.position = position
    
    def display_info(self):
        print(f"\nPlayer: {self.name}\nAge: {self.age}\nTeam: {self.team}\nPosition: {self.position}")
    
    def play(self):
        print(f"{self.name} is playing for {self.team} as {self.position}")

class Striker(FootballPlayer):
    def __init__(self, name: str, age: int, team: str, goals_scored: int = 0):
        super().__init__(name, age, team, "Striker")
        self.goals_scored = goals_scored
    
    def score_goal(self):
        self.goals_scored += 1
        print(f"{self.name} scored! Total goals: {self.goals_scored}")
    
    def play(self):
        print(f"{self.name} is trying to score goals")
    
    def display_info(self):
        super().display_info()
        print(f"Goals scored: {self.goals_scored}")

class Midfielder(FootballPlayer):
    def __init__(self, name: str, age: int, team: str, assists: int = 0):
        super().__init__(name, age, team, "Midfielder")
        self.assists = assists
    
    def make_assist(self):
        self.assists += 1
        print(f"{self.name} made an assist! Total assists: {self.assists}")
    
    def play(self):
        print(f"{self.name} is controlling the midfield")
    
    def display_info(self):
        super().display_info()
        print(f"Assists: {self.assists}")

class Defender(FootballPlayer):
    def __init__(self, name: str, age: int, team: str, tackles_made: int = 0):
        super().__init__(name, age, team, "Defender")
        self.tackles_made = tackles_made
    
    def make_tackle(self):
        self.tackles_made += 1
        print(f"{self.name} made a tackle! Total tackles: {self.tackles_made}")
    
    def play(self):
        print(f"{self.name} is defending the goal")
    
    def display_info(self):
        super().display_info()
        print(f"Tackles made: {self.tackles_made}")

class Goalkeeper(FootballPlayer):
    def __init__(self, name: str, age: int, team: str, saves_made: int = 0):
        super().__init__(name, age, team, "Goalkeeper")
        self.saves_made = saves_made
    
    def make_save(self):
        self.saves_made += 1
        print(f"{self.name} made a save! Total saves: {self.saves_made}")
    
    def play(self):
        print(f"{self.name} is guarding the goal")
    
    def display_info(self):
        super().display_info()
        print(f"Saves made: {self.saves_made}")

# Test code
def test_countries():
    print("\nTesting Countries:")
    countries = [UK(), Italy(), Qatar()]
    for country in countries:
        country.display_capital()
        country.display_language()
        country.language()
        print()

def test_players():
    print("\nTesting Football Players:")
    striker = Striker("Kane", 30, "Bayern Munich")
    midfielder = Midfielder("De Bruyne", 31, "Manchester City")
    defender1 = Defender("Van Dijk", 32, "Liverpool")
    defender2 = Defender("Dias", 26, "Manchester City")
    goalkeeper = Goalkeeper("Alisson", 31, "Liverpool")

    players = [striker, midfielder, defender1, defender2, goalkeeper]
    
    # Display info
    for player in players:
        player.display_info()
        player.play()
    
    # Simulate actions
    striker.score_goal()
    midfielder.make_assist()
    defender1.make_tackle()
    goalkeeper.make_save()

if __name__ == "__main__":
    test_countries()
    test_players()