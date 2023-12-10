import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def play():
    is_continue = True
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    while is_continue:
        # замена туза и блэкджек
        if (sum(user_cards)>21 and not 11 in user_cards):
            print(f'You lose you have {sum(user_cards)}')
            is_continue = False
            return ('')
        elif(sum(user_cards)>21 and 11 in user_cards):
            user_cards[user_cards.index(11)] = 1
        elif (sum(computer_cards) > 21 and 11 in computer_cards):
            computer_cards[computer_cards.index(11)] = 1
        elif(sum(user_cards) == 21 or sum(computer_cards) == 21):
            print(f'Game over you have {sum(user_cards)} and computer {sum(computer_cards)}')
            return ('')
        # Вопрос о продолжении
        user_answer = input(f'You have {user_cards} and computer have {computer_cards[0]}, ** , Do you want to take another card?(Y/N)\n')
        if(user_answer == 'Y'):
            user_cards.append(random.choice(cards))
        # Подсчет результата
        else:
            user_sum = sum(user_cards)
            computer_sum = sum(computer_cards)
            while computer_sum < 17:
                computer_cards.append(random.choice(cards))
                computer_sum = sum(computer_cards)
                print(computer_sum)
            winner = ""
            if (user_sum > computer_sum):
                winner = "You win"
            elif (computer_sum > 21):
                if (sum(computer_cards) > 21 and 11 in computer_cards):
                    computer_cards[computer_cards.index(11)] = 1
                else:
                    winner = "You win"
            elif (user_sum < computer_sum and computer_sum < 21):
                winner = "Computer win"
            elif(user_sum == computer_sum):
                winner = 'Draw'
            if winner !="" :
                print(f'You cards are {user_cards}, computer cards are {computer_cards} ,{winner}')
                is_continue = False
play()
