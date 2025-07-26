import random
import ascii_art as a

def random_number():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20, 21, 22, 23, 24, 25, 26, 27, 28, 29,30, 31, 32, 33, 34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49,50, 51, 52, 53, 54, 55, 56, 57, 58, 59,60, 61, 62, 63, 64, 65, 66, 67, 68, 69,70, 71, 72, 73, 74, 75, 76, 77, 78, 79,80, 81, 82, 83, 84, 85, 86, 87, 88, 89,90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
    number = random.choice(numbers)
    return number

if __name__ == "__main__":
    attempts = 0
    while attempts < 3:
        user_num = input("From 1-100 guess the number I am thinking:\n")
        computer_number =  random_number()
        if user_num == computer_number:
            print(f"YOU GUESSED {user_num} AND IT'S CORRECT!! WOOHOO!! HERE IS A FLOWER")
            print(a.flower)
            break
        else:
            attempts +=1
            print(a.oh_no)
            print(f"Oh no! You guessed {user_num} and it is NOT correct")
            print("Try again")

        if attempts == 3:
            print(f"Oh damn, you lost! The number I was thinking was {computer_number}")
            print(a.you_lost)
    
    

