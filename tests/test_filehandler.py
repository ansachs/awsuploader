import unittest

from uploader.filehandler import *


class FileHandlerTests(unittest.TestCase):

    # @mock.patch('uploader.filehandler.os')
    # def test_list_files(self, mock_os):
    #     list_files('some path')
    #     mock_os.listdir.assert_called_with('some path')
    def setUp(self) -> None:
        self.test_dir = 'testdir/'


    def test_list_files(self):
        files = list_files(self.test_dir)
        self.assertEqual(len(files), 3)
        assert 'file3.txt' in files


if __name__ == '__main__':
    unittest.main()