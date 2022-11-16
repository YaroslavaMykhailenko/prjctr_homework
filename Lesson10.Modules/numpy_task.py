import numpy as np

# 4. Write a script that imports numpy. Execute code from their site ([https://numpy.org/](https://numpy.org/)) and run it on local computer
# 5. As a result, you should send screenshot and archive with venv, requirements.txt and [numpy.py](http://numpy.py/)

x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99
print(x)

print(x.max(axis=1))

rng = np.random.default_rng()
samples = rng.normal(size=2500)
print(samples)