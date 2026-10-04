"""
Unit tests for the EmotionDetection package.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for emotion_detector function.
    """

    def test_emotion_detector(self):
        """
        Verify that emotion_detector correctly identifies the dominant emotion.
        """
        # Test case 1: Joy
        res_1 = emotion_detector("I am glad this happened")
        self.assertEqual(res_1['dominant_emotion'], 'joy')

        # Test case 2: Anger
        res_2 = emotion_detector("I am really mad about this")
        self.assertEqual(res_2['dominant_emotion'], 'anger')

        # Test case 3: Disgust
        res_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res_3['dominant_emotion'], 'disgust')

        # Test case 4: Sadness
        res_4 = emotion_detector("I am so sad about this")
        self.assertEqual(res_4['dominant_emotion'], 'sadness')

        # Test case 5: Fear
        res_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res_5['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
