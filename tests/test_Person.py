# -*- coding: utf-8 -*-
"""Tests for `bioinfo_course` package."""
import pytest
from bioinfo_course import bioinfo_course
from bioinfo_course.bioinfo_course import Person

# Test class for Person
class TestPerson:
    # Test the constructor (__init__) method
    def test_constructor(self):
        person = Person("Alice", 30)
        assert person.name == "Alice"
        assert person.age == 30

    # Test the greet method
    def test_greet(self):
        person = Person("Alice", 30)
        assert person.greet() == "Hello, my name is Alice and I am 30 years old."