class Band:
    """Band class representing a collection of musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band and its musicians."""
        musician_details = "\n".join(str(musician) for musician in self.musicians)
        return f"{self.name}:\n{musician_details}"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing what each musician is playing."""
        return "\n".join(musician.play() for musician in self.musicians)