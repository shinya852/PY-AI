import sklearn.datasets #skleanには事前に大量のテストデータが入っている為今回使用

digits = sklearn.datasets.load_digits()

print("データの個数=",len(digits.images))
print("画像データ=",digits.images[1])#画像データーの表示
print("何の数字か=",digits.target[1])#上記データーが何の数字を表示してあるかを表示

#画像データは数字として表示される
