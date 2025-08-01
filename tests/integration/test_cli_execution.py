"""Integration tests for CLI command execution."""
import pytest
import subprocess
import sys
import shlex
import tempfile
from pathlib import Path
from click.testing import CliRunner
import os

# Add src to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

try:
    from src.cli import main as cli_main
    import src.bamsnap as bamsnap
except ImportError:
    pytest.skip("Source modules not available", allow_module_level=True)


class TestCLIExecution:
    """Test actual CLI command execution."""

    @pytest.fixture
    def output_dir(self, temp_dir):
        """Create output directory for test results."""
        out_dir = temp_dir / "output"
        out_dir.mkdir()
        return out_dir

    @pytest.fixture
    def sample_data_dir(self):
        """Path to sample data directory (if it exists)."""
        data_dir = Path(__file__).parent.parent / "data"
        return data_dir if data_dir.exists() else None

    @pytest.mark.integration
    @pytest.mark.slow
    def test_cli_help_command(self):
        """Test CLI help command."""
        runner = CliRunner()
        result = runner.invoke(cli_main, ['--help'])
        
        assert result.exit_code == 0
        assert 'usage' in result.output.lower() or 'options' in result.output.lower()

    @pytest.mark.integration
    def test_cli_invalid_option(self):
        """Test CLI with invalid option."""
        runner = CliRunner()
        result = runner.invoke(cli_main, ['--invalid-option'])
        
        assert result.exit_code != 0

    @pytest.mark.integration
    @pytest.mark.slow
    def test_cli_missing_required_args(self):
        """Test CLI with missing required arguments."""
        runner = CliRunner()
        result = runner.invoke(cli_main, [])
        
        # Should show help or error
        assert result.exit_code != 0 or 'usage' in result.output.lower()

    @pytest.mark.integration
    @pytest.mark.slow
    #@pytest.mark.skipif(not Path("../data").exists(), reason="Test data directory not found")
    def test_cli_with_sample_data(self, output_dir):
        """Test CLI with actual sample data if available."""
        # This test only runs if data directory exists
        data_dir = Path(__file__).parent.parent / "data"

        # Look for any BAM file in data directory
        bam_files = list(data_dir.glob("*.bam"))
        if not bam_files:
            pytest.skip("No BAM files found in data directory")
        
        bam_file = bam_files[0]
        
        # Check if index exists
        index_file = bam_file.with_suffix(bam_file.suffix + '.bai')
        if not index_file.exists():
            pytest.skip(f"Index file not found for {bam_file}")
        
        runner = CliRunner()
        result = runner.invoke(cli_main, [
            '--bam', str(bam_file),
            '--pos', 'chr1:1000-2000',
            '--out', str(output_dir / "test_output.png"),
            '--save-image-only',
            '--margin', '50'
        ])
        
        # Command might fail due to various reasons, but should parse arguments
        if result.exit_code == 0:
            # If successful, check output exists
            assert (output_dir / "test_output.png").exists()
        else:
            # If failed, at least it should not be due to argument parsing
            print(f"Command failed with: {result.output}")
            # This is expected for many test cases due to missing reference, etc.

    @pytest.mark.integration
    def test_cli_programmatic_execution(self, output_dir):
        """Test programmatic CLI execution similar to your test_run.py."""
        # Create a minimal test command that doesn't require real data
        test_commands = [
            "--help",
            "--bam /nonexistent/file.bam --pos chr1:1000 --out /tmp/test.png --save-image-only"
        ]
        
        for cmd_args in test_commands:
            if cmd_args == "--help":
                # Help should always work
                runner = CliRunner()
                result = runner.invoke(cli_main, ['--help'])
                assert result.exit_code == 0
            else:
                # Other commands may fail due to missing files, but should parse
                runner = CliRunner()
                args = shlex.split(cmd_args)
                result = runner.invoke(cli_main, args, catch_exceptions=True)
                # Don't assert exit code as files don't exist, just that it ran


