import matplotlib.pyplot as plt
import sys
import math_lib
import matplotlib
matplotlib.use('Agg')


def boxplot(L, out_file_name):
    """Generates a boxplot from given data
    """
    if len(L) == 0:
        return None
    try:
        plt.figure()
        plt.boxplot(L)
        plt.xlabel('Box')
        plt.ylabel('Distribution')
        plt.title('Mean: %6.2f, Standard deviation: %6.2f' %
                  (math_lib.list_mean(L), math_lib.list_stdev(L)))
        plt.savefig(out_file_name, bbox_inches='tight')
        pass


def histogram(L, out_file_name):
    """Generates a histogram from given data
    """
    if len(L) == 0:
        return None
    try:
        plt.figure()
        plt.hist(L, bins=20)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Mean: %6.2f, Standard deviation: %6.2f' %
                  (math_lib.list_mean(L), math_lib.list_stdev(L)))
        plt.savefig(out_file_name, bbox_inches='tight')
        pass


def combo(L, out_file_name):
    """Generates boxplot and histogram from given data
    """
    if len(L) == 0:
        return None
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.boxplot(L)
        plt.xlabel('Value')
        plt.ylabel('Distribution')

        plt.subplot(1, 2, 2)
        plt.hist(L, bins=20)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.savefig(out_file_name, bbox_inches='tight')
        sys.exit
