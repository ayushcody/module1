"""
Emotion Detection Package.

This package provides an emotion detector function that analyzes text
using IBM Watson NLP EmotionPredict service.
"""
# pylint: disable=invalid-name
from .emotion_detection import emotion_detector

__all__ = ['emotion_detector']
