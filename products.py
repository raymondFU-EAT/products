import os # operating system
products = [] # 設立一個資料庫products
if os.path.isfile('products.csv'): # 收尋檔案
	print('恭喜找到檔案!')
	with open('products.csv', 'r', encoding='utf-8') as f:# 讀取資料
	    for line in f:
		    if '商品, 價格' in line:
			    continue
		    name,price = line.strip().split(',') # 一行一行的資料,strip剔除空格,split切割列
		    products.append([name, price])         

else:
	print('沒找到檔案喔!')

# 讓使用者輸入
while True: # 進行迴圈(因為需要重複詢問'商品名稱'和'商品價格')
	name = input('請輸入商品名稱')
	if name == 'q': # 如果再'商品名稱'欄位輸入'q'
		break # 離開迴圈
	price = input('請輸入商品價格')
	products.append([name, price]) # 把'商品名稱'和'商品價格'一起包裝後再放入上面的products資料庫中
print(products) 

# 印出檔案
for p in products: # 用'p'迴路資料庫products
	print('商品', p[0], '價格', p[1]) # 印出所有在products中的資料,一格一格輸出

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: # 創造一個資料夾'products.csv'並且寫入資料,並且用coding'utf-s'(國際通用編碼程式)寫入資料
	f.write('商品, 價格\n') # 寫入第一欄'商品,價格'空格
	for p in products: # 設立一個迴圈'p',把products丟入
		f.write(p[0] +  ',' + p[1] + '\n') # 把迴圈讀出來的資料寫入新創的csv資料中
