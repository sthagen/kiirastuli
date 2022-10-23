import kiirastuli.kiirastuli as api


def test_humanize_mass():
    assert api.humanize_mass(0) == ('0', 'total bytes')


def test_humanize_duration():
    assert api.humanize_duration(0) == ('0.000', 'millis')
