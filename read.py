data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))

print('檔案讀取完，總共有', len(data), '筆資料')


print(data[0])

word_count= {} 
for d in data:
	words = d.split()
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

for word in word_count:
	if word_count[word] > 1000000:
		print(word, word_count[word])

while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in word_count:
		print(word, '出現過的次數為: ', word_count[word])
	else:
		print('這個字沒有出現過喔')

print('謝謝使用本服務')


sum_len = 0
for d in data:
	sum_len += len(d)
print('每筆留言平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度<100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言有提到good')
print(good[0])