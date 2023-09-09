from game.cell import Cell
class WordCalculator:
    def calculate_word_value(word):
        total_value = 0
        word_multiplier = 1

        for cell in word:
            letter_value = cell.letter.value

            if cell.multiplier_type == 'letter':
                letter_value *= cell.multiplier

            total_value += letter_value

            if cell.multiplier_type == 'word':
                word_multiplier *= cell.multiplier

        return total_value * word_multiplier