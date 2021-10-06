#import libraries
import pandas as pd #used to read the files
import seaborn as sns #for visualization but here we used to get heatmap

class preprocess:
    """
    This class is used to preprocess data
        1. file reading
        2. renaming columns
        3. finding difference between high and low columns
    """

    file = "E:\python assignment\HDFCBANK_01-01-2021_27-09-2021.csv"

    def file_reading(self):
        """
        Method name : file_reading
        Description : this is used to read the file using read_csv function

        written by : Mallela Divya

        """
        data = pd.read_csv(self.file)
        return data

    def col_rename(self, data):
        """
        Method name : col_rename
        Description : this is used to rename the columns using rename function
        :param data: file which was read
        :return: data which renamed the columns

        written by : Mallela Divya
        """
        dict1 = {
            'Date': 'date',
            'High Price': 'high',
            'Low Price': 'low',
            'Total Traded Quantity': 'trade',
            'Turnover (in lacs)': 'turnover_in_lakhs',
            'No. of Contracts': 'contracts'}
        data.rename(columns=dict1, inplace=True)
        return data

    def add_new_column(self, data):
        """
                Method name : add_new_column
                Description : this is used to add difference column to the existing data frame
                :param data: file which was read
                :return: data which added a new column

                written by : Mallela Divya
                """
        difference = data['high'] - data['low']
        data['difference'] = difference
        return data

    def file_save(self, data):
        """
                Method name : file_save
                Description : this is used to save the file which is preprocessed using to_csv function
                return :  saved file

                written by : Mallela Divya
                """
        file = data.to_csv('processed_data.csv', index=False)
        return file

    def find_correlation(self, final_data):
        """
        Method name : find_correlation
        Description : To find the correlation and plotting the heatmap using seaborn library of the final_data
        :param final_data
        :return: image

        written by: Mallela Divya
        """
        corr_plot = sns.heatmap(final_data.corr(), annot=True)
        return corr_plot