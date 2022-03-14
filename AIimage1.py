#データを画像化して表示
import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

plt.imshow(digits.images[1], cmap="Blues")
plt.show()
