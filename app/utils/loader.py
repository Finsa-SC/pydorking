import json

def dork_generator(categories_input = None):
    with open("../data/query.json", 'r') as file:
        all_dorks = json.load(file)

    if categories_input:
        categories = categories_input.split(",")
        for category in categories:
            if category in all_dorks:
                for dork in all_dorks[category]:
                    yield dork
            else:
                print(f"\t[x] Invalid category!")

    else:
        for dorks in all_dorks.values():
            for dork in dorks:
                yield dork