from pytest import mark

import olfilereader


@mark.e2e
def test_olfilereader_read_text() -> None:
    with olfilereader.TextReader("tests/fixtures/data/text.txt") as reader:
        for idx, chunk in enumerate(reader):
            assert chunk == ["Hello, world!\n", "Hello olfilereader.\n"][idx]
