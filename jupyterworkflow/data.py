import os
from urllib.request import urlretrieve
import pandas as pd

def get_freemont_data(filename, url, force_download):

	""" Download and cache data
	
	Parameters
	==========
	filename : string (mandatory)
		location to save the data, and name of the file
	url : string (mandatory)
		web address of the data
	force_download : bool (mandatory)
		if True, force redownload the data
		
	Returns
	=======
	data : pandas.DataFrame
		the freemont bridge data
		
	"""

	if force_download or not os.path.exists(filename):
		urlretrieve(url, filename)

	data = pd.read_csv(filename, index_col='Date', parse_dates=True)
	
	return data
