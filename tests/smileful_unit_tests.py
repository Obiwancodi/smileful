import os
import unittest
from urlparse import urlparse

os.environ["CONFIG_PATH"] = "smileful.config.TestingConfig"
import smileful
from smileful import calculate_score


