import pytest
import sys
import os

@pytest.mark.skipif(sys.platform != "darwin", reason="Runs only on macOS")
def test_macos_only_feature():
    assert sys.platform == "darwin"

@pytest.mark.skipif(not os.path.exists("/etc/hosts"), reason="Requires /etc/hosts file")
def test_hosts_file_exists():
    assert os.path.exists("/etc/hosts")