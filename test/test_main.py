# import random
# class TestCLI(unittest.TestCase):

#     @patch('builtins.input', return_value='3')
#     def test_get_player_count(self, input_patched):
#         self.assertEqual(
#             get_player_count(),
#             3,
#         )

#     @patch('builtins.print')
#     @patch('builtins.input', side_effect=['A', '3'])
#     def test_get_player_count_wrong_input(self, input_patched, print_patched):
#         self.assertEqual(
#             get_player_count(),
#             3,
#         )

#     @patch('builtins.print')
#     @patch('builtins.input', side_effect=['10', '1'])
#     def test_get_player_count_control_max(self, input_patched, print_patched):
#         self.assertEqual(
#             get_player_count(),
#             1,
#         )
        
# if __name__ == '__main__':
#     unittest.main()