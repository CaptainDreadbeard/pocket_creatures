from pocket_creatures.pet import Pet

class Dragon(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Dragon"

    def update_stats(self):
        super.update_stats()
        # Dragons get hungry faster and lose energy quicker
        self.hunger = min(100, self.hunger + 2)
        self.energy = max(0, self.energy - 1)

    def get_mood(self):
        mood = super().get_mood()
        # Dragons get fiery when hungry or angry
        if self.hunger > 80:
            return "fiery"
        if self.cleanliness < 30:
            return "irritated"
        return mood 
    