'''
input keywords

output sites after search

output to csv - done

filters through links and emails and exports as csv
'''
import pandas as pd
import os


class output():
    
    # Exports data to a csv with the file name: file_name
    def to_csv(self, file_name, data):
        if file_name[-4:] == '.csv':
            self._file_name = file_name[0 : (length(file_name) - 4)]
        else:
            self._file_name = file_name
        
        pd.DataFrame(data).to_csv(f'{self._file_name}.csv', index=False)
        print(f'Emails and links saved to {os.getcwd()} as {self._file_name}.csv')




if __name__ == '__main__':
	o = output()
	o.to_csv('thing', [
        {'Email(s)': 'stuff', 'Link': 'bla bla', 'Name': 'Duke'},
        {'Email(s)': 'hellothere', 'Link': 'hahahaha', 'Name': 'Georgia Tech'},
        {'Email(s)': 'hello there how are you', 'Link': '2e98r232', 'Name': 'NC State'}
        ])