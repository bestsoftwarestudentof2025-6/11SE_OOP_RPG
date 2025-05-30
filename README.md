# RPG Lesson: Object-Oriented Programming 

## Educational Purpose

This project is designed as an educational tool to demonstrate Object-Oriented Programming (OOP) concepts in Python. The code is intentionally structured to be clear, readable, and easy to understand for students learning OOP principles.

### Enhanced with Windsurf AI
The project now utilizes Windsurf AI for continuous improvement and maintenance, ensuring the codebase remains up-to-date with best practices while maintaining its educational focus.

## Running the Game

To run the game, simply execute:

```
python rpg_game/main.py
```

No installation or setup is required - just clone the repository and run the main file.

## Project Structure

This project uses a simple, modular structure to demonstrate OOP concepts:

### Main Files
- `rpg_game/main.py` - Entry point to run the game
- `rpg_game/game.py` - Game class and main game logic
- `rpg_game/character.py` - Character and Boss classes
- `rpg_game/weapon.py` - Weapon class implementation
- `rpg_game/constants.py` - Game constants and configuration

### Utility Files
- `rpg_game/utils/console.py` - Console UI utilities
- `rpg_game/utils/logger.py` - Game logging functionality

### Documentation
- `README.md` - Project documentation
- `ROADMAP.md` - Development plans
- `CHANGELOG.md` - Version history and changes
- `RULES.md` - Project rules and guidelines
- `UML_class_diagram.md` - Class structure and relationships

## COIPEA: Core OOP Concepts Demonstrated

This code demonstrates all six fundamental Object-Oriented Programming principles (COIPEA):
- **C**lasses and **O**bjects
- **I**nheritance
- **P**olymorphism
- **E**ncapsulation
- **A**bstraction

### 1. Classes and Objects
- The code defines several classes (`GameLogger`, `Weapon`, `Character`, `Boss`, `Game`) that encapsulate data and behavior
- Objects are instantiated from these classes (e.g., player character, bosses, weapons)

### 2. Inheritance
- `Boss` inherits from `Character`, demonstrating class hierarchy
- The `super().__init__()` call in `Boss.__init__` shows proper parent constructor invocation
- Method overriding is shown in `Boss.attack()` which extends the parent's method

### 3. Polymorphism
- Method overriding in `Boss.attack()` demonstrates polymorphism - same method name but different behavior than parent class
- The `attack()` method behaves differently depending on the actual object type (Character vs Boss)
- This allows for treating different object types through a common interface

### 4. Encapsulation
- Each class encapsulates its own data (attributes) and behavior (methods)
- Classes have clear responsibilities and manage their own state
- Objects maintain their internal state and expose functionality through methods
- The `Character` class demonstrates proper encapsulation with:
  - A private `_health` attribute (indicated by the underscore prefix)
  - Public `get_health()` and `set_health()` methods for controlled access
  - Data validation in the setter to ensure health is never negative
  - Consistent use of getters/setters throughout the codebase (e.g., in combat logic)
  - The `Weapon` class is composed within the `Character` class, demonstrating strong composition

### 5. Abstraction
- Classes represent abstract concepts (Character, Weapon, Game) hiding implementation details
- The Game class abstracts away the complexity of game flow management
- Users of the classes only need to understand the interface, not internal workings

### 6. Additional Relationships
- **Composition**: Strong composition between `Character` and `Weapon` (a character "has-a" weapon)
- **Dependency**: `GameLogger` demonstrates a dependency relationship (explicitly mentioned as "dotted line in UML")

## UML Class Diagram Concepts

The code demonstrates several UML class diagram concepts including classes, relationships (inheritance, composition, dependency), and various class members.

For a detailed analysis of UML concepts in this code, see [UML_class_diagram.md](UML_class_diagram.md).

## Design Patterns and Principles

### 1. Single Responsibility Principle
- Each class has a clear, focused purpose
- Utility functions are separated into logical groups (e.g., `clear_screen`, `press_enter` in console utilities)
- The `GameLogger` class handles all logging functionality
- The `Weapon` class focuses solely on weapon properties and behavior

### 2. Game Loop Pattern
- The `Game.run()` method implements a simple game loop

### 3. Factory Method (simplified)
- `choose_weapon()` acts as a factory for creating weapon configurations

## OOP Learning Value

### 1. Clear Demonstration of OOP Concepts
- **Inheritance**: The `Boss` class extends `Character` and overrides the `attack` method
- **Encapsulation**: Private attributes with getters/setters in `Character` class
- **Composition**: `Character` contains a `Weapon` object
- **Dependency**: `Game` depends on `GameLogger` for logging
- **Polymorphism**: Different attack behaviours between `Character` and `Boss`

### 2. Progressive Learning Path
1. Start with basic utility functions
2. Introduce simple classes (`Weapon`)
3. Build more complex classes with relationships (`Character`, `Boss`)
4. Show how classes interact in the `Game` class

### 3. Code Organization
- Clear separation of concerns
- Logical grouping of related functionality
- Consistent naming conventions
- Proper use of Python's module system


### Areas That Could Be Challenging 

1. **Multiple Classes at Once**
   - The code introduces several classes simultaneously, which might be overwhelming
   - A more step-by-step approach might build one class at a time

2. **Some Advanced Concepts**
   - Static methods (`@staticmethod`) might need additional explanation
   - The distinction between composition and dependency might be subtle for beginners

3. **Limited Visibility Examples**
   - Doesn't demonstrate private/protected attributes with Python's underscore convention
   - Missing encapsulation examples with getters/setters

## Learning Recommendations

### Suggested Learning Approach
1. **Start with the Big Picture**
   - Play the game in action
   - Discuss with a peer the overall architecture and class relationships

2. **Progressive Implementation**
   - Begin with the `Weapon` class (simplest)
   - Move to `Character` class and introduce encapsulation
   - Show inheritance with the `Boss` class
   - Finally, demonstrate the `Game` class that ties everything together

3. **Hands-On**
   - Extend the `Character` class with new abilities
   - Implement a new weapon type with special effects
   - Add a new game mechanic using the existing class structure

4. **Code Review**
   - Walk through the code together with a peer, discussing design decisions
   - Highlight good practices and potential improvements
   - Connect the implementation to the corresponding UML diagram

## Future Enhancements

See [ROADMAP.md](ROADMAP.md) for planned improvements.
