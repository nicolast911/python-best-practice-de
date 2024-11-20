from dataclasses import dataclass, field
from typing import Optional

@dataclass
class One:  # a recipe
    aaa: str  # name
    bbb: list[str]  # list of ingredients
    ccc: str  # instructions
    ddd: Optional[int] = None  # rating


@dataclass
class Many:
    foo: list[One] = field(default_factory=list)

    def add_thing(self, thing: One):
        self.foo.append(thing)

    def get_thing(self, aaa: str) -> One:
        for thing in self.foo:
            if thing.aaa == aaa:
                return thing
        raise KeyError(f"recipe {aaa} not found!")

    def get_things_1(self, bbb: str) -> list[One]:
        result = []
        for thing in self.foo:
            if bbb in thing.bbb:
                result.append(thing)
        return result

    def get_things_2(self, ddd: int) -> list[One]:
        result = []
        for thing in self.foo:
            if thing.ddd == ddd:
                result.append(thing)
        return result

    def get_things_3(self, ddd: int) -> list[One]:
        result = []
        for thing in self.foo:
            if thing.ddd is None or thing.ddd >= ddd:
                result.append(thing)
        return result