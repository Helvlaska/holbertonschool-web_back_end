#!/usr/bin/env python3
"""
Utilitaire de pagination : retourne (start, end) pour une page.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retourne (start, end) pour une page 1-indexée ; end est exclusif."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
