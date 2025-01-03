import pandas as pd
import matplotlib.pyplot as plt

# import when running from main.py file
from SRC.hf import retrieve_file, record_loader_gen

# import if running from this file
# from helper_functions.hf import retrieve_file, record_loader_gen


# To output full tables without truncation:
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


class BabyNames:
    """
    A class that creates a Pandas DataFrame called names_df from
    all the rows outputted when using helper functions to load
    the data from all yobxxxx.txt files within the baby_names
    folder.


    Attributes:
    -----------
        names_df (DataFrame): Pandas DataFrame of all yobxxxx.txt file data

    Methods:
    --------
        sort_data: sorts names_df by year
        m_f_names: creates line plot for total M and F names for the given years
        most_popular_ever: for 3 most popular names, creates line plot for their popularity over time
        unisex: bar-plot for all unisex names over time
        unisex_evolution: Creates line plot for all unisex names inputted by user, over time
    """

    def __init__(self):
        row_list = []
        for row in record_loader_gen(retrieve_file('.txt')):
            row_list.append(row)
        self.names_df = pd.DataFrame(row_list)
        # print(self.names_df.sample(5))
        self.names_df.columns = ['Name', 'Sex', 'Births', 'Year']
        self.sort_data()

    def sort_data(self):
        """
        Sorts names_df DataFrame in ascending order by year (1880, 1881, etc.).

        Args:
            n/a

        Return:
            n/a
        """
        # to check pandas DataFrame created when print(b1) in if name = main.
        # return print(self.names_df)
        self.names_df = self.names_df.sort_values(by='Year', ascending=True)
        # print(self.names_df)
        # print(self.names_df.shape[0]) # prints number of records via main.py print(b1)
        return

    def m_f_names(self, start_yr=1880, end_yr=2022):
        """
        Calculates total number of male and female names for each year and
        creates a line plot. Only creates plot for the start and end years
        given when method is called.

        Args:
            start_yr (int): starting year of plot, default 1880
            end_yr (int): ending year of plot, default 2022

        Return:
            n/a
        """
        subset_df = self.names_df[(self.names_df['Year'] >= start_yr) & (self.names_df['Year'] <= end_yr)]
        # Unstack transforms given column from being vertical rows, to being horizontal columns,
        # which become the 2 lines plotted.
        grouped_df = subset_df.groupby(['Year', 'Sex']).sum(['Births']).unstack('Sex')
        # First group, 'Year' is automatically made new index, this resets it to be 0-X. Not needed after unstack.
        # grouped_df = grouped_df.reset_index()

        # Plotting data and labeling axes
        grouped_df.plot()
        plt.title('Total Births by Sex and Year')
        plt.xlabel('Year')
        plt.ylabel('Total Births')
        plt.legend(title='total births, sex')
        plt.grid()
        plt.show()
        # print(grouped_df.head(10))
        return

    def most_popular_ever(self):
        """
        Calculates the 3 most popular names throughout history and
        creates a line plot of their popularity over the years.

        Args:
            n/a

        Return:
            n/a
        """
        # grouped_df = self.names_df.groupby(['Name'])['Births'].sum().reset_index()
        grouped_df = self.names_df.groupby(['Name'], as_index=False).agg({'Births': 'sum', 'Year': 'first'})
        grouped_df.columns = ['Name', 'Total Births', 'Year']

        sorted_df = grouped_df.sort_values(by='Total Births', ascending=False)
        # top_3 = sorted_df.iloc[:3]

        # Assign value of top three names to an object
        num_1 = sorted_df.iloc[0, 0]
        num_2 = sorted_df.iloc[1, 0]
        num_3 = sorted_df.iloc[2, 0]

        # From original grab all rows where Name column equivalent to top 3 names of all time in sorted_df
        subset_df = self.names_df[(self.names_df['Name'] == num_1) |
                                  (self.names_df['Name'] == num_2) | (self.names_df['Name'] == num_3)]

        subset_df = subset_df.groupby(['Year', 'Name']).sum(['Births']).unstack('Name')

        # Plotting data and labeling axes
        subset_df.plot()
        plt.title('Top 3 Most Popular Names')
        plt.xlabel('Year')
        plt.ylabel('Total Births')
        plt.legend(title='total births, name')
        plt.show()
        # print(subset_df.head())
        return

    def unisex(self):
        """
        Finds all unisex names (given to M and F). Calculates and plots
        (bar-plot) the total number of births for every unisex name
        over time.

        Args:
            n/a

        Return:
            n/a
        """
        # subset df into set of M names and F names. Create set unisex_names by intersection of M and F sets.
        # A set does not contain duplicates
        m_subset_df = set(self.names_df[(self.names_df['Sex'] == 'M')]['Name'])
        f_subset_df = set(self.names_df[(self.names_df['Sex'] == 'F')]['Name'])
        # print(m_subset_df)
        # print(f_subset_df)
        unisex_names = m_subset_df.intersection(f_subset_df)
        # print(type(unisex_names))
        # print(len(unisex_names))

        subset_df = self.names_df[(self.names_df['Name'].isin(unisex_names))]
        subset_df2 = subset_df.groupby(['Year']).sum(['Births'])
        # print(subset_df2)

        subset_df2.plot(kind='bar')
        plt.title('Gender Neutral Names Over Time')
        plt.xlabel('Year')
        plt.ylabel('Births')
        plt.show()

        return

    def unisex_evolution(self):
        """
        Adds all unisex names to a set (same as what is done at
        beginning of unisex method). Prints set of unisex names
        and asks user to input as many names as they want until
        they enter 'q'. Everytime a user enters a name, this method
        checks whether it is within the unisex set before storing it.
        For all names user inputs, plots the number births over time
        in one line plot.

        Args:
            n/a

        Return:
            n/a
        """
        m_subset_df = set(self.names_df[(self.names_df['Sex'] == 'M')]['Name'])
        f_subset_df = set(self.names_df[(self.names_df['Sex'] == 'F')]['Name'])
        # print(m_subset_df)
        # print(f_subset_df)
        unisex_names = m_subset_df.intersection(f_subset_df)
        print(unisex_names)

        input_list = []
        while True:
            user_input = input('Please enter unisex names you want to see the evolution of: ')
            if user_input == 'q':
                break
            if user_input not in unisex_names:
                print('This name does not exist, please enter another')
                continue
            input_list.append(user_input)
        print(input_list)

        for name in input_list:
            subset_df = self.names_df[(self.names_df['Name'] == name)]
            subset_df2 = subset_df.groupby(['Year']).sum(['Births'])
            plt.plot(subset_df2, label=f'{name} births')

        plt.title('Gender Neutral Names')
        plt.xlabel('Year')
        plt.ylabel('Births')
        plt.legend()
        plt.grid()
        plt.show()
        return


if __name__ == "__main__":
    b1 = BabyNames()

    # Testing pandas DataFrame created in init with return print(self.names_df) in sort_data
    print(b1)

    # Testing m_f_names subsets, groups, and plots names_df correctly. Yes.
    # print(b1.m_f_names(1880, 2022))
    # print(b1.m_f_names(1920, 1950))

    # Testing most_popular_ever grouped, subset, and plot correctly. Yes.
    # print(b1.most_popular_ever())

    # Testing unisex grouped, subset, and plot correctly. Yes
    # print(b1.unisex())

    # Testing unisex_evolution
    # print(b1.unisex_evolution())
    pass
