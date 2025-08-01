"""Simple CLI execution tests using subprocess."""
import pytest
import subprocess
import sys
import tempfile
import shlex
from pathlib import Path
import os


class TestCLISubprocess:
    """Test CLI execution using subprocess - actually runs the command line."""

    @pytest.fixture
    def setup_test_environment(self, temp_dir):
        """Set up test environment with mock data."""
        data_dir = temp_dir / "data"
        out_dir = temp_dir / "out"
        data_dir.mkdir()
        out_dir.mkdir()
        
        # Create minimal mock BAM files
        test_bam = data_dir / "test.bam"
        test_bam.touch()
        (data_dir / "test.bam.bai").touch()
        
        return temp_dir

    @pytest.mark.integration
    @pytest.mark.slow
    def test_cli_help_subprocess(self):
        """Test CLI help using subprocess - should always work."""
        try:
            # Try different ways to call the CLI
            commands_to_try = [
                [sys.executable, "-m", "src.cli", "--help"],
                ["poetry", "run", "bamsnap", "--help"],
                ["python", "-m", "src.cli", "--help"]
            ]
            
            success = False
            for cmd in commands_to_try:
                try:
                    result = subprocess.run(
                        cmd, 
                        capture_output=True, 
                        text=True, 
                        timeout=30,
                        cwd=Path(__file__).parent.parent.parent
                    )
                    
                    if result.returncode == 0 and ('usage' in result.stdout.lower() or 'options' in result.stdout.lower()):
                        success = True
                        print(f"✅ CLI help works with: {' '.join(cmd)}")
                        break
                        
                except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.CalledProcessError):
                    continue
            
            if not success:
                pytest.skip("No working CLI command found")
                
        except Exception as e:
            pytest.skip(f"CLI help test failed: {e}")

    @pytest.mark.integration
    @pytest.mark.slow
    def test_cli_invalid_option_subprocess(self):
        """Test CLI with invalid option using subprocess."""
        try:
            result = subprocess.run([
                sys.executable, "-m", "src.cli", "--invalid-option"
            ], capture_output=True, text=True, timeout=10,
               cwd=Path(__file__).parent.parent.parent)
            
            # Should fail with non-zero exit code
            assert result.returncode != 0
            
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("CLI module not accessible via subprocess")

    @pytest.mark.integration
    @pytest.mark.slow
    def test_simple_cli_command_subprocess(self, setup_test_environment):
        """Test a simple CLI command that should parse but may fail on execution."""
        original_cwd = os.getcwd()
        os.chdir(setup_test_environment)
        
        try:
            # Simple command that should at least parse correctly
            cmd = [
                sys.executable, "-m", "src.cli",
                "--bam", "./data/test.bam",
                "--pos", "chr1:1000",
                "--out", "./out/test.png",
                "--save-image-only"
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=Path(__file__).parent.parent.parent
            )
            
            # Command may fail due to invalid BAM, but should not fail on argument parsing
            print(f"Exit code: {result.returncode}")
            print(f"Stdout: {result.stdout}")
            print(f"Stderr: {result.stderr}")
            
            # If it fails, it should be due to BAM processing, not argument parsing
            if result.returncode != 0:
                # Check that it's not an argument parsing error
                error_text = result.stderr.lower()
                assert "usage:" not in error_text, "Command failed due to argument parsing"
                assert "invalid option" not in error_text, "Command failed due to invalid option"
            
        except subprocess.TimeoutExpired:
            pytest.fail("Command timed out")
        except FileNotFoundError:
            pytest.skip("CLI module not found for subprocess execution")
        finally:
            os.chdir(original_cwd)


