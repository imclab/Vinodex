import django
from django.utils import unittest
from unittest_helper import UnitTestHelper

@unittest.skip("Annotation has not yet been implemented")
class AnnotationTestCase(django.test.TestCase):

    def setUp(self):
        self.helper = UnitTestHelper(self)

    def test_can_create_annotation(self):
        self.fail("Not implemented")

    def test_can_delete_annotation(self):
        self.fail("Not implemented")

    def test_can_update_annotation(self):
        self.fail("Not implemented")

    def test_can_get_annotation(self):
        self.fail("Not implemented")

    def test_annotation_key_cannot_be_null(self):
        self.fail("Not implemented")

    def test_annotation_key_must_be_unique_to_bottle(self):
        self.fail("Not implemented")

