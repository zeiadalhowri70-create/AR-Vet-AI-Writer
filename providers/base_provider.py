# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass

    @abstractmethod
    def health(self):
        pass

    def info(self):

        return {"provider": self.__class__.__name__, "version": "1.0"}
