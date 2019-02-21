import os.path


@dataclass
class Prediction:
    """Single two-team prediction from a student.
    """

    index: int = None
    unc: int = None
    duke: int = None

    @classmethod
    def generate(cls, iterator: List = None):
        """Yields self per row of input file."""
        for idx, item in enumerate(iterator):
            yield cls(index=idx, **item)


# __END__
