#!/usr/bin/env python3
"""retreving data using  index range method"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function `index_range` calculates the starting and
    ending indices for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        The function `get_page` retrieves a specific page of data from a
        dataset, based on the given page number and page size.
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        s, e = index_range(page, page_size)
        csv = len(self.dataset())
        if s > csv or e > csv:
            return []
        return self.dataset()[s:e]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        The function `get_hyper` returns a dictionary containing information
        about a paginated dataset, including the current page, page size, data
        on the current page, and links to the next and previous pages.
        """
        new_dict = {'page_size': 0, 'page': 0,
                    'data': [], 'next_page': 0,
                    'prev_page': 0, 'total_pages': 0}
        p = self.get_page(page, page_size)
        new_dict['page_size'] = len(p)
        new_dict['page'] = page
        new_dict['data'] = p
        total_pages = math.ceil(len(self.dataset()) / page_size)
        new_dict['next_page'] = page + 1 if page + 1 < total_pages else None
        new_dict['prev_page'] = page - 1 if page > 1 else None
        new_dict['total_pages'] = total_pages
        return new_dict
