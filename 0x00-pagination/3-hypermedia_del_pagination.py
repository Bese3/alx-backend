#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Implementing a get_hyper_index method with two integer
        arguments: index with a None default value
        """
        assert type(index) is int
        assert type(page_size) is int
        csv_file = self.indexed_dataset()
        data = []
        csv_size = len(csv_file)
        assert index > 0 and index < csv_size
        next_idx = index
        for _ in range(page_size):
            next_idx += 1
        for i in range(index, index + page_size):
            try:
                data.append(csv_file[i])
            except KeyError:
                next_idx += 1
                continue
        return {'index': index, 'data': data,
                'page_size': page_size, 'next_index': next_idx
                }
