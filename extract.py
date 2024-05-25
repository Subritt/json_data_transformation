import json
import resources
import pandas as pd

# function to read .json file
def extract_json(file_path):
    """
    Read a .json file.

    Parameters:
    file_path (string): File location where the json file is

    Returns:
    returns variable consisting of the json data
    """
    print("file_path ->", file_path)

    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        # print(json_data)
    except Exception as e:
        print(f"Exception found: {e}")
    
    return json_data

def change_to_dataframe(json_data):
    """
    Change Json file into a Pandas DataFrame

    Parameters:
    json_data (json): json data

    Returns:
    returns pandas DataFrame
    """
    data_df = pd.DataFrame(json_data)
    return data_df

if __name__ == "__main__":
    print("Script is running as main")
    file_path = resources.json_file_path
    json_data = extract_json(file_path)
    print("json length ->", len(json_data))
    # print(json_data)
    
    data_df = change_to_dataframe(json_data)
    print("data_df length ->", len(data_df))
    print(data_df)
