"""Unit tests for BamSnap class."""
import pytest
from unittest.mock import Mock, patch, mock_open

from src.bamsnap import BamSnap


class TestBamSnap:
    """Test BamSnap class methods."""

    def test_get_split_poslist_empty(self):
        """Test get_split_poslist with empty position list."""
        bamsnap = BamSnap.__new__(BamSnap)  # Create without __init__
        result = bamsnap.get_split_poslist([], 4)
        assert result == {}

    def test_get_split_poslist_round_robin(self):
        """Test get_split_poslist distributes positions correctly."""
        bamsnap = BamSnap.__new__(BamSnap)
        positions = [1, 2, 3, 4, 5, 6, 7]
        result = bamsnap.get_split_poslist(positions, 3)
        
        expected = {
            0: [1, 4, 7],
            1: [2, 5],
            2: [3, 6]
        }
        assert result == expected

    def test_get_split_poslist_more_processes_than_positions(self):
        """Test behavior when more processes than positions."""
        bamsnap = BamSnap.__new__(BamSnap)
        positions = [1, 2]
        result = bamsnap.get_split_poslist(positions, 5)
        
        expected = {
            0: [1],
            1: [2],
            2: [],
            3: [],
            4: []
        }
        assert result == expected

    def test_get_split_poslist_single_process(self):
        """Test with single process."""
        bamsnap = BamSnap.__new__(BamSnap)
        positions = [1, 2, 3, 4, 5]
        result = bamsnap.get_split_poslist(positions, 1)
        
        expected = {0: [1, 2, 3, 4, 5]}
        assert result == expected

    