#!/usr/bin/env python3
"""Pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)


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
        """ Returns data paged
        """
        assert (type(page) == int), "page must be int"
        assert (type(page_size) == int), "page size must be int"
        assert (page > 0), "page must be grater than 0"
        assert (page_size > 0), "page size must be grater than 0"
        dataSize = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, dataSize)
        if start >= dataSize:
            return []
        return self.dataset()[start:end]
