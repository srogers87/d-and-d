import random

voice_qual = [
    "croaky",
    "breathy",
    "dead",
    "flat",
    "fruity",
    "grating",
    "high",
    "monotonous",
    "deep",
    "nasal",
    "booming",
    "gruff",
]

voice_accent = ["normal", "english", "irish", "scottish", "american", "wacky"]

forename_first_syll = [
    "And",
    "Pel",
    "Ter",
    "Tan",
    "Ab",
    "Okr",
    "Rem",
    "Dal",
    "Tar",
    "Lan",
    "Nol",
    "Ulf",
    "Col",
    "Xan",
    "Kur",
    "Er",
    "Quar",
    "Hoff",
    "Veyl",
    "Pul",
]

forename_second_syll = [
    "on",
    "el",
    "or",
    "rey",
    "ram",
    "ithe",
    "over",
    "'em",
    "yl",
    "ixe",
    "ig",
    "elon",
    "emon",
    "ek",
    "aw",
    "anel",
    "us",
    "yme",
    "ival",
    "RAND",
]

rand = ["a", "e", "i", "o", "u", ""]

surnames_first_syll = [
    "Far",
    "Short",
    "Tall",
    "Full",
    "Storm",
    "Hard",
    "Hill",
    "Clear",
    "Wild",
    "Dark",
    "High",
    "Low",
    "Bright",
    "Swift",
    "Oaken",
    "Dread",
    "Still",
    "Dawn",
    "Dusk",
    "Proud",
]

surnames_second_syll = [
    "church",
    "brook",
    "tree",
    "wood",
    "sea",
    "ridge",
    "stride",
    "river",
    "rider",
    "mane",
    "flame",
    "stone",
    "sworn",
    "seeker",
    "splitter",
    "bane",
    "jaw",
    "hammer",
    "water",
    "walker",
]

races = [
    "human",
    "human",
    "human",
    "human",
    "human",
    "human",
    "elf",
    "dwarf",
    "dwarf",
    "gnome",
    "halfling",
    "half-elf",
    "half-orc",
    "tiefling",
]

classes = [
    "barbarian",
    "bard",
    "cleric",
    "druid",
    "fighter",
    "monk",
    "paladin",
    "ranger",
    "rogue",
    "sorcerer",
    "warlock",
    "wizard",
]

professions = [
    "Actor",
    "Advocate",
    "Advisor",
    "Animal handler",
    "Apothecary",
    "Architect",
    "Archivist",
    "Armorer",
    "Astrologer",
    "Baker",
    "Banker",
    "Barber",
    "Barkeep",
    "Blacksmith",
    "Bookseller",
    "Brewer",
    "Bricklayer",
    "Brothel keeper",
    "Buccaneer",
    "Butcher",
    "Caravanner",
    "Carpenter",
    "Cartographer",
    "Chandler",
    "Chef",
    "Clock maker",
    "Cobbler",
    "Cook",
    "Counselor",
    "Courtesan",
    "Courtier",
    "Cowherd",
    "Dancer",
    "Diplomat",
    "Distiller",
    "Diver",
    "Farmer",
    "Fisherman",
    "Fishmonger",
    "Gardener",
    "General",
    "Gladiator",
    "Glovemaker",
    "Goldsmith",
    "Grocer",
    "Guardsman",
    "Guildmaster",
    "Hatmaker",
    "Healer",
    "Herald",
    "Herbalist",
    "Hermit",
    "Historian",
    "Hunter",
    "Ice seller",
    "Innkeeper",
    "Inventor",
    "Jailer",
    "Jester",
    "Jeweler",
    "Judge",
    "Knight",
    "Lady",
    "Leatherworker",
    "Librarian",
    "Linguist",
    "Locksmith",
    "Lord",
    "Lumberjack",
    "Mason",
    "Masseur",
    "Merchant",
    "Messenger",
    "Midwife",
    "Miller",
    "Miner",
    "Minister",
    "Minstrel",
    "Monk",
    "Mortician",
    "Necromancer",
    "Noble",
    "Nun",
    "Nurse",
    "Officer",
    "Painter",
    "Patissier",
    "Perfumer",
    "Philosopher",
    "Physician",
    "Pilgrim",
    "Potter",
    "Priest",
    "Privateer",
    "Professor",
    "Roofer",
    "Ropemaker",
    "Rugmaker",
    "Saddler",
    "Sailor",
    "Scabbard maker",
    "Sculptor",
    "Scavenger",
    "Scholar",
    "Seamstress",
    "Servant",
    "Shaman",
    "Shepherd",
    "Ship's captain",
    "Silversmith",
    "Slave",
    "Slaver",
    "Smith",
    "Soldier",
    "Spice Merchant",
    "Squire",
    "Stablehand",
    "Stevedore",
    "Stonemason",
    "Steward",
    "Street seller",
    "Street sweeper",
    "Student",
    "Surgeon",
    "Surveyor",
    "Sailor",
    "Tanner",
    "Tavernkeeper",
    "Tax collector",
    "Teacher",
    "Thatcher",
    "Thief",
    "Torturer",
    "Town crier",
    "Toymaker",
    "Vendor",
    "Veterinarian",
    "Vintner",
    "Weaver",
    "Wetnurse",
    "Woodcarver",
    "Wood seller",
    "Wrestler",
    "Writer",
]

