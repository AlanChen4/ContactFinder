import pandas as pd
import os


class output():
    '''filters through links and emails and exports as csv'''

    # Initialize data frame with data dictionary that has links, emails, keywords, etc.
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    # Exports data to a csv with the called file_name.csv
    def to_csv(self, file_name):
        if file_name[-4:] == '.csv':
            self._file_name = file_name[: (len(file_name) - 4)]
        else:
            self._file_name = file_name
        
        self.df.to_csv(f'{self._file_name}.csv', index=False)
        print(f'Emails and links saved to {os.getcwd()} as {self._file_name}.csv')
    
if __name__ == '__main__':
	o = output([
        {'Email(s)': 'stuff', 'Link': 'bla bla', 'Name': 'Duke', 'Keywords': 'ha, na, ma'},
        {'Email(s)': 'hellothere', 'Link': 'hahahaha', 'Name': 'Georgia Tech', 'Keywords': 'ha, na, ma'},
        {'Email(s)': 'hello there how are you', 'Link': '2e98r232', 'Name': 'NC State', 'Keywords': 'ha, na, ma'}
        ])