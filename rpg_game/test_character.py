import unittest
import io
import sys
from rpg_game.character import Character, Boss, Sidekick, Villain, LEVEL_UP_EXP
from rpg_game.inventory import Item, Weapon, Armor, Consumable, Inventory
from rpg_game.utils.logger import GameLogger

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character(
            "Test Character",
            health=100,
            damage=10,
            weapon_name="Test Sword",
            weapon_damage=5,
            level=1,
            experience=0
        )
        self.boss = Boss(
            "Test Boss",
            health=150,
            damage=20,
            weapon_name="Boss Sword",
            weapon_damage=10,
            special_ability="Fireball"
        )
        self.sidekick = Sidekick(
            "Test Sidekick",
            health=80,
            damage=5,
            weapon_name="Sidekick Sword",
            weapon_damage=3,
            support_ability="Heal"
        )
        self.villain = Villain(
            "Test Villain",
            health=120,
            damage=15,
            weapon_name="Villain Sword",
            weapon_damage=8,
            evil_deed="Steal",
            level=1,
            experience=0
        )

    def test_character_creation(self):
        self.assertEqual(self.character.name, "Test Character")
        self.assertEqual(self.character.get_health(), 100)
        self.assertEqual(self.character.damage, 10)
        self.assertIsNotNone(self.character.weapon)

    def test_experience_system(self):
        # Test initial state
        self.assertEqual(self.character.experience, 0)
        self.assertEqual(self.character.level, 1)
        
        # Test experience gain without level up
        self.character.gain_experience(50)
        self.assertEqual(self.character.experience, 50)
        self.assertEqual(self.character.level, 1)
        
        # Test experience gain with level up
        self.character.gain_experience(50)  # Should level up
        self.assertEqual(self.character.experience, 0)  # Experience resets after level up
        self.assertEqual(self.character.level, 2)
        
        # Test multiple level ups
        initial_health = self.character.get_health()
        initial_damage = self.character.damage
        
        self.character.gain_experience(200)  # Should level up twice
        self.assertEqual(self.character.level, 4)
        
        # Check stats increased with each level
        self.assertGreater(self.character.get_health(), initial_health)
        self.assertGreater(self.character.damage, initial_damage)
        
        # Test experience gain with partial level up
        self.character.gain_experience(150)  # Should level up once
        self.assertEqual(self.character.level, 5)
        self.assertEqual(self.character.experience, 50)  # 150 - 100 = 50
        
        # Test experience gain with multiple partial level ups
        self.character.gain_experience(175)  # Should level up once
        self.assertEqual(self.character.level, 7)
        self.assertEqual(self.character.experience, 25)  # 175 - 150 = 25
        
        # Test experience gain with very large amount
        initial_level = self.character.level
        initial_exp = self.character.experience
        self.character.gain_experience(1000)  # Should level up multiple times
        self.assertGreater(self.character.level, initial_level)
        self.assertLess(self.character.experience, LEVEL_UP_EXP)
        
        # Test experience gain with negative amount (should be ignored)
        self.character.gain_experience(-50)
        self.assertEqual(self.character.experience, initial_exp)  # Should remain unchanged
        
        # Test logging functionality
        logger = GameLogger()
        
        # Capture stdout for logging
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Gain experience with logging
        self.character.gain_experience(LEVEL_UP_EXP, logger)
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Check logs
        logs = captured_output.getvalue()
        self.assertIn("Test Character leveled up to level", logs)
        
    def test_logging(self):
        """Test the logging functionality during combat and level up."""
        logger = GameLogger()
        
        # Test combat logging
        enemy = Character("Enemy", 100, 10)
        
        # Capture the output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Test combat logging
        self.character.attack(enemy, logger)
        
        # Test level up logging
        self.character.gain_experience(LEVEL_UP_EXP, logger)
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Check logs
        logs = captured_output.getvalue()
        self.assertIn(self.character.name, logs)
        self.assertIn(enemy.name, logs)
        self.assertIn("Test Character leveled up to level", logs)
        self.assertIn("New stats:", logs)

    def test_inventory(self):
        # Test adding items
        sword = Weapon("Sword", "A sharp sword", 10)
        armor = Armor("Armor", "Heavy armor", 5)
        potion = Consumable("Healing Potion", "Restores health", "heal", 20)

        self.assertTrue(self.character.inventory.add_item(sword))
        self.assertTrue(self.character.inventory.add_item(armor))
        self.assertTrue(self.character.inventory.add_item(potion))

        # Test equipping items
        self.assertTrue(self.character.inventory.equip_weapon(sword))
        self.assertTrue(self.character.inventory.equip_armor(armor))
        self.assertTrue(self.character.inventory.use_consumable(potion))

    def test_boss_special_ability(self):
        special_ability = "Fireball"
        self.boss = Boss("Test Boss", 150, 20, special_ability)
        self.assertEqual(self.boss.use_special_ability(), f"Test Boss uses {special_ability}!")

    def test_character_level_up(self):
        # Test gaining experience without leveling up
        self.character.gain_experience(50)
        self.assertEqual(self.character.experience, 50)
        self.assertEqual(self.character.level, 1)
        
        # Test leveling up
        self.character.gain_experience(50)
        self.assertEqual(self.character.experience, 0)
        self.assertEqual(self.character.level, 2)
        self.assertGreater(self.character.get_health(), 100)
        self.assertGreater(self.character.damage, 10)

    def test_character_attack_with_experience(self):
        # Create a test enemy with higher health than damage
        enemy = Character(
            "Test Enemy",
            health=150,
            damage=10,
            level=1,
            experience=0
        )
        
        # Verify initial state
        self.assertEqual(self.character.experience, 0)
        self.assertEqual(self.character.level, 1)
        
        # Verify initial damage calculation
        damage = self.character.damage + (self.character.weapon.damage if self.character.weapon else 0)
        self.assertEqual(damage, 15)  # Base damage 10 + weapon damage 5
        
        # Attack the enemy multiple times
        enemy_health = enemy.get_health()
        for i in range(10):
            damage, enemy_defeated = self.character.attack(enemy)
            if i < 9:  # First 9 attacks should not defeat the enemy
                self.assertFalse(enemy_defeated)
                # Verify damage is being applied correctly
                self.assertEqual(enemy.get_health(), enemy_health - (i + 1) * 15)
            else:  # Last attack should defeat the enemy
                self.assertTrue(enemy_defeated)
                self.assertEqual(enemy.get_health(), 0)  # Enemy should be dead
                
                # Verify experience gain after defeating enemy
                self.assertEqual(self.character.experience, LEVEL_UP_EXP)  # Should gain exactly LEVEL_UP_EXP amount
                self.assertEqual(self.character.level, 1)  # Should not level up yet
                
                # Verify experience is tracked correctly
                self.assertGreater(self.character.experience, 0)
                self.assertLessEqual(self.character.experience, LEVEL_UP_EXP)
                
                # Verify experience gain is logged
                # Capture stdout
                captured_output = io.StringIO()
                sys.stdout = captured_output
                sys.stdout.flush()
                
                # Attack again to get logs
                self.character.attack(enemy, GameLogger())
                sys.stdout = sys.__stdout__
                
                # Get and verify logs
                logs = captured_output.getvalue()
                self.assertIn("Test Character gained 100 experience points", logs)
                self.assertIn("Total experience: 100", logs)
                
                # Verify stats after level up
                initial_health = self.character.get_health()
                initial_damage = self.character.damage
                
                # Create a new enemy for the next test
                new_enemy = Character("Test Enemy 2", 150, 10)
                
                # Attack new enemy with logging to gain experience
                self.character.attack(new_enemy, logger)
                
                # Verify experience gain after defeating new enemy
                self.assertEqual(self.character.experience, LEVEL_UP_EXP)  # Should still have LEVEL_UP_EXP since we level up
                
                # Check logs
                self.assertIn("Test Character leveled up to level", logs)
                self.assertIn("New stats:", logs)
                
                # Verify stats after level up
                self.assertEqual(self.character.level, 2)
                self.assertGreater(self.character.get_health(), initial_health)
                self.assertGreater(self.character.damage, initial_damage)
        
        # Verify stats before level up
        initial_health = self.character.get_health()
        initial_damage = self.character.damage
        
        # Test experience gain with logger
        logger = GameLogger()
        
        # Create a new enemy for the next test
        new_enemy = Character("Test Enemy 2", 150, 10)
        
        # Verify experience before attack
        self.assertEqual(self.character.experience, LEVEL_UP_EXP)
        
        # Capture stdout for logging
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sys.stdout.flush()  # Ensure all output is captured
        
        # Attack new enemy with logging to gain experience
        self.character.attack(new_enemy, logger)
        
        # Verify experience gain after defeating new enemy
        self.assertEqual(self.character.experience, LEVEL_UP_EXP)  # Should still have LEVEL_UP_EXP since we level up
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Check logs
        logs = captured_output.getvalue()
        self.assertIn("Test Character gained 100 experience points", logs)
        self.assertIn("Test Character leveled up to level", logs)
        self.assertIn("New stats:", logs)
        
        # Verify stats after level up
        self.assertEqual(self.character.level, 2)
        self.assertGreater(self.character.get_health(), initial_health)
        self.assertGreater(self.character.damage, initial_damage)

    def test_sidekick_support_ability(self):
        self.assertEqual(self.sidekick.use_support_ability(), "Test Sidekick uses Heal!")

    def test_villain_evil_deed(self):
        self.assertEqual(self.villain.commit_evil_deed(), "Test Villain commits Steal!")

if __name__ == '__main__':
    unittest.main()
