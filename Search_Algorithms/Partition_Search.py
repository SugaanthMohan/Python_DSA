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
        self.low = min(set(container_))
        self.high = max(set(container_))
        self.pidx = pidx
        self.elements = container_

    def __repr__(self):
        return "Pid: {pid} with range {low} => {high}".format(
            low=self.low,
            high=self.high,
            pid=self.pidx
        )

    def __str__(self):
        return "Pid: {pid} with range {low} => {high}".format(
            low=self.low,
            high=self.high,
            pid=self.pidx
        )


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
            list(
                itertools.starmap(
                    self.create_partition,
                    enumerate(np.array_split(container_, partitions_count))
                )
            )
        )

    def search_partition(self, element):

        my_partition = list(
            filter(
                lambda x: x.low <= element <= x.high,
                self.partitions
            )
        )

        return my_partition[0].pidx, np.where(my_partition[0].elements, element)


if __name__ == '__main__':
    List = np.arange(1000)
    partitions = 10
    my_ds = PartitionList(List, partitions)
    print(my_ds.search_partition(30))
