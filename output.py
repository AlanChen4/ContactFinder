'''
input keywords

output sites after search

output to csv

'''
import pandas as pd


links = [
    {'Name': 'Duke', 'Link': 'bla bla', 'Email(s)': 'stuff'},
    {'Name': 'Georgia Tech', 'Link': 'hahahaha', 'Email(s)': 'hellothere'},
    {'Name': 'NC State', 'Link': '2e98r232', 'Email(s)': 'hello there how are you'}
]

def to_csv(sites):
    # sites is a list of dictionaries
    return pd.DataFrame(sites)