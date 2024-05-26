import pandas as pd
import os

def create_csv(task_data, worker_data, folder_path, source_file_name):

    if worker_data == "master":
        # check folder availability
        final_destination_folder = folder_check(folder_path, source_file_name)

        # create csv
        file_name = f"{worker_data}.csv"
        task_data.to_csv(os.path.join(final_destination_folder, file_name), index=False)
        print(f"{worker_data}.csv created!")
    else:
        for worker in worker_data:
            print("creating CSV for ->", worker)
            # print(task_data)
            # print(type(task_data))
            try:
                worker_df = task_data.loc[
                    task_data["Assignee"] == worker
                ].copy()
                # drop Assignee column
                worker_df.drop(columns=["Assignee"], axis=1, inplace=True)

                # check folder availability
                final_destination_folder = folder_check(folder_path, source_file_name)

                # create csv
                file_name = f"{worker}.csv"
                worker_df.to_csv(os.path.join(final_destination_folder, file_name), index=False)
                print(worker_df)
                print(f"{worker}.csv created!")
            except Exception as e:
                print("Exception: ", e)

# check if folder exists, else create one
def folder_check(folder_path, source_file_name):
    final_destination_folder = f"{folder_path}/{source_file_name}"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        os.makedirs(final_destination_folder)
        return final_destination_folder
    else:
        if not os.path.exists(final_destination_folder):
            os.makedirs(final_destination_folder)
            return final_destination_folder
        return final_destination_folder
        


if __name__ == "__main__":
    print("Running as load.py")
