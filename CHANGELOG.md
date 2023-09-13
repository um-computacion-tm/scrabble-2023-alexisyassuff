# Changelog

## [28-08-2023]

### Added

- Created a method and test to verify that the player has the tiles to complete the desired word.

## [29-08-2023]

### Added

- Created tests and functions responsible for verifying player's tiles and performing deductions when successful.
- Descriptive message of changes.

## [30-08-2023]

### Added

- Added Codeclimate and CircleCI.

## [09-09-2023]

### Added

- Added tests and methods for multipliers.
- Added Scrabble-related tests to control player turns.

## [10-09-2023] 

### Added

- Added tests related to the Board class.

## [11-09-2023] Morning 

### Added

- Added file CHANGELOG.md

## [11-09-2023] Afternoon

### Added
- Implemented a new function that manages the next turn in the game.
- Added unit tests to verify the correct functionality of the 'next_turn' method.
  - `test_next_turn_when_player_is_not_the_first`: Ensures that after player 0, it's player 1's turn.
  - `test_next_turn_when_player_is_last`: In a scenario with 3 players, confirms that after player 3, it's player 1's turn.

## [12-09-2023]

### Added

- Implemented the `validate_word_inside_board` method in the `Board` class to check if a word can fit on the game board. This method verifies the word's location and orientation to ensure it fits within the board boundaries.
  
## [13-09-2023]

### Added

- Added a new method validate_word_out_of_board to validate if a word goes out of bounds on the game board, enhancing testing capabilities.

