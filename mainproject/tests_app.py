import unittest
from unittest.mock import patch
import app

class TestMainFunctions(unittest.TestCase):
    def setUp(self):
        with patch('app.input', return_value='q'):
            app.main()

    def test_move_documents(self):
        with patch('app.input', side_effect=['11-2', '4']):
            app.move_documents(app.directories)
        self.assertIn('11-2', app.directories.get('4'))
    
    def test_add_documents(self):
        with patch('app.input', side_effect=['passport', '422041', 'Lavrentiev Dmitrii', '2']):
            app.add_documents(app.documents, app.directories)
        self.assertIn('422041', app.directories.get('2'))
        search_values = []
        for data in app.documents:
            for values in data.values():
                search_values.append(values)
        self.assertIn('422041', search_values)
        self.assertIn('Lavrentiev Dmitrii', search_values)

    def test_delete_documents(self):
        with patch('app.input', return_value='2207 876234'):
            app.delete_documents(app.documents, app.directories)
        search_values_docs = []
        search_values_dirs = []
        for data in app.documents:
            for values in data.values():
                search_values_docs.append(values)
        for values in app.directories.values():
            search_values_dirs.append(values)
        self.assertIsNot('2207 876234', search_values_docs)
        self.assertIsNot('2207 876234', search_values_dirs)

    def test_shelf_number(self):
        with patch('app.input', return_value='2207 876234'):
            app.shelf_number(app.directories)
        self.assertIn('1', app.directories.keys())



if __name__ == "__main__":
    unittest.main()