import pandas as pd

data = pd.read_csv('corinnej_accessKeys.csv', skiprows = 1, names=['KeyID', 'AccessKey'])
key_value_pair = data.to_dict(orient='records')

# for pair in key_value_pair:
#     print(data)

first_pair = key_value_pair[0]
keyID = first_pair['KeyID']
accessKey = first_pair['AccessKey']

print(f"KeyID: {keyID}, AccessKey: {accessKey}")