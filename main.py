"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Exercice POO héritage
"""
from random import randint
from dataclasses import dataclass

print("TP4.2 - POO héritage\n")


def stat_calculation():
    first_d6 = randint(1, 6)
    second_d6 = randint(1, 6)
    third_d6 = randint(1, 6)
    fourth_d6 = randint(1, 6)

    smallest = min(first_d6, second_d6, third_d6, fourth_d6)
    return first_d6 + second_d6 + third_d6 + fourth_d6 - smallest


@dataclass
class CreatureStats:
    strength: int = stat_calculation()
    dexterity: int = stat_calculation()
    constitution: int = stat_calculation()
    intelligence: int = stat_calculation()
    wisdom: int = stat_calculation()
    charisma: int = stat_calculation()

    strength_modifier: int = (strength - 10) // 2
    dexterity_modifier: int = (dexterity - 10) // 2
    constitution_modifier: int = (constitution - 10) // 2
    intelligence_modifier: int = (intelligence - 10) // 2
    wisdom_modifier: int = (wisdom - 10) // 2
    charisma_modifier: int = (charisma - 10) // 2


class NPC:
    def __init__(self, name, job, creature_type, race):
        self.name = name
        self.job = job
        self.creature_type = creature_type
        self.race = race
        self.stats = CreatureStats()
        self.armour_class = 12

    def display_info(self):
        print(f"\n"
              f"\nNom: {self.name}"
              f"\nProfession: {self.job}"
              f"\nType de creature: {self.creature_type}"
              f"\nRace: {self.race}"
              f"\n"
              f"\nStats de {self.name}:"
              f"\n\tForce: {self.stats.strength}"
              f"\n\tAgilité: {self.stats.dexterity}"
              f"\n\tConstitution: {self.stats.constitution}"
              f"\n\tIntelligence: {self.stats.intelligence}"
              f"\n\tSagesse: {self.stats.wisdom}"
              f"\n\tCharisme: {self.stats.charisma}"
              f"\n")


test = NPC("Kerzin", "Forgeron", "Humanoïde", "Nain")
test.display_info()
