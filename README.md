### This program covers the following steps.
1. Program to only extract JSON files located within source_folder. <br />
2. Convert it to pandas DataFrame. <br />
3. Perform specific two conditional checks within the DataFrame and add a Status Column. <br />
4. Randomly assign rows fulfiling the conditional checks to the listed workers. <br />
5. Create a master CSV file consisting of initial plus added columns. <br />
6. Create individual worker CSV files only consisting of initial columns.

### To be changes:
1. Update the source_data folder with your desired JSON files. <br />
2. Update `resources.py`: <br />
    2.1 `source_folder_path` variable with the path for your `source_data` folder. <br />
    2.2 `worker_data` list with your desired worker names. <br />
    2.3 `folder_path` with the folder path for your CSV dump primary folder. <br />
    2.4 `master_csv_file_name` with the name that you want to give to the master CSV file. <br />

### To Run
After you have made all the necessary changes. <br />
Run `main.py` file and the program will go perform all the above mentioned steps.
