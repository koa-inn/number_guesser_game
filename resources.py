import random
from typing import List

class Chatbot():
    def __init__(self):
        self.user = Gueser()
    

    def number_selector(self, low: int, high: int):
        """ Takes range and generates a random number to be guessed. Stores this number and the range in the class object. """
        self.hidden_number: int = random.randint(low, high)
        self.lowend = low
        self.highend = high
        self.range = range(low, high)
        self.hints = 3
        self.guesses = 5


    def factors_hint(self, num) -> int:
        factors: List[int] = []
        for n in range(1,num):
            if num % n == 0:
                factors.append(n)
        random.shuffle(factors)
        return factors[0]
    
    def multiples_hint(self, num) -> int:
        multiples: List[int] = []
        for n in range(2,8):
            multiples.append(num*n)
        random.shuffle(multiples)
        return multiples[0]
        
    def larger_hint(self, num) -> int:
        larger_list = [i for i in self.range if i > num]
        random.shuffle(larger_list)
        return larger_list[0]

    def smaller_hint(self, num) -> int:
        smaller_list = [i for i in self.range if i < num]
        random.shuffle(smaller_list)
        return smaller_list[0]

    def even_odd_hint(self, num) -> str:
        if num % 2 == 0:
            return "even"
        else:
            return "odd"

    def hint_generator(self, num: int) -> List[str]:
        """ Generates the list of hints and stores them in the class object. """
        self.hint_list: List[str] = []
        self.hint_list.append(f"{self.factors_hint(num)} is a factor of the hidden number.")
        self.hint_list.append(f"{self.multiples_hint(num)} is a multiple of the hidden number.")
        if num < self.highend:
            self.hint_list.append(f"{self.larger_hint(num)} is a number which is larger than the hidden number.")
        if num > self.lowend:
            self.hint_list.append(f"{self.smaller_hint(num)} is a number which is smaller than the hidden number.")
        self.hint_list.append(f"The hidden number is an {self.even_odd_hint(num)}")
        random.shuffle(self.hint_list)
        return self.hint_list


    def guess_checker(self, guessed_num: int, hidden_num: int):
        if guessed_num == hidden_num:
            return True
        else:
            return False

    def custom_game_setup(self):
        #
        print("Please enter the desired number of guesses. The default is 5.")
        while True:
            requested_guesses = input()
            try:
                requested_guesses = int(requested_guesses)
                assert requested_guesses > 1
                break
            except:
                print("Please ony enter positive integer values.")
        #
        print("Please enter the desired number of hints (up to 4). The default is 3.")
        while True:
            requested_hints = input()
            try:
                requested_hints = int(requested_hints)
                assert requested_hints >= 0 and requested_hints <= 4
                break
            except:
                print("Please ony enter non-negative integer values up to 4.")
        #
        print("Please enter the lowest number in the range of possible number choices (number must be a positive integer).")
        while True:
            requested_lowend = input()
            try:
                requested_lowend = int(requested_lowend)
                assert requested_lowend > 0
                break
            except:
                print("Please ony enter positive integer values.")
        #
        print(f"Please enter the highest number in the range of possible number choices (number must be a positive integer and be larger than your chosen low of {requested_lowend}).")
        while True:
            requested_highend = input()
            try:
                requested_highend = int(requested_highend)
                assert requested_highend > requested_lowend
                break
            except:
                print(f"Please ony enter positive integer values which are greater than the chosen low of {requested_lowend}.")
        #
        self.number_selector(requested_lowend, requested_highend)
        self.guesses = requested_guesses
        self.hints = requested_hints
                


    def user_interface(self):
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Hello, and welcome to the number guesser extravaganza v1.0")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Please select if you would like to play with default setting or custom settings.")
       
        while True:
            settings_choice: str = input("Enter a 'd' to play with default settings or a 'c' to play with custom settings: ")
            if settings_choice not in ['c', 'd']:
                print("Please only enter a valid choice.")
            elif settings_choice == 'c':
                self.custom_game_setup()
                break
            else: 
                self.number_selector(1,30)
                break
        print("-------------------------------------------")
        print(f"The object of the game is to guess a randomly chosen number in the range from {self.lowend} to {self.highend}. You have {self.guesses} total guesses and {self.hints} hints that you can request to help guess the number.")
        print("-------------------------------------------")
        self.hint_list = self.hint_generator(self.hidden_number)
        while self.guesses > 0: #gameplay loop
            print(f"You have {self.guesses} guesses remaining and {self.hints} hints remaining.")
            guess = self.user.guess_number(self.lowend, self.highend, self)
            outcome = self.guess_checker(guess, self.hidden_number)
            if outcome == True:
                return print("Congratulations, you've guessed the correct number!!!\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            else:
                print("Sorry that guess is not correct")
                self.guesses -= 1
                print("-------------------------------------------")
        return print(f"Sorry you have run out of guesses, the hidden number was {self.hidden_number} ... better luck next time!\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")




class Gueser():
    def __init__(self):
        pass

    def guess_number(self, low: int, high: int, bot: Chatbot):
        if bot.hints > 0:
            print("If you would like to use a hint enter 'h' otherwise enter your guess.")
        else:
            print("Please enter your guess.")

        while True:
            next_guess = input()
            try:
                if next_guess in ["h","'h'"]:
                    self.request_hint(bot)
                else:
                    next_guess = int(next_guess)
                    assert next_guess >= low and next_guess <= high
                    return next_guess
            except:
                print("Please only enter valid choices.")


    def request_hint(self, bot: Chatbot):
        if bot.hints > 0:
            print(bot.hint_list.pop())
            bot.hints -= 1
        else:
            print("Unfortunately you have run out of hints...")