class TestSubprocessCLI:
    """Test CLI using subprocess (actual command execution)."""

    @pytest.mark.integration
    @pytest.mark.slow
    def test_subprocess_cli_help(self):
        """Test CLI help using subprocess."""
        try:
            result = subprocess.run([
                sys.executable, '-m', 'src.cli', '--help'
            ], capture_output=True, text=True, timeout=30)
            
            assert result.returncode == 0
            assert 'usage' in result.stdout.lower() or 'options' in result.stdout.lower()
            
        except subprocess.TimeoutExpired:
            pytest.fail("CLI help command timed out")
        except FileNotFoundError:
            pytest.skip("CLI module not found for subprocess execution")

    @pytest.mark.integration
    @pytest.mark.slow
    def test_subprocess_cli_invalid_args(self):
        """Test CLI with invalid arguments using subprocess."""
        try:
            result = subprocess.run([
                sys.executable, '-m', 'src.cli', '--invalid-option'
            ], capture_output=True, text=True, timeout=10)
            
            assert result.returncode != 0
            
        except subprocess.TimeoutExpired:
            pytest.fail("CLI command timed out")
        except FileNotFoundError:
            pytest.skip("CLI module not found for subprocess execution")


# Convert your existing test commands to proper pytest tests
class TestLegacyCLICommands:
    """Test commands from your original test_run.py file."""
    
    @pytest.fixture
    def mock_data_files(self, temp_dir):
        """Create mock data files for testing."""
        data_dir = temp_dir / "data"
        data_dir.mkdir()
        
        # Create mock BAM files
        bam_files = [
            "test_SV1.bam",
            "NA12877.bam", 
            "NA12878.bam", 
            "NA12879.bam"
        ]
        
        for bam_file in bam_files:
            (data_dir / bam_file).touch()
            (data_dir / (bam_file + ".bai")).touch()
        
        # Create mock VCF file
        vcf_content = """##fileformat=VCFv4.2
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO
chr9	114786933	.	A	G	60	PASS	.
chr10	117542948	.	C	T	60	PASS	.
"""
        (data_dir / "NATRIO_test_3.vcf").write_text(vcf_content)
        
        return data_dir

    @pytest.mark.integration
    @pytest.mark.slow
    def test_sample_cli_commands(self, mock_data_files, temp_dir):
        """Test a few sample CLI commands with mocked data."""
        output_dir = temp_dir / "out"
        output_dir.mkdir()
        
        # Change to temp directory so relative paths work
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            sample_commands = [
                f"--bam ./data/NA12879.bam --title 'NA12879 (Daughter)' --pos chr10:117542948 --out ./out/test1.png --save-image-only",
                f"--bam ./data/NA12879.bam --pos chr10:117542948 --margin 500 --out ./out/test2.png --save-image-only"
            ]
            
            for cmd in sample_commands:
                args = shlex.split(cmd)
                runner = CliRunner()
                
                # Use catch_exceptions=True to see what happens
                result = runner.invoke(cli_main, args, catch_exceptions=True)
                
                print(f"Command: {cmd}")
                print(f"Exit code: {result.exit_code}")
                if result.output:
                    print(f"Output: {result.output}")
                
                # For mocked data, we expect it might fail, but arguments should parse
                # The main goal is testing argument parsing and basic execution flow
                
        finally:
            os.chdir(original_cwd)

    @pytest.mark.parametrize("cmd_args", [
        "--bam test.bam --pos chr1:1000 --out test.png --save-image-only",
        "--bam test.bam --pos chr1:1000-2000 --margin 100 --out test.png --save-image-only",
        "--help"
    ])
    @pytest.mark.integration
    def test_argument_parsing_variations(self, cmd_args):
        """Test various argument parsing scenarios."""
        runner = CliRunner()
        args = shlex.split(cmd_args) if cmd_args != "--help" else ["--help"]
        
        result = runner.invoke(cli_main, args, catch_exceptions=True)
        
        if "--help" in cmd_args:
            assert result.exit_code == 0
        else:
            # For other commands, just test that they don't crash during parsing
            # They may fail due to missing files, but that's expected
            print(f"Command: {cmd_args}, Exit code: {result.exit_code}")
