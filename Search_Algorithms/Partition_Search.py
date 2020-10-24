"""
"""

from Utils import Shuffler
import numpy as np
import itertools


class Partition:

    __slots__ = (
        'low',
        'high',
        'pidx',
        'elements'
    )

    def __init__(self, pidx, container_):
        self.low = min(container_)
        self.high = max(container_)
        self.pidx = pidx
        self.elements = container_


class PartitionList:
    __slots__ = (
        'partitions',
        'p_count'
    )

    @staticmethod
    def create_partition(partition_idx, partition):
        return Partition(partition_idx, partition)

    def __init__(self, container_, partitions_count):

        self.p_count = partitions_count
        self.partitions = np.array(
            [
                itertools.starmap(
                    self.create_partition,
                    enumerate(np.array_split(container_, partitions_count))
                )
            ]
        )

    def search_partition(self, element):

        my_parition = np.array(
            filter(
                lambda x: x[1].low <= element <= x[1].high,
                self.partitions
            )
        )

        return {
            "PN": my_parition[0],
            "PN_IDX": np.where(my_parition[1] == element)
        }


if __name__ == '__main__':
    List = np.arange(1000)
    partitions = 10
    my_ds = PartitionList(List, partitions)
    for item in my_ds.partitions:
    #print(my_ds.search_partition(30))

