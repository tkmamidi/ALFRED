import unittest
from src.conversation import Conversation

class TestConversation(unittest.TestCase):

    def setUp(self):
        self.conversation = Conversation()

    def test_process(self):
        # Test that process method returns correct output
        input_data = "Hello ALFRED"
        expected_output = "Hello User"
        actual_output = self.conversation.process(input_data)
        self.assertEqual(actual_output, expected_output)

    def test_respond(self):
        # Test that respond method returns correct output
        input_data = "What's the weather like?"
        expected_output = "I'm sorry, I can't provide weather updates at the moment."
        actual_output = self.conversation.respond(input_data)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()