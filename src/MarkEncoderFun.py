from sklearn import preprocessing

lable_encoder = preprocessing.LabelEncoder()

input_classes = ['audi', 'ford', 'audi', 'toyota', 'ford', 'bmw']

lable_encoder.fit(input_classes)

# word is marked with index
print("Class mapping :\n")
for i, item  in enumerate(lable_encoder.classes_) :
    print(item, '-->', i)

# find index from word
labels = ['toyota', 'ford', 'audi']
encoded_label = lable_encoder.transform(labels)
print ("Labels :", labels)
print ("Encoded Labels:", encoded_label)

# find word by index
indexs = [2, 1, 0, 3, 1]
encoded_indexs = lable_encoder.inverse_transform(indexs);
print ("Index :", indexs)
print ("Encoded Indexs:", encoded_indexs)


