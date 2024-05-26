import json
import pandas as pd

# function to read .json file
def extract_json(file_path) -> json:
    """
    Read a .json file.

    Parameters:
    file_path (string): File location where the json file is

    Returns:
    returns variable consisting of the json data
    """
    with open(file_path, 'r') as file:
        print("inside Open")
        json_data = json.load(file)
    # print(json_data)
    
    return json_data

def change_to_dataframe(json_data) -> pd.DataFrame:
    """
    Change Json file into a Pandas DataFrame

    Parameters:
    json_data (json): json data

    Returns:
    returns pandas DataFrame
    """
    data_df = pd.DataFrame(json_data)
    return data_df
