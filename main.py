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
    def __init__(self, name, job, race, creature_type):
        self.name = name
        self.job = job
        self.creature_type = creature_type
        self.race = race
        self.stats = CreatureStats()
        self.armour_class = randint(8, 12)
        self.hit_points = randint(10, 20)

    def display_info(self):
        print(f"\n"
              f"\nNom: {self.name}"
              f"\nProfession: {self.job}"
              f"\nRace: {self.race}"
              f"\nType de creature: {self.creature_type}"
              f"\nPoints de vie: {self.hit_points}"
              f"\n"
              f"\nStats de {self.name}:"
              f"\n\tForce: {self.stats.strength}"
              f"\n\tAgilité: {self.stats.dexterity}"
              f"\n\tConstitution: {self.stats.constitution}"
              f"\n\tIntelligence: {self.stats.intelligence}"
              f"\n\tSagesse: {self.stats.wisdom}"
              f"\n\tCharisme: {self.stats.charisma}"
              f"\n")


class Kobold(NPC):
    def __init__(self, name, job):
        super().__init__(name, job, "Kobold", "Humanoïde")
        self.proficiency_bonus = 2

    def attack(self, target, target_ac):
        d20 = randint(1, 20)
        dagger_hit = d20 + self.stats.dexterity_modifier + self.proficiency_bonus

        if d20 == 1:
            return 0

        elif target_ac > dagger_hit:
            return 0

        elif target_ac <= dagger_hit:
            dagger_damage = randint(1, 4) + self.stats.dexterity_modifier
            return dagger_damage

        elif d20 == 20:
            dagger_damage = randint(1, 4) + randint(1, 4) + self.stats.dexterity_modifier
            return dagger_damage

    def receive_damage(self, to_hit, damage):
        if to_hit < self.armour_class:
            pass

        elif to_hit >= self.armour_class:
            self.hit_points -= damage

        elif to_hit:
            self.hit_points -= damage


class Hero(NPC):
    def __init__(self, name, job, race, creature_type):
        super().__init__(name, job, race, creature_type)
        self.proficiency_bonus = 2
        self.shield = 2
        self.armour_class += self.shield

    def attack(self, target, target_ac):
        d20 = randint(1, 20)
        longsword_hit = d20 + self.stats.dexterity_modifier + self.proficiency_bonus

        if d20 == 1:
            return 0

        elif target_ac > longsword_hit:
            return 0

        elif target_ac <= longsword_hit:
            longsword_damage = randint(1, 4) + self.stats.strength_modifier
            return longsword_damage

        elif d20 == 20:
            longsword_damage = randint(1, 4) + randint(1, 4) + self.stats.strength_modifier
            return longsword_damage

    def receive_damage(self, to_hit, damage):
        if to_hit < self.armour_class:
            self.hit_points -= 0

        elif to_hit >= self.armour_class:
            self.hit_points -= damage

        elif to_hit:
            self.hit_points -= damage
