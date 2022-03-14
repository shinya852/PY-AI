import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

for i in range(50):#・・・50回繰り返す
    plt.subplot(5, 10, i + 1)#・・・iに1を足しながら5*10表示を行う
    plt.axis("off")#・・・枠線を非表示
    plt.title(digits.target[i])#数字の定義　ここではiを表示
    plt.imshow(digits.images[i], cmap="Greys")
plt.show()

#50個の数字を学習完了
