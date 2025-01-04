# Analyzing Time Series Trends of Over 2 Million Historical Baby Name Records (1880 - 2022)
**Author:** Michelle Zong

This project examines over a century of baby name data from the Social Security Administration to uncover trends in naming patterns. Using object-oriented programming, dynamic helper functions, module imports, `pandas`, and `matplotlib`, this project processes over 140 data files, cleans and transforms 2,085,158 records, as well as calculates and visualizes time series trends. 


## Packages
- `pandas` for data manipulation and analysis (sorting, filtering, grouping, etc.)
- `matplotlib.pyplot` for line plots over time,  bar plot over time
- `os` for interacting with the operating system (files/directory management, input/output variables, etc.)
- `re` for pattern matching of regular expressions

## Techniques Used
- **Object-Oriented Programming:** Encapsulation of data processing, cleaning, manipulation, and visualization within the BabyNames class.
- **Dynamic Helper Functions:** retrieve_files: Scans directories to locate and collect paths for over 140 .txt files for processing. Can do so for any type of user inputted file extension.
- **Memory-efficient Processing:** of large datasets. record_loader_gen yields each record of the data files one at a time.
- **Module import and export:** Designed as a multi-module project, enabling the reuse of functions and classes across different .py files. Example: Helper functions from hf.py are imported and used in babynames.py.
- **Data Manipulation and Cleaning:** Uses Pandas for sorting, filtering, and transforming raw data into structured formats suitable for analysis.
- **Interactive Data Visualization:** Creates dynamic line and bar time series plots based on user interaction (e.g., selecting the unisex names user is interesting in seeing plotted over time, selecting the time range for male and female names over time).
- **Use of Regular Expression:** pattern matching to extract year from file names.

## Project Structure
```bash
BabyNames_timeSeriesTrends/
│
├── main.py
├── .gitignore
├── requirements.txt
├── README.md
├── SRC/
│   ├── babynames.py
│   ├── hf.py
├── Data/
│   ├── 1800s/
│   │   └── yob1880.txt
│   │   └── yob1881.txt
│   │   └── ...
│   ├── 1900s/
│   └── 2000s/
├── Tests/
```

## Source Code Overview
### main.py
Instantiates BabyNames class and calls methods in the BabyNames class. The `__init__()` method in BabyNames class calls on the helper functions `record_loader_gen(path_list)` and `retrieve_file(ext)` to initialize the object's (b1's) attributes. 

### hf.py
Helper functions that load data from over 140 .txt files, totalling 2,085,158 records.

- `retrieve_file(ext)`: Traverses every folder in project directory. Creates and returns a list containing the file path and name for every file with the extension given by the user. In this 
case, extension given was .txt. 
    -  **Args:** 
        - ext (str): file extension
    - **Return:** 
        - file_list (list): list of path/file_name.txt for every file that contains file extension specified

- `record_loader_gen(path_list)`: A generator that opens a file and yields each line from every file. Each record line it yields is composed of the name, gender, births, and year. Uses a regular expression to extract year from file name. Casts births and year into ints to do math on them later.
    - **Args:**
        - path_list (list): list of file-path names

    - **Return:**
        - name (str): name of row
        - sex (str): gender of row
        - births (int): number of births of row
        - year (int): corresponding year of row

### babynames.py
Class `BabyNames` that creates a Pandas DataFrame called names_df from all the rows outputted when using helper functions to load all yobxxxx.txt data files. Methods in this class plot visualizations and answer analytical questions about the data such as... aggregate male and female names over a dynamic range of time, the popularity over time of the 3 most popular names throughout history, total births for every unisex name over time, total births for every unisex name inputted by the user over time. 
- **Attributes:**
    - names_df (DataFrame): Pandas DataFrame of all yobxxxx.txt file data
- **Methods:**
    - `sort_data(self):` sorts names_df in ascending order by year (1880, 1881, etc.)
        - Args:
            - n/a
        - Return:
            - n/a
    - `m_f_names(self, start_yr=1880, end_yr=2022):` Calculates total number of male and female names for each year and creates a line plot. Only creates plot for the start and end years given when method is called.
        - Args:
            - start_yr (int): starting year of plot, default 1880
            - end_yr (int): ending year of plot, default 2022
        - Return:
            - n/a
    - `most_popular_ever(self):` for 3 most popular names, creates line plot for their popularity over time
        - Args:
            - n/a
        - Return:
            - n/a
    - `unisex(self):` Finds all unisex names (given to M and F). Calculates and plots (bar-plot) the total number of births for every unisex name over time.
        - Args:
            - n/a
        - Return:
            - n/a
    - `unisex_evolution(self):` Creates line plot for all unisex names inputted by user, over time
        - Args:
            - n/a
        - Return:
            - n/a

## How to Run

1. **Fork the Repository**:
   ```bash
   git fork https://github.com/mmzong/BabyNames_timeSeriesTrends.git
   ```

2. **Install Requirements**:
   ```bash
   pip install -r <path/to/requirements.txt>
   ```

3. **Run the Project**:
   ```bash
    python src/main.py
   ```

