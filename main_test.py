# TODO working on unit testing
# when actually running it gives time with 02:00:00
# but in test it produces 02:00
#Carter
import unittest
from unittest.mock import patch
from io import StringIO
from Event import Event

class TestMain(unittest.TestCase):
    def setUp(self):
        self.event = Event('Testing Event', '04/02/2024', '01:00', '02:00', 'None')

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        self.event.display()
        expected_output = '\nEvent: Testing Event\nDate: 04/02/2024\nStart Time: 01:00:00\nEnd Time: 02:00:00\nDescription: None'   
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        

if __name__ == '__main__':
    unittest.main()
