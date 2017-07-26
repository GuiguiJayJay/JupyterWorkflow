import os
from urllib.request import urlretrieve
import pandas as pd

FREEMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_freemont_data(filename='freemont.csv', url=FREEMONT_URL, force_download=False):

	""" Download and cache data
	
	Parameters
	==========
	filename : string (optional)
		location to save the data, and name of the file
	url : string (optional)
		web address of the data
	force_download : bool (optional)
		if True, force redownload the data
		
	Returns
	=======
	data : pandas.DataFrame
		the freemont bridge data
		
	"""

	if force_download or not os.path.exists(filename):
		urlretrieve(url, filename)

	data = pd.read_csv(filename, index_col='Date', parse_dates=True)
	data.columns = ['West','East']
	data['Total'] = data['West'] + data['East']
	
	return data
