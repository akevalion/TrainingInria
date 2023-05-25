import analyzer
import os
from unittest import TestCase

class TestNumberOfRequestInFile(TestCase):
    def setUp(self) -> None:
        self.request = "/list"
        self.content = "2023-05-25T13:28,GET,"+self.request
        self.filename = "test_file.log" #asking for tempfile
        with open(self.filename, "w") as the_file:
            the_file.write(self.content)

    def tearDown(self):
        os.remove(self.filename)

    def test_number_of_request_for_line_one(self):
        result = analyzer.find_number_of_requests(self.filename, self.request)
        assert result == 1

def test_number_of_requests_in_file():
    request = "/list"
    content = "2023-05-25T13:28,GET,"+request
    filename = "test_file.log"
    with open(filename, "w") as the_file:
        the_file.write(content)
    assert analyzer.find_number_of_requests(filename, request)
    os.remove(filename)

def test_count_number_of_requests():
    request = "/list"
    contents = [
        "2023-05-25T13:28,GET,"+request, 
        "2023-05-25T13:28,GET,/post" ]
    result = analyzer.count_number_of_requests_in_string(contents, request)
    assert result == 1


