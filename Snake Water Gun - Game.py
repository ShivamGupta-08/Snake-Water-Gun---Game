import emojis
import random
chance = 10
x = 0
com_p = 0
u_p = 0
print("Welcome To Game")
try:
    while chance > x:
        x += 1
        c_ch = ["W", "S", "G"]
        c_choi = random.choice(c_ch)

        print(f"Round {x}")
        print(emojis.encode('S = :snake: , W = :ocean: , G = :gun:'))
        print("Choose Your Letter")
        ch = (input())

        if ch == "S" and c_choi == "W":
            print(emojis.encode("You choose snake :snake:"))
            print(emojis.encode("Computer choose water :ocean:"))
            print("You Win")
            u_p += 1
            print(f"You have {u_p} points")
            print(f"Computer have {com_p} points")

        elif ch == "W" and c_choi == "G":
            print(emojis.encode("You choose water :ocean:"))
            print(emojis.encode("Computer choose gun :gun:"))
            print("You Win")
            u_p += 1
            print(f"You have {u_p} points")
            print(f"Computer have {com_p} points")

        elif ch == "G" and c_choi == "S":
            print(emojis.encode("You choose gun :gun:"))
            print(emojis.encode("Computer choose snake :snake:"))
            print("You Win")
            u_p += 1
            print(f"You have {u_p} points")
            print(f"Computer have {com_p} points")

        elif ch == "S" and c_choi == "G":
            print(emojis.encode("You choose snake :snake:"))
            print(emojis.encode("Computer choose gun :gun:"))
            print("Computer Win")
            com_p += 1
            print(f"You have {u_p} points")
            print(f"Computer have {com_p} points")

        elif ch == "W" and c_choi == "S":
            print(emojis.encode("You choose water :ocean:"))
            print(emojis.encode("Computer choose snake :snake:"))
            print("Computer Win")
            com_p += 1
            print(f"You have {u_p} points")
            print(f"Computer have {com_p} points")

        elif ch == "G" and c_choi == "W":
            print(emojis.encode("You choose gun :gun:"))
            print(emojis.encode("Computer choose water :ocean:"))
            print("Computer Win")
            com_p += 1
            print(f"You have {u_p} points")
            print(f"Computer have {com_p} points")

        elif ch == "S" and c_choi == "S":
            print(emojis.encode("You choose snake :snake:"))
            print(emojis.encode("Computer choose snake :snake:"))
            print("DRAW")
            print(f"You have {u_p} points")
            print(f"Computer have {com_p} points")

        elif ch == "W" and c_choi == "W":
            print(emojis.encode("You choose water :ocean:"))
            print(emojis.encode("Computer choose water :ocean:"))
            print("DRAW")
            print(f"You have {u_p} points")
            print(f"Computer have {com_p} points")

        elif ch == "G" and c_choi == "G":
            print(emojis.encode("You choose gun :gun:"))
            print(emojis.encode("Computer choose gun :gun:"))
            print("DRAW")
            print(f"You have {u_p} points")
            print(f"Computer have {com_p} points")

        else: print("Error Occurred")

        print("-------------------------------------------")


except:
    raise Exception("Error Occurred")
print("---------------RESULTS--------------------")
if u_p>com_p:
     print(emojis.encode(f"You win : {u_p} points :trophy:"))
     print(emojis.encode(f"Computer loose : {com_p} points :cry:"))
elif u_p<com_p:
     print(emojis.encode(f"Computer win : {com_p} points :trophy:"))
     print(emojis.encode(f"You loose : {u_p} points :cry:"))
