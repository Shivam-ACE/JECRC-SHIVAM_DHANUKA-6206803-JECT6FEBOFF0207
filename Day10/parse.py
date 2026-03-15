import pickle
file = open('temp11.txt', 'ab+')
data = {
    'fullname':'Shivam Dhanuka',
    'userid':87654321,
    'password':'******'
}
# print(f'original data: {data}')
# print(f'type of original data: {type(data)}')

enc_data = pickle.dumps(data)
file.write(enc_data)

file.seek(0)
enc_data = file.read()
print(type(enc_data))

ori_data = pickle.loads(enc_data)
print(ori_data, type(ori_data))

# print(f'encrypted data: {enc_data}')
# print(f'type of encrypted data: {type(enc_data)}')

# dec_data = pickle.loads(enc_data)

# print(f'decrypted data: {dec_data}')
# print(f'type of decrypted data: {type(dec_data)}')

file.close()