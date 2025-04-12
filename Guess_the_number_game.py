import random
def choose_lv():
    while True:
        lv = input("Mời bạn nhập mức độ trò chơi (E/M/H): ").upper()
        if lv == "E" or lv == "M" or lv == "H":
            break
    time = 0
    match lv:
        case "E":
            times = 9
        case "M":
            times = 6
        case "H":
            times = 4
    return times
def game():
    time_play = 0
    time_win = 0
    while True:
        num_random = random.randint(1, 101)
        times = choose_lv()
        for i in range(times):
            num_guess = int(input("Enter your guessing number:"))
            if num_guess == num_random:
                print(f"You win! After {i+1} times.")
                time_win += 1
                break
            elif num_guess > num_random:
                print(f"Wrong! Your guessing number is too high. you have {times-i-1} times left.")
            else:
                print(f"Wrong! Your guessing number is too low. you have {times-i-1} times left.")
        print(f"The computer's guessing number is {num_random}")
        time_play += 1
        choi_tiep = input("Do you want to play again? (Y/N): ").upper()
        if choi_tiep == "N":
            print(f"Total time play: {time_play}, total time win: {time_win}")
            break
if __name__ == '__main__':
    game()