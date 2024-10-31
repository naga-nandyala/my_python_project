import pandas as pd

from e2e_samples.fabric_sample.src.datapipeline_code.transform import read_csv, transform_data


def test_read_csv(monkeypatch):
    # Mock the pd.read_csv function
    def mock_read_csv(file_name):
        return pd.DataFrame({"name": ["Alice", "Bob"], "salary": [50000, 60000]})

    monkeypatch.setattr(pd, "read_csv", mock_read_csv)

    df = read_csv("dummy_path")
    assert not df.empty
    assert list(df.columns) == ["name", "salary"]
    assert df["name"].tolist() == ["Alice", "Bob"]


def test_transform_data():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "salary": [50000, 60000]})

    transformed_df = transform_data(df)
    assert not transformed_df.empty
    assert list(transformed_df.columns) == ["name", "salary"]
    assert transformed_df["name"].tolist() == ["Alice", "Bob"]


# 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