features = [
    "distinctive jewelry",
    "piercings",
    "outlandish clothes",
    "formal clothes",
    "ragged clothes",
    "facial scar",
    "missing teeth",
    "missing fingers",
    "mixed eye colours",
    "tattoos",
    "birthmark",
    "unusual skin color",
    "bald head",
    "braided beard/hair",
    "unusual hair colour",
    "eye twitch",
    "distinctive nose",
    "distinctive posture",
    "exceptional beauty",
    "exceptional ugliness",
    "missing hand",
    "flashy amulet",
    "birthmark",
    "missing eye",
]


class NPC:
    def __init__(self):
        second_syll = random.choice(forename_second_syll)
        if second_syll == "RAND":
            second_syll = random.choice(rand)

        name = (
            random.choice(forename_first_syll)
            + second_syll
            + " "
            + random.choice(surnames_first_syll)
            + random.choice(surnames_second_syll)
        )
        race = random.choice(races)
        _class = random.choice(classes)
        gender = "male" if random.randrange(10) < 6 else "female"
        vq = random.choice(voice_qual)
        va = random.choice(voice_accent)
        voice = vq + "," + va
        feature = random.choice(features)

        profs = []
        for i in range(0, 5):
            prof = random.choice(professions)
            if prof not in profs:
                profs.append(prof)
            else:
                i += 0

        self.name = name
        self.location = None
        self.race = race
        self._class = _class
        self.gender = gender
        self.feature = feature
        self.voice = voice
        self.profs = profs

    def get_stats(self):
        template = """
		NAME: {},
		LOCATION: {},
		GENDER: {},
		RACE: {},
		CLASS: {},
		FEATURE: {},
		VOICE: {}
		PROFESSIONS: {}
		""".format(
            self.name,
            self.location,
            self.gender,
            self.race,
            self._class,
            self.feature,
            self.voice,
            self.profs,
        ).replace(
            "\t", ""
        )

        return template

    def save_npc_stats(self, name, template):
        attrs = vars(self)
        filename = name + ".txt"
        print("Outputting to " + filename)
        with open(filename, "w+") as outfile:
            outfile.write(template)


def main():
    while True:
        user_input = input("Press Enter to create an NPC or enter q to quit:\n")
        if user_input.strip().lower() == "q":
            quit()
        my_npc = NPC()
        force_race = input("Enter override race if desired or enter to skip > ")
        if force_race:
            my_npc.race = force_race
        force_prof = input("Enter override profession if desired or enter to skip > ")
        if force_prof:
            my_npc.profs = force_prof
        location = input("Add a location? > ")
        if (
            location
            and location.strip().lower() is not "n"
            and location.strip().lower() is not "no"
        ):
            my_npc.location = location

        stats = my_npc.get_stats()
        print(stats)
        user_input = input("Save NPC? > ")
        if user_input.strip().lower() == "y" or user_input.strip().lower() == "yes":
            my_npc.save_npc_stats(my_npc.name, stats)


if __name__ == "__main__":
    main()
