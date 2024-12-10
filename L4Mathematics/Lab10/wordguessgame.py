import random

class WordGuessGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.round = 1
        self.word_tracker = []
        self.continue_count = 0
        self.words_by_length = {
            3: ["cat", "dog", "bat", "rat", "hat", "mat", "pat", "sat", "fat", "rat"],
            4: ["book", "fish", "tree", "frog", "bird", "lion", "bear", "wolf", "deer", "duck"],
            5: ["apple", "grape", "lemon", "peach", "melon", "kiwi", "mango", "olive", "onion", "pears"],
            6: ["banana", "orange", "tomato", "potato", "carrot", "celery", "garlic", "ginger", "pepper", "pumpkin"],
            7: ["cherry", "lettuce", "spinach", "cucumber", "eggplant", "avocado"],
            8: ["avocado", "bluebell", "elephant", "hospital" ],
            9: ["blueberry", "pineapple", "watermelon", "strawberry"],
        }
    
    def get_next_word(self):
        word_length = 3 + self.round - 1
        if word_length in self.words_by_length:
            return random.choice(self.words_by_length[word_length])
        else:
            print("Game Over, No more words to guess")
            return None
        
    def play_round(self):
        word_to_guess = self.get_next_word()
        if word_to_guess is None:
            print("Game Over")
            return False
        else:
            hint = word_to_guess[0]  # first letter of the word
            guessed_word = input(f"Round {self.round}: Enter a word starting with '{hint}' and has {len(word_to_guess)} letters: ")

            if guessed_word == word_to_guess:
                self.score += 10
                print("Correct! 10 points added to your score.")
            else:
                print(f"Wrong, the correct word to guess was '{word_to_guess}'")

        self.word_tracker.append(guessed_word)
        self.round += 1

        return True
    
    def display_score(self):
        print(f"Player {self.player_name} scored {self.score} points after {self.round - 1} rounds.")
        print(f"Player continued the game {self.continue_count} times.")

    def start_game(self):
        while True:
            if not self.play_round():
                break
            self.display_score()
            continue_game = input("Do you want to continue playing? (yes/no): ")
            if continue_game.lower() != "yes":
                break
            self.continue_count += 1
        print("Game Over")
        self.display_score()

# Example usage
player_name = input("Enter player name: ")
game = WordGuessGame(player_name)
game.start_game()