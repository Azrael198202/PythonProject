import numpy as np
from sklearn import preprocessing

data = np.array([[3, -1.5, 2, -5.4], [0, 4, -0.3, 2.1], [1, 3.3,-1.9, -4.3]])

# Mean removal
data_standardized = preprocessing.scale(data)
print ("\nMean =", data_standardized.mean(axis=0))
print ("Std deviation =", data_standardized.std(axis=0))

#scaling
data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled = data_scaler.fit_transform(data)
print("Min max scaled data =\n", data_scaled)

#normalization
data_normalized = preprocessing.normalize(data, norm="l1")
print ("L1 normalized data=\n", data_normalized)

#binarization
data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data)
print ("Binarized data =\n", data_binarized)

#one-hot encoding
encoder = preprocessing.OneHotEncoder()
encoder.fit([[0, 2, 1, 12], [1, 3, 5, 3], [2, 3, 2, 12], [1, 2, 4, 3]])
encoder_ventor = encoder.transform([[2, 3, 5, 3]]).toarray()
print ("Encoded ventor =\n", encoder_ventor)
