import scipy

database = scipy.io.readsav('D:/istks.sav')
print(database.keys())
istks = database['istks']
continuum = database['continuum']
print(istks.shape)
print(continuum.shape)