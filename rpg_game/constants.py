"""
Constants for the RPG game.

This module contains all the constant values used throughout the game.
"""

from typing import Final

# Player constants
PLAYER_INITIAL_HEALTH: Final[int] = 110
PLAYER_INITIAL_DAMAGE: Final[int] = 10

# Boss constants
GOBLIN_KING_NAME: Final[str] = "Goblin King"
GOBLIN_KING_HEALTH: Final[int] = 50
GOBLIN_KING_DAMAGE: Final[int] = 8

DARK_SORCERER_NAME: Final[str] = "Dark Sorcerer"
DARK_SORCERER_HEALTH: Final[int] = 60
DARK_SORCERER_DAMAGE: Final[int] = 9

# Weapon constants
WEAPON_ROCK_NAME: Final[str] = "Rock"
WEAPON_ROCK_DAMAGE: Final[int] = 2

WEAPON_PAPER_NAME: Final[str] = "Paper"
WEAPON_PAPER_DAMAGE: Final[int] = 3

WEAPON_SCISSORS_NAME: Final[str] = "Scissors"
WEAPON_SCISSORS_DAMAGE: Final[int] = 4

# UI constants
SEPARATOR_LENGTH: Final[int] = 30
BORDER_LENGTH: Final[int] = 80

# Experience and Leveling constants
LEVEL_UP_EXP: Final[int] = 100
BASE_EXP_GAIN: Final[int] = 50
EXP_MULTIPLIER: Final[float] = 1.5

# Game messages
WELCOME_MESSAGE: Final[str] = (
    "🌟 Welcome, brave adventurer, to the RPG Adventure! 🌟\n"
    "Legends tell of heroes who rise against impossible odds—will you become one?"
)
INTRO_MESSAGE: Final[str] = (
    "In a realm shrouded in darkness and peril, you, {player_name}, have been chosen by fate.\n"
    "Two formidable bosses threaten the land: the ferocious Goblin King and the enigmatic Dark Sorcerer.\n"
    "Your journey will test your courage, wit, and strength. Gather your resolve—the fate of this world rests in your hands."
)

# Level messages
GOBLIN_KING_INTRO: Final[str] = (
    "🗡️ Level 1: The Goblin King's Lair 🗡️\n"
    "You step into a dank, torch-lit cavern echoing with guttural laughter.\n"
    "The Goblin King, infamous for his brute strength and savage cunning, awaits.\n"
    "Steel yourself, {player_name}, for this battle will be fierce and unforgiving!"
)
DARK_SORCERER_INTRO = (
    "🔮 Level 2: The Dark Sorcerer's Tower 🔮\n"
    "With the Goblin King fallen, you ascend a spiraling staircase into a chamber pulsing with arcane energy.\n"
    "The Dark Sorcerer, master of forbidden spells and illusions, greets you with a sinister grin.\n"
    "Only true heroes survive his magic. Face your fears, {player_name}, and let your legend grow!"
)

# Combat messages
VICTORY_MESSAGE = (
    "🏆 Triumph! 🏆\n"
    "With a final, decisive blow, you have vanquished {enemy_name}.\n"
    "The air crackles with your newfound power as the path ahead becomes clear."
)
DEFEAT_MESSAGE = (
    "💀 Defeat... 💀\n"
    "You fought valiantly, but {enemy_name} has bested you in battle.\n"
    "Every setback is a lesson—rise again, stronger than before!"
)
GAME_WIN_MESSAGE = (
    "🎉 Heroic Victory! 🎉\n"
    "All evil has been banished thanks to your bravery, {player_name}.\n"
    "The people rejoice, and songs will be sung of your deeds for generations to come!\n"
    "You are a true legend of the realm!"
)
GAME_OVER_MESSAGE = (
    "☠️ Game Over ☠️\n"
    "Though darkness prevails this day, the spirit of a true hero never fades.\n"
    "Rest and return, {player_name}—the world still needs you. Your next adventure awaits!"
)
