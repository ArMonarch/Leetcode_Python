from unittest import TestCase


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        if len(operations) == 0:
            return 0

        x = 0
        for operation in operations:
            match operation:
                case "++X":
                    x += 1

                case "X++":
                    x += 1

                case "--X":
                    x -= 1

                case "X--":
                    x -= 1

                case _:
                    pass

        return x


class Tests(TestCase):
    def test_case_01(self) -> None:
        operations = ["--X","X++","X++"]
        expected = 1

        self.assertEqual(expected, Solution().finalValueAfterOperations(operations))

    def test_case_02(self) -> None:
        operations = ["++X","++X","X++"]
        expected = 3

        self.assertEqual(expected, Solution().finalValueAfterOperations(operations))

    def test_case_03(self) -> None:
        operations = ["X++","++X","--X","X--"]
        expected = 0

        self.assertEqual(expected, Solution().finalValueAfterOperations(operations))
