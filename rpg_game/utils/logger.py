"""
Logger module for the RPG game.
"""
import sys
import os
import datetime
from typing import Any

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))



class GameLogger:
    """
    GameLogger class to log combat and other game events.
    
    This class demonstrates association relationship with Game (solid line in UML).
    """
    
    def __init__(self, log_to_console: bool = True) -> None:
        """
        Initialize a new GameLogger.
        
        Args:
            log_to_console: Whether to print logs to the console
        """
        self.log_to_console = log_to_console
        self.logs = []  # Store all log messages
        
    def log(self, message: str) -> None:
        """
        Log a general message.
        
        Args:
            message: The message to log
        """
        if self.log_to_console:
            print(message)
        # Future enhancement: could log to file, database, etc.

    def log_combat(self, attacker: Any, defender: Any, damage: int) -> None:
        """
        Log a combat event.
        
        Args:
            attacker: The attacking character
            defender: The defending character
            damage: The amount of damage dealt
        """
        # Get current time for the log
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] COMBAT LOG: {attacker.name} attacked {defender.name} for {damage} damage"
        self.log(log_message)

    def log_level_up(self, character: Any) -> None:
        """
        Log a level up event.
        
        Args:
            character: The character that leveled up
        """
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] LEVEL UP: {character.name} reached level {character.level}!"
        self.log(log_message)

    def get_logs(self) -> list:
        """
        Get all logged messages.
        
        Returns:
            A list of logged messages
        """
        return self.logs
