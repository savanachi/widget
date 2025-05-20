from src.masks import get_reqiusits

if __name__ == "__main__":
    with open("../tests/accounts_cards.txt", "r", encoding= 'utf-8') as file:
        lines = file.readlines()
        for line in lines:
            req_mask = get_reqiusits(line)
            print(req_mask)
