# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Memory Sync Engine

Stage 2.7.5
"""


class VeterinaryMemorySyncEngine:

    VERSION = "1.0.0"

    def __init__(self, short_memory, long_memory):

        self.short_memory = short_memory

        self.long_memory = long_memory

    def sync_case(self, case):

        result = {"short_memory": False, "long_memory": False}

        try:

            self.short_memory.add_case(case)

            result["short_memory"] = True

        except Exception:

            pass

        try:

            self.long_memory.save_case(case)

            result["long_memory"] = True

        except Exception:

            pass

        result["synced"] = result["short_memory"] and result["long_memory"]

        return result

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Memory Sync Engine",
            "version": self.VERSION,
        }