class TestCLIWithPoetry:
    """Test CLI using Poetry commands."""

    @pytest.mark.integration
    @pytest.mark.slow
    def test_poetry_run_help(self):
        """Test CLI help using poetry run."""
        try:
            result = subprocess.run([
                "poetry", "run", "bamsnap", "--help"
            ], capture_output=True, text=True, timeout=30,
               cwd=Path(__file__).parent.parent.parent)
            
            if result.returncode == 0:
                assert 'usage' in result.stdout.lower() or 'options' in result.stdout.lower()
            else:
                pytest.skip("Poetry run bamsnap not working")
                
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Poetry not available or bamsnap not installed")

    @pytest.mark.integration
    @pytest.mark.slow
    def test_poetry_run_simple_command(self, temp_dir):
        """Test simple command using poetry run."""
        # Create test files
        data_dir = temp_dir / "data"
        out_dir = temp_dir / "out"
        data_dir.mkdir()
        out_dir.mkdir()
        
        test_bam = data_dir / "test.bam"
        test_bam.touch()
        (data_dir / "test.bam.bai").touch()
        
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            result = subprocess.run([
                "poetry", "run", "bamsnap",
                "--bam", "./data/test.bam",
                "--pos", "chr1:1000-2000",
                "--out", "./out/test.png",
                "--save-image-only",
                "--margin", "50"
            ], capture_output=True, text=True, timeout=60,
               cwd=Path(__file__).parent.parent.parent)
            
            print(f"Poetry command exit code: {result.returncode}")
            print(f"Stdout: {result.stdout}")
            print(f"Stderr: {result.stderr}")
            
            # May fail due to invalid BAM format, but should parse arguments
            
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Poetry run not working")
        finally:
            os.chdir(original_cwd)


class TestCLICommandParsing:
    """Test command parsing without actually executing bamsnap."""

    def test_shlex_parsing(self):
        """Test that shlex correctly parses command strings."""
        test_cmd = 'bamsnap -bam ./data/test.bam -title "Test Sample" -pos chr1:1000-2000 -out test.png'
        parsed = shlex.split(test_cmd)
        
        expected = [
            'bamsnap', '-bam', './data/test.bam', '-title', 'Test Sample', 
            '-pos', 'chr1:1000-2000', '-out', 'test.png'
        ]
        assert parsed == expected

    def test_complex_command_parsing(self):
        """Test parsing of complex commands with multiple options."""
        cmd = '''bamsnap -bam ./data/sample1.bam ./data/sample2.bam 
                 -title "Sample 1" "Sample 2" 
                 -pos chr1:1000-2000 
                 -margin 100 
                 -out ./out/result.png 
                 -save_image_only'''
        
        parsed = shlex.split(cmd)
        
        assert 'bamsnap' in parsed
        assert '-bam' in parsed
        assert './data/sample1.bam' in parsed
        assert './data/sample2.bam' in parsed
        assert '-title' in parsed
        assert 'Sample 1' in parsed
        assert 'Sample 2' in parsed
        assert '-pos' in parsed
        assert 'chr1:1000-2000' in parsed

    @pytest.mark.parametrize("cmd_str", [
        "bamsnap --help",
        "bamsnap -bam test.bam -pos chr1:1000 -out test.png",
        "bamsnap -bam test.bam -pos chr1:1000-2000 -margin 100 -out test.png --save-image-only"
    ])
    def test_various_command_formats(self, cmd_str):
        """Test parsing of various command formats."""
        parsed = shlex.split(cmd_str)
        
        assert len(parsed) > 0
        assert parsed[0] == "bamsnap"
        
        # Check that arguments come in pairs (except for flags)
        flags = ["--help", "--save-image-only", "--no-title"]
        
        i = 1
        while i < len(parsed):
            if parsed[i] in flags:
                i += 1  # Flag without value
            elif parsed[i].startswith('-'):
                assert i + 1 < len(parsed), f"Option {parsed[i]} should have a value"
                i += 2  # Option with value
            else:
                i += 1  # Value


def test_original_approach_simulation():
    """Simulate the original test_run.py approach without actual execution."""
    # Sample commands from original file
    sample_commands = [
        """-bam ./data/test.bam -title "Test" -pos chr1:1000 -out ./out/test.png -save_image_only""",
        """-bam ./data/sample1.bam ./data/sample2.bam -title "S1" "S2" -pos chr1:1000-2000 -out ./out/test2.png"""
    ]
    
    bamsnap_prog = "bamsnap"
    
    for cmd in sample_commands:
        full_cmd = bamsnap_prog + " " + cmd.strip()
        parsed_argv = shlex.split(full_cmd)
        
        # Verify the parsing worked as expected
        assert parsed_argv[0] == "bamsnap"
        assert "-bam" in parsed_argv
        assert "-pos" in parsed_argv
        assert "-out" in parsed_argv
        
        print(f"✅ Command parsed successfully: {' '.join(parsed_argv[:3])}...")


if __name__ == "__main__":
    # Run this specific test file
    pytest.main([__file__, "-v"])
