from single_tech_samples.sample_azuresql.src.transform import add


def test_add():
    assert 2 + 3 == add(2, 3)
