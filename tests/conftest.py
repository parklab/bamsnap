"""Shared pytest fixtures and test configuration."""
import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, MagicMock
import sys

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_bam_file(temp_dir):
    """Create a sample BAM file path for testing."""
    bam_path = temp_dir / "sample.bam"
    # Create empty file for testing file existence
    bam_path.touch()
    return str(bam_path)


@pytest.fixture
def sample_bam_index(sample_bam_file):
    """Create a sample BAM index file."""
    index_path = sample_bam_file + ".bai"
    Path(index_path).touch()
    return index_path


@pytest.fixture
def sample_bamlist_file(temp_dir, sample_bam_file):
    """Create a sample bamlist file for testing."""
    bamlist_path = temp_dir / "bamlist.txt"
    bamlist_content = f"""# This is a comment
{sample_bam_file}\tSample1
{sample_bam_file}\tSample2
"""
    bamlist_path.write_text(bamlist_content)
    return str(bamlist_path)


@pytest.fixture
def mock_logger():
    """Mock logger for testing."""
    logger = Mock()
    logger.info = Mock()
    logger.debug = Mock()
    logger.warning = Mock()
    logger.error = Mock()
    return logger


@pytest.fixture
def mock_options(mock_logger):
    """Mock options dictionary for testing."""
    return {
        'bam': [],
        'bamlist': None,
        'title': [],
        'ref': None,
        'poslist': [
            {'chrom': 'chr1', 't_pos': 12345, 'g_spos': 12000, 'g_epos': 12700},
            {'chrom': '2', 't_spos': 23000, 't_epos': 23500, 'g_spos': 22500, 'g_epos': 24000},
        ],
        'process': 2,
        'out': '/tmp/test_output',
        'margin': 100,
        'width': 1000,
        'height': 600,
        'imagetype': 'png',
        'separated_bam': False,
        'log': mock_logger,
        'plot_margin_left': 0,
        'plot_margin_right': 0,
        'plot_margin_top': 20,
        'plot_margin_bottom': 20,
    }


@pytest.fixture
def sample_positions():
    """Sample genomic positions for testing."""
    return [
        {'chrom': 'chr1', 't_pos': 12345, 'g_spos': 12000, 'g_epos': 12700},
        {'chrom': 'chr2', 't_spos': 23000, 't_epos': 23500, 'g_spos': 22500, 'g_epos': 24000},
        {'chrom': '3', 't_pos': 45678, 'g_spos': 45000, 'g_epos': 46000},
        {'chrom': 'chrX', 't_spos': 67000, 't_epos': 67200, 'g_spos': 66800, 'g_epos': 67400},
    ]


@pytest.fixture
def mock_bam_object():
    """Mock BAM object for testing."""
    bam = Mock()
    bam.filename = "/path/to/sample.bam"
    bam.title = "Sample BAM"
    bam.title2 = "Sample_BAM"
    bam.setReference = Mock()
    return bam
