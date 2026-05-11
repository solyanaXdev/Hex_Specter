from backend.hex_specter.analyzer import analyze_file

def test_basic():
    class File:
        filename = "test.png"

    result = analyze_file(File())
    assert result["status"] == "analyzed"
