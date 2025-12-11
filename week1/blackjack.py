import cards

class BlackjackGame():
    def __init__(self):
        self.deck = cards.Deck()
        self.deck.shuffle()
        self.player_hand = cards.Hand()
        self.dealer_hand = cards.Hand()

    def hit(self):
        self.player_hand.add_card(self.deck.draw())

    def stand(self):
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.draw())

    def check_bust(self, hand: cards.Hand):
        return hand.value() > 21
    
    def check_blackjack(self, hand: cards.Hand):
        return hand.value() == 21 and len(hand.cards) == 2

    def initial_deal(self):
        self.player_hand.flush()
        self.dealer_hand.flush()

        if len(self.deck.cards) < 10:
            self.deck.reset()
        
        self.deck.shuffle()

        for _ in range(2):
            self.player_hand.add_card(self.deck.draw())
            self.dealer_hand.add_card(self.deck.draw())

    def winner(self):
        if self.check_bust(self.player_hand):
            return "Dealer wins! Player busted."
        if self.check_bust(self.dealer_hand):
            return "Player wins! Dealer busted."
        if self.check_blackjack(self.player_hand) and not self.check_blackjack(self.dealer_hand):
            return "Player wins with a Blackjack!"
        if self.check_blackjack(self.dealer_hand) and not self.check_blackjack(self.player_hand):
            return "Dealer wins with a Blackjack!"  
        if self.check_blackjack(self.player_hand) and self.check_blackjack(self.dealer_hand):
            return "Push! Both have Blackjack."
        if self.player_hand.value() > self.dealer_hand.value():
            return "Player wins!"   
        if self.player_hand.value() < self.dealer_hand.value():
            return "Dealer wins!"
        
        return "Push! It's a tie."
        
    def run_match(self):
        self.initial_deal()

        print("Player's Hand:", ', '.join(str(card) for card in self.player_hand.cards), f"Value: {self.player_hand.value()}")
        print("Dealer's Hand:", str(self.dealer_hand.cards[0]), ", Hidden")

        if self.check_blackjack(self.player_hand):
            print("Player has Blackjack!")
            return 'player_blackjack'
        
        while True:
            action = input("Hit or Stand? (h/s): ").strip().lower()
            if action == 'h':
                self.hit()
                print("Player drew:", str(self.player_hand.cards[-1]), "value:", self.player_hand.value())
                if self.check_bust(self.player_hand):
                    break
                if self.player_hand.value() == 21:
                    print("Player reached 21, auto-stand.")
                    break
            elif action == 's':
                break
            else:
                print("Invalid input, type 'h' or 's'.")
        self.stand()
        print("Dealer reveals:", ", ".join(str(c) for c in self.dealer_hand.cards), "value:", self.dealer_hand.value())

        result = self.winner()
        print("Result:", result)
        return result
    
game = BlackjackGame()
while True:
    game.run_match()
    again = input("Play again? (y/n): ").strip().lower()
    if again != 'y':
        break

