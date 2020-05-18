class Fish:
    place = "aquarium"
    n_fish = 0  # number of fish in the aquarium

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        Fish.n_fish = Fish.n_fish + 1


greg = Fish("Greg", "guppy")
g1 = Fish('Aman', 'Madan')
g2 = Fish('Aman', 'Madan')

print(Fish.n_fish)