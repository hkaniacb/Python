import random # program do debagowania fragmentu kodu znajdującego się w << with pysnooper.snoop() >>

# pip install pysnooper
import pysnooper

SIZE = 5
random_values_a = [random.randint(1, 100) for x in range(SIZE + 1)]
random_values_b = [random.randint(1, 100) for x in range(SIZE + 1)]
# debagowanie fragmentu kodu
with pysnooper.snoop():
    for (x, y) in zip(random_values_a, random_values_b):
        z = x + y / 2
