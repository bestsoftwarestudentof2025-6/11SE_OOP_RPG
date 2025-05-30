"""
Character module for the RPG game.

This module contains the Character base class and the Boss subclass.
"""
import sys
import os
from typing import Optional, Union

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rpg_game.inventory import Weapon, Inventory
from rpg_game.utils.logger import GameLogger

# Experience system constants
LEVEL_UP_EXP = 100  # Experience needed to level up
EXP_MULTIPLIER = 1.2  # Multiplier for stats when leveling up


class Character:
    """
    Represents a game character with health, damage, and weapon attributes.
    
    This class demonstrates encapsulation with private attributes and getter/setter methods.
    """
    
    def __init__(
        self, 
        name: str, 
        health: int, 
        damage: int, 
        weapon_name: Optional[str] = None, 
        weapon_damage: int = 0,
        level: int = 1,
        experience: int = 0,
        max_inventory_size: int = 10
    ) -> None:
        """
        Initialize a new Character.
        
        Args:
            name: The character's name
            health: The character's initial health
            damage: The character's base damage
            weapon_name: The name of the character's weapon (optional)
            weapon_damage: The damage bonus of the character's weapon
            level: The character's current level
            experience: The character's current experience points
            max_inventory_size: Maximum size of the character's inventory
        """
        self.name = name
        self._health = health
        self.damage = damage
        self.weapon = Weapon(weapon_name, f"A {weapon_name} weapon", weapon_damage) if weapon_name else None
        self.inventory = Inventory(max_inventory_size)
        self.level = level
        self.experience = experience

    # Getter for health - provides controlled access to the private attribute
    def get_health(self) -> int:
        """
        Get the character's current health.
        
        Returns:
            The character's current health
        """
        return self._health
    
    # Setter for health with validation - ensures health is never negative
    def set_health(self, new_health: int) -> None:
        """
        Set the character's health with validation.
        
        Args:
            new_health: The new health value
        """
        if new_health < 0:
            self._health = 0
        else:
            self._health = new_health

    # Method for the character to attack an enemy
    def attack(self, enemy: 'Character', logger: Optional[GameLogger] = None) -> tuple[int, bool]:
        """
        Attack another character.
        
        Args:
            enemy: The character to attack
            logger: Optional logger to log the combat
            
        Returns:
            A tuple containing:
            - The total damage dealt
            - A boolean indicating if the enemy was defeated
        """
        total_damage = self.damage + (self.weapon.damage if self.weapon else 0)
        # Use getter and setter instead of direct attribute access
        current_health = enemy.get_health()
        enemy.set_health(current_health - total_damage)
        enemy_defeated = enemy.get_health() <= 0
        
        # Use the logger if provided (dependency), otherwise fall back to static method
        if logger:
            logger.log_combat(self, enemy, total_damage)
        
        # If enemy is defeated, gain experience
        if enemy_defeated:
            # Store current experience before gaining more
            current_exp = self.experience
            self.gain_experience(LEVEL_UP_EXP, logger)  # Use LEVEL_UP_EXP constant
            if logger:
                logger.log(f"{self.name} defeated {enemy.name} and gained {LEVEL_UP_EXP} experience points!")
                logger.log(f"Total experience: {current_exp + LEVEL_UP_EXP}")
        
        return total_damage, enemy_defeated

    def gain_experience(self, amount: int, logger: Optional[GameLogger] = None) -> bool:
        """
        Gain experience points and potentially level up.
        
        Args:
            amount: The amount of experience to gain
            logger: Optional logger to log the experience gain
            
        Returns:
            True if the character leveled up, False otherwise
        """
        if amount < 0:
            if logger:
                logger.log(f"{self.name} attempted to gain negative experience. Ignoring.")
            return False
            
        self.experience += amount
        leveled_up = False
        
        while self.experience >= LEVEL_UP_EXP:
            # Store remaining experience after level up
            remaining_exp = self.experience - LEVEL_UP_EXP
            self.experience = remaining_exp
            self.level += 1
            self._health = int(self._health * EXP_MULTIPLIER)
            self.damage = int(self.damage * EXP_MULTIPLIER)
            leveled_up = True
            
            # Log level up details
            if logger:
                logger.log(f"{self.name} leveled up to level {self.level}!")
                logger.log(f"New stats: Health={self.get_health()}, Damage={self.damage}")
                logger.log(f"Remaining experience: {remaining_exp}")
            
        if logger:
            logger.log(f"{self.name} gained {amount} experience points. Total: {self.experience}")
            
        return leveled_up

    # Method to display character information
    def display(self) -> None:
        """Display the character's information."""
        weapon_name = self.weapon.name if self.weapon else 'No Weapon'
        weapon_damage = self.weapon.damage_bonus if self.weapon else 0
        # Use getter instead of direct attribute access
        print(f"Name: {self.name}\nHealth: {self.get_health()}\nDamage: {self.damage}\nWeapon: {weapon_name} (+{weapon_damage} Damage)")


