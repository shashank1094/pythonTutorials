import copy

L1 = [1, 2, 3, 4]
L2 = copy.copy(L1)  # Assigning copy of L1 to L2
print("Initial id of L1:", id(L1))
print("Initial id of L2:", id(L2))
L2.append(5)
print("L1:", L1)
print("L2:", L2)
print("Final id of L1:", id(L1))
print("Final id of L2:", id(L2))

# import re
#
# table_t = """' Table of Contents I. INTRODUCTION .................................... 1 II. FACTUAL ASPECTS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 A. The Clean Air Act . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 B. EPA\'s Gasoline Rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 1. Establishment of Baselines . . . . . . . . . . . . . . . . . . . . . . . . 3 2. Reformulated Gasoline . . . . . . . . . . . . . . . . . . . . . . . . . . 4 3. Conventional Gasoline (or "Anti-Dumping Rules") . . . . . . . . 4 C. The May 1994 Proposal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 III. MAIN ARGUMENTS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 A. General .................................... 5 B. The General Agreement on Tariffs and Trade . . . . . . . . . . . . . . . . 6 1. Article I - General Most-Favoured-Nation Treatment . . . . . . . 6 2. Article III - National Treatment on Internal Taxation and Regulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 a) Article III:4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 b) Article III:1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 3. Article XX - General Exceptions . . . . . . . . . . . . . . . . . . . . 15 4. Article XX(b) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 a) "Protection of Human, Animal and Plant Life or Health" . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 b) "Necessary" . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 5. Article XX(d) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 6. Article XX(g) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 a) "Related to the conservation of exhaustible natural resources..." . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 b) "... made effective in conjunction with restrictions on domestic production or consumption" . . . . . . . . . . 23 7. Preamble to Article XX . . . . . . . . . . . . . . . . . . . . . . . . . . 23 8. Article XXIII - Nullification and Impairment . . . . . . . . . . . . 25 '"""
# # print(table_t)
# romans = ["I.", "II.", "III.", "IV.", "V.", "VI.", "VII.", "VIII.", "IX.", "X."]
# for i in range(0, len(romans)):
#     try:
#         print(re.search(r"((?<={})\s+(?P<name>[A-Z \.]*?)(\d))".format(romans[i]), table_t).group())
#     except:
#         pass

# import re
#
# st1 = "Hello"
# st2 = """this
# is
# a
# multi
# line
# hello"""
#
# print("st1 :: " + st1)
# print("st2 :: " + st2)
# print()
#
# print("Going to match st1 with ^ and $ in regex :: ")
# if re.match(r"^[A-Za-z]+$", st1):
#     print("Yay! its a match.")
# else:
#     print("Noo!")
#
#
# print("Going to match st2 with ^ and $ in regex :: ")
# if re.match(r"^[A-Za-z]+$", st2):
#     print("Yay! its a match.")
# else:
#     print("Noo!")
#
#
# print("Going to match st1 without ^ and $ in regex :: ")
# if re.match(r"[A-Za-z]+", st1):
#     print("Yay! its a match.")
# else:
#     print("Noo!")
#
#
# print("Going to match st2 without ^ and $ in regex :: ")
# if re.match(r"[A-Za-z]+", st2):
#     print("Yay! its a match.")
# else:
#     print("Noo!")
#
#
