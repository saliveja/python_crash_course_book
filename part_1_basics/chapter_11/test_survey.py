import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """Create a survey and a set of responses
        for use in all test methods."""
        # setUp() is only used within unittest
        # outside of this frame we use __init__()

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""

        self.my_survey.store_response(self.responses[0])
        # storing one response. The index is because this test is
        # designed to test a single response
        self.assertIn(self.responses[0], self.my_survey.responses)
        # self.assertIn verifies that the item is in the list

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""

        for response in self.responses:
            self.my_survey.store_response(response)
            # using a for loop to store the three answers

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
            # using a for loop to check so the three answers are in the list


if __name__ == '__main__':
    unittest.main()
