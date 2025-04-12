import random
def rolling():
    num_random = random.randint(1, 6)
    num_random2 = random.randint(1, 6)
    total = num_random + num_random2
    ket_qua = ""
    if total > 5:
        ket_qua = "tai"
    elif total <5:
        ket_qua = "xiu"
    else:
        ket_qua = "no hu"
    return ket_qua
def game():
    money_of_bank = 100000
    while True:
        ket_qua = rolling()
        du_doan = input("Enter Tài(>5) or Xĩu(<=5) or Nỗ hũ(=5): ").lower()
        while du_doan != "tai" and du_doan != "xiu" and du_doan != "no hu":
            du_doan = input("Incorrect input. Please enter again: ").lower()
        stake = int(input(f"The amount of money currently in your account: {money_of_bank}\nHow much do you want to bet?: "))

        while stake > money_of_bank:
            stake = int(input("You don't have enough money in your account. Please enter a smaller amount: "))

        if du_doan == ket_qua:
            print("You win!666")
            if du_doan == "no hu":
                money_of_bank += stake*3
            else:
                money_of_bank += stake
            print(f"The amount of money currently in your account: {money_of_bank}")
        else:
            print("You lose!")
            money_of_bank -= stake
            print(f"The amount of money currently in your account: {money_of_bank}")
        tiep_tuc = input("Do you want to play again? (Y/N): ").upper()
        if tiep_tuc == "N" or money_of_bank <= 0:
            if money_of_bank <= 0:
                print("You have no money left. Game over.")
            print("Thanks for playing!")
            break
if __name__ == '__main__':
    game()
