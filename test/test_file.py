import fileman.file as file
from fileman import File

def test_by_ext():
    assert file.by_ext(ext="txt", folder="test_data") == ["test_data\\textfile_1.txt", "test_data\\textfile_2.txt"]
    assert file.by_ext(ext="csv", folder="test_data") == ["test_data\\data.csv"]

    f = File("test_data\\textfile_1.txt")
