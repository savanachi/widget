from src.widget import get_reqiusits, get_date
from src.processing import filter_by_state, sort_by_date

if __name__ == "__main__":
    with open("../tests/accounts_cards.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            req_mask = get_reqiusits(line)
            print(req_mask)

    my_list = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
    print(my_list)
    print(sort_by_date(my_list))

    print(get_date("2024-03-11T02:26:18.671407"))
