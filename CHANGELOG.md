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

## [21-09-2023]

### Added
- Added board-related unit tests to ensure proper game functionality.
  - `test_board_is_empty` verifies that the board is empty as expected.
  - `test_board_is_not_empty` checks that the board is not empty after adding letters.
  - `test_place_word_empty_board_horizontal_fine` ensures the ability to place words on an empty board in the horizontal orientation.
  - `test_place_word_empty_board_horizontal_wrong` verifies that it's not possible to place words on an empty board with incorrect placement in the horizontal orientation.
  - `test_place_word_empty_board_vertical_fine` confirms the capability to place words on an empty board in the vertical orientation.
  - `test_place_word_empty_board_vertical_wrong` checks that it's not possible to place words on an empty board with incorrect placement in the vertical orientation.
  - `test_place_word_not_empty_board_horizontal_fine` ensures the ability to place words on a non-empty board in the horizontal orientation.

## [23-09-2023]

### Added
- Added basic Scrabble game functionality in the main.py file. Players can now enter the number of participants and start the game. A loop has been implemented to allow each player to take their turn and play their words.

## [24-09-2023]

### Added
Added to the method that performs the unit test corresponding to verifying if board is empty

## [26-09-2023]

### Added
Added a function, validate_word_place_board, to the Board class to check the board's ability to receive a word at a specific location and orientation. This feature ensures that in the horizontal orientation the words fit correctly on the board based on their length.

## [27-09-2023] 00hs
### Added
- Added to the validate_palabra_place_board function, the verification of the capacity of the board to ensure that in both horizontal and vertical orientation the words fit correctly on the board according to their length.
- Updated readme.md adding file name and file number.

## [27-09-2023] 10hs

### Added
- Added a method that checks the next turn when the game starts. This is done by defining the following shift variable within the __init__ constructor.

## [04-10-2023]

### Added
- Added tests that will verify that the word is available in the dictionary of the Royal Spanish Academy

## [05-10-2023] 13hs

### Added
- Added respective methods to the test_diccionary.py file that will verify the existence of the word in the RAE

## [06-10-2023] 13hs

### Added
- The validate_word function was added to the scrabble.py file where it is verified that the user has in his hand the pieces corresponding to the word he wants to enter, also that the word fits on the board and also that it exists in the dictionary.


Name: Alexis Yassuff
Id: 62072