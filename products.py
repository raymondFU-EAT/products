products = [] # 設立一個資料庫products
while True: # 進行迴圈(因為需要重複詢問'商品名稱'和'商品價格')
	name = input('請輸入商品名稱')
	if name == 'q': # 如果再'商品名稱'欄位輸入'q'
		break # 離開迴圈
	price = input('請輸入商品價格')
	products.append([name, price]) # 把'商品名稱'和'商品價格'一起包裝後再放入上面的products資料庫中
print(products) 

for p in products: # 用'p'迴路資料庫products
	print('商品', p[0], '價格', p[1]) # 印出所有在products中的資料,一格一格輸出

with open('products.csv', 'w', encoding='utf-8') as f: # 創造一個資料夾'products.csv'並且寫入資料,並且用coding'utf-s'(國際通用編碼程式)寫入資料
	f.write('商品, 價格\n') # 寫入第一欄'商品,價格'空格
	for p in products: # 設立一個迴圈'p',把products丟入
		f.write(p[0] +  ',' + p[1] + '\n') # 把迴圈讀出來的資料寫入新創的csv資料中