class Boss(Character):
    """
    Represents a boss character with enhanced abilities.
    
    This class demonstrates inheritance and method overriding.
    """
    
    def __init__(
        self, 
        name: str, 
        health: int, 
        damage: int, 
        special_ability: Optional[str] = None,
        weapon_name: Optional[str] = None, 
        weapon_damage: int = 0,
        level: int = 1,
        experience: int = 0
    ) -> None:
        """
        Initialize a new Boss character.
        
        Args:
            name: The boss's name
            health: The boss's initial health
            damage: The boss's base damage
            special_ability: The boss's special ability
            weapon_name: The name of the boss's weapon (optional)
            weapon_damage: The damage bonus of the boss's weapon
        """
        super().__init__(name, health, damage, weapon_name, weapon_damage, level=level, experience=experience)
        self.special_ability = special_ability

    def use_special_ability(self) -> str:
        """
        Use the boss's special ability.
        
        Returns:
            A string describing the special ability's effect
        """
        if self.special_ability:
            return f"{self.name} uses {self.special_ability}!"
        return f"{self.name} has no special ability."

class Sidekick(Character):
    """
    Represents a helpful sidekick character.
    
    This class demonstrates inheritance and additional helper methods.
    """
    
    def __init__(
        self, 
        name: str, 
        health: int, 
        damage: int, 
        weapon_name: Optional[str] = None, 
        weapon_damage: int = 0,
        support_ability: Optional[str] = None,
        level: int = 1,
        experience: int = 0
    ) -> None:
        """
        Initialize a new Sidekick character.
        
        Args:
            name: The sidekick's name
            health: The sidekick's initial health
            damage: The sidekick's base damage
            weapon_name: The name of the sidekick's weapon (optional)
            weapon_damage: The damage bonus of the sidekick's weapon
            support_ability: The sidekick's support ability
        """
        super().__init__(name, health, damage, weapon_name, weapon_damage, level=level, experience=experience)
        self.support_ability = support_ability

    def use_support_ability(self) -> str:
        """
        Use the sidekick's support ability.
        
        Returns:
            A string describing the support ability's effect
        """
        if self.support_ability:
            return f"{self.name} uses {self.support_ability}!"
        return f"{self.name} has no support ability."

class Villain(Character):
    """
    Represents a villain character.
    
    This class demonstrates inheritance and additional malicious behaviors.
    """
    
    def __init__(
        self, 
        name: str, 
        health: int, 
        damage: int, 
        evil_deed: Optional[str] = None,
        weapon_name: Optional[str] = None, 
        weapon_damage: int = 0,
        level: int = 1,
        experience: int = 0
    ) -> None:
        """
        Initialize a new Villain character.
        
        Args:
            name: The villain's name
            health: The villain's initial health
            damage: The villain's base damage
            evil_deed: The villain's evil deed
            weapon_name: The name of the villain's weapon (optional)
            weapon_damage: The damage bonus of the villain's weapon
        """
        super().__init__(name, health, damage, weapon_name, weapon_damage, level=level, experience=experience)
        self.evil_deed = evil_deed

    def commit_evil_deed(self) -> str:
        """
        Have the villain commit an evil deed.
        
        Returns:
            A string describing the evil deed
        """
        if self.evil_deed:
            return f"{self.name} commits {self.evil_deed}!"
        return f"{self.name} has no evil deed."
