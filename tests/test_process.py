from scripts.process import load_data, add_feature
import pandas as pd

def test_load_data(tmp_path):
    sample = tmp_path / "sample.csv"
    sample.write_text("id,x,value\n1,1,2\n2,2,4\n")
    df = load_data(str(sample))
    assert list(df.columns) == ["id", "x", "value"]
    assert len(df) == 2

def test_add_feature():
    df = pd.DataFrame({"x": [1, 2], "value": [2, 4]})
    out = add_feature(df)
    assert "z" in out.columns
    assert out.loc[0, "z"] == 2
    assert out.loc[1, "z"] == 8
