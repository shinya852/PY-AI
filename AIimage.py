#データを画像化して表示
import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

plt.imshow(digits.images[0], cmap="Greens")#数値データーを緑の濃淡画像にする。Greensの部分を変更すると色が変更できる []内の数字を変更すると該当数字を画像化。今回の場合は0
plt.show()

