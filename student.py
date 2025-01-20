"""
Module Name: student.py
Author: Yoel Baer Buzgalo
Created: 2025-01-19
Description:
    This module provides a helper class
"""

class Student:
    __slots__ = ["__name","__tasks"]
    def __init__(self, name, tasks):
        self.__name = name
        self.__tasks = tasks

    def __str__(self):
        return f"Student Name: {self.__name}<br>Topic Covered: {self.__tasks}"