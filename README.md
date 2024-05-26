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

### Environment and package setup
1. Create a python virtual environment or choose one that you want. <br />
    `python -m venv <virtual_environment_name>` <br />
2. Activate the virtual environment <br />
    In terminal go to the folder where the virtual environment was created then run the following command <br />
    `source <virtual_environment_name>/bin/activate` <br />
    replace `<virtual_environment_name>` with your environment name. <br />
3. Run the following command in your terminal to install the package. <br />
    `pip install -r requirement.txt` <br />
    > If this does not work, add version to all the packages name like `pandas==1.1.3` or manually install the packages from terminal example: `pip install pandas`

### To Run
After you have made all the necessary changes. <br />
Run `main.py` file and the program will go perform all the above mentioned steps.
