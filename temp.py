'''
sentence = "Hello (candidate), this is (myname). Welcome to (company)!! How are you (doing)?"
word_mapping = [['candidate', 'shashank'], ['company', 'cisco'], ['myname', 'rahul']]
output = "Hello shashank, this is rahul. Welcome to cisco!! How are you (doing)?"
'''

# import re

# def replace_vars(sentence, word_mapping):
#     # sentence_copy = sentence
#     word_dict = {}
#     for word_map in word_mapping:
#         word_dict[word_map[0]] = word_map[1]
#     all_occ =  re.findall('\(\w+\)', sentence)
#     # print(word_dict)
#     # print(all_occ)
#     for occurence in all_occ:
#         key = occurence.strip('(').strip(')')
#         # print(key, occurence)
#         if key not in word_dict:
#             continue
#         val = word_dict[key]
#         sentence = sentence.replace(occurence, val)

#     print(sentence)


# sentence = "Hello (candidate), this is (myname). Welcome to (company)!! How are you (doing)?"
# word_mapping = [['candidate', 'shashank'], ['company', 'cisco'], ['myname', 'rahul']]
# replace_vars(sentence, word_mapping)


'''

Given a list of coins and amount which represents total amt of money, return combinations and the no of combinations
of coins that would make up to that amount. If combination is not possible return 0

amount = 5, coins = [1,2,5]

no - 4
5
2+2+1
1+1+1+2
1+1+1+1+1

'''

import copy

ans = []


def helper(amount, coins, index, curr_coins):
    if amount == 0:
        ans.append(copy.deepcopy(curr_coins))
        return
    for j in range(index, len(coins)):
        curr_coin = coins[j]
        amount_left = amount - curr_coin

        if (amount_left) > 0:
            curr_coins.append(curr_coin)
            # temp_curr_coins =
            helper(amount_left, coins, j, copy.deepcopy(curr_coins))
            helper(amount - coins[j + 1], coins, j + 1, copy.deepcopy(curr_coins))
        if (amount_left) == 0:
            curr_coins.append(curr_coin)
            ans.append(copy.deepcopy(curr_coins))
        if amount_left < 0:
            break
        print(locals())


def combinations_calculator(amount, coins):
    index = 0
    for i in range(len(coins)):
        helper(amount, coins, i, curr_coins=[])


combinations_calculator(amount=5, coins=[1, 2, 5])

print(ans)