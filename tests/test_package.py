import re

import olfilereader


def test_olfilereader_has_version() -> None:
    assert re.match(r"\d+\.\d+\.\d+", olfilereader.__version__)
