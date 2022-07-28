"""
Similarly structured code was used to process metadata of artworks and compute
features which were subsequently used in a multi-criteria decision-making algorithm.

Following snippet is to showcase parallel processing of a dictionary.
"""

from multiprocessing import Manager
import concurrent.futures

dictionary = {
    0: {},
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
}

sub_dictionary = Manager().dict()


def processing(x, subdict):
    subdict[x] = {'square': x ** 2, 'cube': x ** 3, 'square_root': np.sqrt(x)}


with concurrent.futures.ProcessPoolExecutor() as executor:
    for i in dictionary:
        executor.submit(process_artwork, i, subdict)
