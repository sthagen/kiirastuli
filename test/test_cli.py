import kiirastuli.cli as cli


def test_parse_request_for_help():
    assert cli.parse_request([]) == 0
