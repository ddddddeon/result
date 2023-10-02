class Result:
    __match_args__ = ("value",)

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"

    def unwrap(self):
        if isinstance(self, Ok):
            return self.value
        else:
            raise ValueError(f"Cannot unwrap an Err: {self.value!r}")


class Ok(Result):
    pass


class Err(Result):
    pass
