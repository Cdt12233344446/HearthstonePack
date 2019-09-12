"""Simple snippet for analysing results."""

from scipy.stats import beta
import numpy as np

alpha = np.ones((4,), dtype=int)


def listeval(string):
    """`Eval()` for list-like inputs."""
    return eval("[" + string.replace(" ", ",") + "]")


def update(array, _array, n=1):
    """Update `array` with input data."""
    _array += [n * 100 - sum(_array)]
    return array + np.array(_array)


if __name__ == "__main__":
    para = listeval(input())
    for i in range(para.pop(0)):
        alpha = update(alpha, listeval(input()), n=para[i])

    # print('\033c', end='')
    print("Updated probability:")
    for i in range(len(alpha)):
        rv = beta(alpha[i], sum(alpha)-alpha[i])
        print("{:.3%}, ({:.3%}, {:.3%})".format(rv.mean(),
                                                rv.interval(0.95)[0],
                                                rv.interval(0.95)[1]))

    print("In comparison, standard prior probability is:",
          "1.00%", "4.00%", "20.00%", "75.00%", sep='\n')
