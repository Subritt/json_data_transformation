import extract
import transformation
import load
import resources

# extract data calling extract module
def extraction():
    # file path
    file_path = resources.json_file_path
    print("file_path ->", file_path)

    # json data extraction
    json_data = extract.extract_json(file_path)
    print("json length ->", len(json_data))
    # print(json_data)
    
    # convert json data to Pandas DataFrame
    data_df = extract.change_to_dataframe(json_data)
    print("data_df length ->", len(data_df))
    # print(data_df)
    return data_df

# transformation: assign random tasks to the worker
def transform(task_data, worker_data):
    # passing task_data to further check the conditions
    task_data_condition_checked = transformation.condition_check(task_data)
    print(task_data_condition_checked)

    # filtered_task_data = task_data_condition_checked.loc[~task_data_condition_checked["Status"].isin(["Incorrect Type", "Incorrect Series"])].reset_index()
    # print(filtered_task_data)
    # print(filtered_task_data.sample()) # sample test

    master_data = transformation.assign_task(task_data_condition_checked, worker_data)

    return master_data

# create CSV files
def load_data(master_data, worker_data, folder_path):
    print("inside load method")
    load.create_csv(master_data, worker_data, folder_path)

if __name__ == "__main__":
    print("Running as driver.py")

    # data extraction
    task_data = extraction()

    # data transformation, assigning worker
    worker_data = resources.worker_data
    master_data = transform(task_data, worker_data)
    print(master_data)

    # load: create respective CSV file
    folder_path = resources.folder_path
    load_data(master_data, "master", folder_path)
    load_data(master_data, worker_data, folder_path)
