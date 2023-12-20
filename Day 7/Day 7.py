# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:51:31 2023

@author: Abby
"""
import sys

card_replacement = {
    'T': '10',
    'J': '1',
    'Q': '12',
    'K': '13',
    'A': '14',
}

ranked_hands = []
unranked_hands = []

def importfile ():
    clean_data = []
    with open(r"C:\Users\Abby\Documents\Python\Day 7\day7.txt", 'r') as file:
        lines = file.readlines()
        my_list = [line.strip() for line in lines]
        for hand in my_list:
            hand = hand.split()
            clean_data.append(hand)
    return clean_data

def hand_type (hand):
    hand = list(hand[0])
    count_list = []
    for card in hand:
        number = hand.count(card)
        add_number = (card, number)
        if count_list.count(add_number) == 0:
            count_list.append(add_number)
    
    return(count_list)



def hand_dict (hand):
    bet = hand[1]
    hand = list(hand[0])
    for place, card in enumerate(hand):
        if not card_replacement.get(card) is None:
            hand[place] = card_replacement.get(card)
    

    count_dict = {}
    five_list = []
    four_list = []
    three_list = []
    high_card_list = []
    full_house_list = []
    pair_list = []
    count_dict["bet"] = bet
    count_dict["hand"] = hand
    for card in hand:
        number = hand.count(card)
        jokers = hand.count('1')
        print("card:", card, "count:", number, "jokers:", jokers)
        if card == "1":
            number = number
        else:
            number = number + jokers
        if number == 5:
            if five_list.count(card) == 0:
                five_list.append(card)
                count_dict["five of a kind"] = five_list
        if number == 4:
            if four_list.count(card) == 0:
                four_list.append(card)
                count_dict["four of a kind"] = four_list
        if number == 3:
            if three_list.count(card) == 0:
                three_list.append(card)
                count_dict["three of a kind"] = three_list
        if number == 2:
            if pair_list.count(card) == 0:
                pair_list.append(card)
                count_dict["pair"] = pair_list
        if number == 1:
            high_card_list.append(card)
            count_dict["high card"] = high_card_list  
    if "pair" in count_dict:
        if len(count_dict.get("pair")) == 2:
            count_dict.pop("pair")
            count_dict["two pair"] = pair_list
    if "pair" in count_dict and "three of a kind" in count_dict:
        if jokers == 0:
            full_house_list.append(count_dict["three of a kind"])
            full_house_list.append(count_dict["pair"])
            count_dict.pop("pair")
            count_dict.pop("three of a kind")
            count_dict["full house"] = full_house_list
    if "three of a kind" in count_dict:
        if len(count_dict.get("three of a kind")) == 2:
            full_house_list.append(count_dict["three of a kind"])
            count_dict.pop("three of a kind")
            count_dict["full house"] = full_house_list

    return(count_dict)



def score_hand (hand):
    print("hand to be ranked", hand)
    if ranked_hands == []:
        ranked_hands.append(hand)
        print("startup")
    else:
        print(len(ranked_hands))
        for rank, ranked_hand in enumerate(ranked_hands):
            print(rank, ranked_hand)  
            superlost = False
            win = False
            contender_hand = hand.get("hand")
            defender_hand = ranked_hand.get("hand")            
            
            contender_five = hand.get("five of a kind")
            defender_five = ranked_hand.get("five of a kind")
            if contender_five is not None and defender_five is None:
                ranked_hands.insert(rank, hand)
                print("won five no defender")
                win = True
                break
            elif contender_five is None and defender_five is not None:
                superlost = True
            elif contender_five is not None and defender_five is not None:
                winner = tiebreaker(contender_hand, defender_hand)
                print("tiebreaker")
                win = True
                if winner == 'contender':
                    ranked_hands.insert(rank, hand)
                    break
                else:
                    superlost = True
 

            contender_four = hand.get("four of a kind")
            defender_four = ranked_hand.get("four of a kind")
            if superlost == True:
                print("super lost")
                superlost = True
            elif contender_four is not None and defender_four is None:
                ranked_hands.insert(rank, hand)
                print("won four no defender")
                win = True
                break
            elif contender_four is None and defender_four is not None:
                superlost = True
                print("super lost")
            elif contender_four is not None and defender_four is not None:
                winner = tiebreaker(contender_hand, defender_hand)
                print(winner)
                print("tiebreaker")
                win = True
                if winner == 'contender':
                    ranked_hands.insert(rank, hand)
                    break
                else:
                    superlost = True 


            contender_house = hand.get("full house")
            defender_house = ranked_hand.get("full house")
            if superlost == True:
                print("super lost")
                superlost = True
            elif contender_house is not None and defender_house is None:
                ranked_hands.insert(rank, hand)
                print("won full house no defender")
                win = True
                break
            elif contender_house is None and defender_house is not None:
                superlost = True
                print("super lost")
            elif contender_house is not None and defender_house is not None:
                winner = tiebreaker(contender_hand, defender_hand)
                print(winner)
                print("tiebreaker")
                win = True
                if winner == 'contender':
                    ranked_hands.insert(rank, hand)
                    break
                else:
                    superlost = True


            contender_three = hand.get("three of a kind")
            defender_three = ranked_hand.get("three of a kind")
            if superlost == True:
                superlost = True
                print("super lost")
            elif contender_three is not None and defender_three is None:
                ranked_hands.insert(rank, hand)
                print("won three no defender")
                win = True
                break
            elif contender_three is None and defender_three is not None:
                superlost = True
                print("super lost")          
            elif contender_three is not None and defender_three is not None:    
                winner = tiebreaker(contender_hand, defender_hand)
                print(winner)
                print("tiebreaker")
                win = True
                if winner == 'contender':
                    ranked_hands.insert(rank, hand)
                    break
                else:
                    superlost = True 


            contender_two_pair = hand.get("two pair")
            defender_two_pair = ranked_hand.get("two pair")
            if superlost == True:
                print("super lost")
                superlost = True
            elif contender_two_pair is not None and defender_two_pair is None:
                ranked_hands.insert(rank, hand)
                print("won two pair no defender")
                win = True
                break
            elif contender_two_pair is None and defender_two_pair is not None:
                superlost = True
                print("super lost")  
            elif contender_two_pair is not None and defender_two_pair is not None:
                winner = tiebreaker(contender_hand, defender_hand)
                print(winner)
                print("tiebreaker")
                win = True
                if winner == 'contender':
                    ranked_hands.insert(rank, hand)
                    break
                else:
                    superlost = True       


            contender_pair = hand.get("pair")
            defender_pair = ranked_hand.get("pair")
            if superlost == True:
                print("super lost")
                superlost = True
            elif contender_pair is not None and defender_pair is None:
                ranked_hands.insert(rank, hand)
                print("won pair no defender")
                win = True
                break
            elif contender_pair is None and defender_pair is not None:
                print("super lost")  
                superlost = True
            elif contender_pair is not None and defender_pair is not None:    
                winner = tiebreaker(contender_hand, defender_hand)
                print(winner)
                print("tiebreaker")
                win = True
                if winner == 'contender':
                    ranked_hands.insert(rank, hand)
                    break
                else:
                    superlost = True 

            
            contender_high = hand.get("high card")
            defender_high = ranked_hand.get("high card")
            if superlost == True:
                print("super lost")
                superlost = True
            elif contender_high is not None and defender_high is None:
                ranked_hands.insert(rank, hand)
                print("won high no defender")
                win = True
                break
            elif contender_high is None and defender_high is not None:
                superlost = True
                print("super lost") 
            elif contender_high is not None and defender_high is not None:
                winner = tiebreaker(contender_hand, defender_hand)
                print(winner)
                print("tiebreaker")
                win = True
                if winner == 'contender':
                    ranked_hands.insert(rank, hand)
                    break
                else:
                    superlost = True 
            
            print(int(len(ranked_hands))-1)
            print(rank)
            if (int(len(ranked_hands))-1) == rank:
                ranked_hands.append(hand)
                break

            

        

           
            
    for rank, hand in enumerate(ranked_hands):
        print("rank ", rank, "hand: ", hand)
    return(ranked_hands)


def tiebreaker (contender, defender):
    print("fight!", contender, defender)
    for number, card in enumerate(contender):
        if contender[number] == defender[number]:
            print("match")
        elif int(contender[number]) > int(defender[number]):
            print("contender won")
            winner = 'contender'
            break
        elif int(contender[number]) < int(defender[number]):
            print("defender won")
            winner = 'defender'
            break
    return(winner)
    

        
clean_data = importfile()
print (clean_data)

for count, hand in enumerate(clean_data):
    hand = hand_dict(hand)
    unranked_hands.append(hand)


for hand in unranked_hands:
    rank = score_hand(hand)
    
score = 0
with open('myfiletest2.txt', 'w') as f:
    for place, ranked_hand in enumerate(ranked_hands):
        rank=len(ranked_hands)- place
        text = str(rank) + str(ranked_hand) + "\r\n"
        f.write(text)
        print(ranked_hand)
        score = score + int(ranked_hand.get('bet')) * rank
    print(score)

    




