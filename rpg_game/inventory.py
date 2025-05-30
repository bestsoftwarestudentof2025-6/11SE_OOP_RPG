"""
Inventory system for managing items and equipment.
"""

class Item:
    """Base class for all items."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class Weapon(Item):
    """Weapon item that can be equipped."""
    def __init__(self, name: str, description: str, damage: int):
        super().__init__(name, description)
        self.damage = damage

class Armor(Item):
    """Armor item that provides defense."""
    def __init__(self, name: str, description: str, defense: int):
        super().__init__(name, description)
        self.defense = defense

class Consumable(Item):
    """Consumable item that provides temporary effects."""
    def __init__(self, name: str, description: str, effect: str, value: int):
        super().__init__(name, description)
        self.effect = effect
        self.value = value

class Inventory:
    """Manages a character's items and equipment."""
    def __init__(self, max_size: int = 10):
        self.max_size = max_size
        self.items: list[Item] = []
        self.equipped_weapon: Weapon | None = None
        self.equipped_armor: Armor | None = None

    def add_item(self, item: Item) -> bool:
        """Add an item to the inventory."""
        if len(self.items) >= self.max_size:
            return False
        self.items.append(item)
        return True

    def remove_item(self, item: Item) -> bool:
        """Remove an item from the inventory."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def equip_weapon(self, weapon: Weapon) -> bool:
        """Equip a weapon."""
        if weapon in self.items:
            self.equipped_weapon = weapon
            return True
        return False

    def equip_armor(self, armor: Armor) -> bool:
        """Equip armor."""
        if armor in self.items:
            self.equipped_armor = armor
            return True
        return False

    def use_consumable(self, consumable: Consumable) -> bool:
        """Use a consumable item."""
        if consumable in self.items:
            # Apply the consumable's effect
            # This would be implemented in the game logic
            self.items.remove(consumable)
            return True
        return False
