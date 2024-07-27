import pytest
from create_string.strings import print_hi


@pytest.mark.parametrize('log_file_name,expected', [("output1.log", "kappa 6.2.0 (Release) Mar 15 2021"),
                                                    ("output2.log", None)])
def test_string(log_file_name, expected):
    # assert linux_version("OS Version\\s*:\\s*(.*)", log_file_name) == expected
    assert print_hi("OS Version", log_file_name) == expected