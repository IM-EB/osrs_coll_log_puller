import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from typing import Dict, List


class CollectionLogEntry:
    def __init__(self, item_name: str, image: str, bis:str, old_points_avail: str, points_avail:str, obtained: int, points_gained: str, collection_log: str):
        self.item_name = item_name
        self.image = image
        self.bis = bis
        self.old_points_avail = old_points_avail
        self.points_avail = points_avail
        self.obtained = obtained
        self.points_gained = points_gained
        self.collection_log = collection_log
        self.calculated_obtained = 0

    def __repr__(self):
        return (f"CollectionLogEntry(item_name={self.item_name}, image={self.image}, bis={self.bis}, "
                f"old_points_avail={self.old_points_avail}, points_avail={self.points_avail}, obtained={self.obtained}, "
                f"points_gained={self.points_gained}, collection_log={self.collection_log}, calculated_obtained={self.calculated_obtained})")

def get_spreadsheet_data(spreadsheet_name: str) -> Dict[str, str]:
    # Define the scope and credentials
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Construct the path to the JSON keyfile
    keyfile_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'creds', 'google-sheets-API-credentials.json')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile_path, scope)

    # Authenticate and open the spreadsheet
    client = gspread.authorize(credentials)

    try:
        # Open the specific spreadsheet
        spreadsheet = client.open(spreadsheet_name)
        worksheet = spreadsheet.get_worksheet(1)  # Assuming you want to access the first worksheet

        # Get all values from the worksheet
        collection_log_data = worksheet.get_all_values()[2:]

        # Parse the data into a more usable format
        parsed_data = parse_data(collection_log_data)
        return parsed_data

    except gspread.exceptions.SpreadsheetNotFound:
        print("Spreadsheet not found. Please check the name and permissions.")

def parse_data(data: List[List[str]]) -> List[CollectionLogEntry]:
    entries = []
    for row in data:
        entry = CollectionLogEntry(
            item_name=row[0].lower(),
            image=row[1],
            bis=row[2],
            old_points_avail=row[3],
            points_avail=row[4],
            obtained = 1 if row[5] == 'TRUE' else 0,
            points_gained=row[6],
            collection_log=row[7]
        )
        entries.append(entry)
    return entries

def update_sheet_data(response: Dict[str, str], parsed_data: Dict[str, str]) -> Dict[str, str]:
    updated_sheet_data = {}
    # Perform the necessary updates to the sheet data using the response and parsed_data dictionaries
    # ...
    # Update the updated_sheet_data dictionary with the updated values
    # ...
    return updated_sheet_data
