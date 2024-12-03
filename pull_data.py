from utils.coll_log_api import pull_from_api_by_rsn
from utils.pull_and_refresh_sheet_data import (get_spreadsheet_data,
                                               update_sheet_data)


def main():
    api_response = pull_from_api_by_rsn("IM EB")

    spreadsheet_name = "Reborn Ranks - IM EB v3"
    parsed_spreadsheet_data = get_spreadsheet_data(spreadsheet_name)

    #for item in parsed_data[1:5]:
    #    print(item)
    print("-----------------")
    #print(response)

    parsed_spreadsheet_data2 = update_sheet_data(api_response, parsed_spreadsheet_data)

    print("update sheet data done")
    for item in parsed_spreadsheet_data2[1:15]:
        print(item)

    print("---_----_----")
    print(api_response)

if __name__ == "__main__":
    main()