def test_metadata_exists():
    import json, os
    assert os.path.exists("src/metadata/metadata_schema.json")
    with open("src/metadata/metadata_schema.json") as f:
        md = json.load(f)
    assert "orders" in md
