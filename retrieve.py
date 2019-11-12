from urllib.request import urlretrieve
#import kaggle


URL = 'http://archive.ics.uci.edu/ml/datasets/Census-Income+%28KDD%29'
DESTINATION = 'data/Census-Income-KDD.csv'
#save the data locally
#urlretrieve(URL, DESTINATION)

URL2 = 'https://doi.org/10.18128/D030.V6.0'
DEST2 = 'data/income-by-age.csv'
#urlretrieve(URL2, DEST2)

KAGGLE_DATASET_NAME = 'Cost_of_living_index.csv'
DEST3 = 'data/cost-of-living-index.csv'
#kaggle.api.authenticate()
#kaggle.api.dataset_download_files(KAGGLE_DATASET_NAME, path=DEST3, unzip=True)

URL4 = 'https://query.data.world/s/re44tlfff26tqpvbfwyhromhvfn6n6'
DEST4 = 'data/loan-balance-by-age.csv'
urlretrieve(URL4, DEST4)

URL5 =  'https://query.data.world/s/weco4xt7qvy2gf4oce5e7467cq3y7h'
DEST5 = 'data/debt-amount-distribution-2014.csv'
urlretrieve(URL5, DEST5)

URL6 = 'https://query.data.world/s/7l24f7cxtcvl5v3dtfdelnec4r5xc7'
DEST6 = 'data/non-mort-balance.csv'
urlretrieve(URL6, DEST6)
print('Done')
