import requests


def pull_from_api_by_rsn(rsn: str) -> dict:
    url = f"https://api.collectionlog.net/collectionlog/user/{rsn}"

    response = requests.get(url).json()

    # Initialize lookup table
    lookup_table = {}

    # Navigate through the nested structure to access all bosses and their items
    clog_data = response["collectionLog"]["tabs"]

    for _category_name, category_data in clog_data.items():
        for _boss_name, subcategory_data in category_data.items():
            items = subcategory_data["items"]
            for item in items:
                lookup_table[item["name"].lower()] = int(item["obtained"])

    return lookup_table