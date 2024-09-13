from utils.coll_log_api import pull_from_api_by_rsn
from utils.pull_and_refresh_sheet_data import (get_spreadsheet_data,
                                               update_sheet_data)


def main():
    response = pull_from_api_by_rsn("IM EB")

    spreadsheet_name = "Reborn Ranks - IM EB v3"
    parsed_data = get_spreadsheet_data(spreadsheet_name)

    update_sheet_data(parsed_data, response)



if __name__ == "__main__":
    main()