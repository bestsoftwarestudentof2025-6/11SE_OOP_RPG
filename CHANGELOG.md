# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2025-05-23]

### Added
- Forked from [Mr-Zamora/11SE_OOP_RPG](https://github.com/Mr-Zamora/11SE_OOP_RPG.git)
- Refactored single-file implementation into multi-file structure
- Added `constants.py` for centralized configuration management
- Implemented type hints throughout the codebase
- Added comprehensive docstrings to all classes and methods

### Changed
- Improved code style to follow PEP 8 guidelines
- Refactored string formatting for better readability
- Updated ROADMAP.md to reflect new project structure

### Fixed
- Fixed long lines to comply with PEP 8 (88 character limit)
- Eliminated magic numbers and hardcoded strings

## [2025-05-30] - Windsurf AI Implementation

### Added
- Implemented Windsurf AI for code improvements and maintenance
- Added automatic CHANGELOG updates
- Enhanced documentation with AI-generated insights

### Changed
- Updated README.md with AI implementation details
- Improved code organization following Windsurf recommendations
- Enhanced documentation consistency

## [2025-05-26] - Major Restructuring

### Milestone: Multi-File RPG Implementation
This update represents a significant milestone in the project's evolution, transforming the codebase from a single-file implementation to a well-organised, modular multi-file structure. This new structure better demonstrates professional software design while maintaining educational clarity.

### Added
- Created dedicated files for each major component:
  - `game.py` - Core game logic and flow management
  - `character.py` - Character and Boss class implementations
  - `weapon.py` - Weapon system implementation
  - `constants.py` - Game configuration and constants
  - `utils/logger.py` - Logging functionality
  - `utils/console.py` - Console interface utilities
- Implemented a clean entry point via `main.py`

### Changed
- Transformed from single-file to multi-file architecture while preserving OOP principles
- Simplified project structure by removing unnecessary package architecture
- Removed `__init__.py` files to make the project a standard Python project
- Modified import statements to work without package structure
- Renamed `PROJECT_RULES.md` to `RULES.md` for better consistency
- Updated documentation to emphasise educational focus
- Enhanced code organisation with logical separation of concerns

### Removed
- Deleted `setup.py` and package installation files
- Removed `run_game.py` in favour of using `rpg_game/main.py` directly
- Eliminated unnecessary complexity that could distract from learning objectives

### Commit Reference
- Commit [0ff49c9](https://github.com/Mr-Zamora/11SE_OOP_RPG/commit/0ff49c9) - "refactor: simplify project structure for educational use"
- Commit [884340c](https://github.com/Mr-Zamora/11SE_OOP_RPG/commit/884340c) - "chore: remove __pycache__ directories and add .gitignore"

### Maintenance
- Removed Python bytecode files (`__pycache__` directories) from version control
- Added comprehensive `.gitignore` file to prevent tracking of generated files
- Improved repository cleanliness and adherence to Python project standards

## [Unreleased]

### Planned
- Add unit tests with 80%+ coverage
- Implement error handling with specific exceptions
- Add inventory system for characters
- Expand character types (Sidekick, Villain classes)
- Enhance combat system
