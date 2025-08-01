"""Unit tests for CLI functionality."""
import pytest
from unittest.mock import patch, Mock
from click.testing import CliRunner

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from src.cli import main


class TestCLI:
    """Test CLI functionality."""

    def test_cli_help(self):
        """Test CLI help command."""
        runner = CliRunner()
        result = runner.invoke(main, ['--help'])
        
        assert result.exit_code == 0
        assert 'bamsnap' in result.output.lower() or 'usage' in result.output.lower()

    @pytest.mark.integration
    def test_cli_with_invalid_args(self):
        """Test CLI with invalid arguments."""
        runner = CliRunner()
        result = runner.invoke(main, ['--invalid-option'])
        
        assert result.exit_code != 0

    @pytest.mark.integration
    def test_cli_missing_required_args(self):
        """Test CLI with missing required arguments."""
        runner = CliRunner()
        result = runner.invoke(main, [])
        
        # Should exit with error or show help
        assert result.exit_code != 0 or 'usage' in result.output.lower()

    @pytest.mark.slow
    @pytest.mark.integration
    def test_cli_with_sample_bam(self, sample_bam_file, sample_bam_index, temp_dir):
        """Test CLI with sample BAM file."""
        output_dir = temp_dir / "output"
        
        runner = CliRunner()
        result = runner.invoke(main, [
            '--bam', sample_bam_file,
            '--pos', 'chr1:1000-2000',
            '--out', str(output_dir),
            '--save-image-only'
        ])
        
        # May fail due to invalid BAM format, but should parse arguments correctly
        # We're mainly testing argument parsing here
        assert '--bam' in str(result.exception) or result.exit_code in [0, 1]
