from typing import List, Any

from .models import Record


class Stack:
    def __init__(self, obj_type: Any):
        self.__obj_type: Any = obj_type
        self.__stacks: List[obj_type] = []

    def add(self, obj: Record) -> bool:
        try:
            self.__stacks.append(obj)

            return True
        except Exception as e:
            return False

    def get(self) -> Record:
        try:
            obj = self.__stacks.pop(0)
            return obj
        except Exception as e: pass

    def is_empty(self):
        return len(self.__stacks) == 0
