from masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    with open("../tests/card_number.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            card_mask = get_mask_card_number(line.strip())
            print(f"card_mask: {card_mask}")

    with open("../tests/accounts_num.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            acc_mask = get_mask_account(line.strip())
            print(f"acc_mask: {acc_mask}")
