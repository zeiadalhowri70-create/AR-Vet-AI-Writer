# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Case Memory Engine

Stage 2.7.1
"""

from copy import deepcopy


class VeterinaryCaseMemoryEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.name = "Veterinary Case Memory Engine"
        self.cases = []

    def add_case(self, case):

        self.cases.append(deepcopy(case))

        return len(self.cases)

    def list_cases(self):

        return deepcopy(self.cases)

    def last_case(self):

        if not self.cases:
            return None

        return deepcopy(self.cases[-1])

    def count(self):

        return len(self.cases)

    def health(self):

        return {
            "status": True,
            "engine": self.name,
            "version": self.VERSION,
            "stored_cases": len(self.cases),
        }
