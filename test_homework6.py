import homework6 as hw


class TestNumberSpiralDiagonals:
    def test_number_spiral_diagonals_case_1(self):
        case = hw.number_spiral_diagonals(1)
        solution = 1
        assert type(case) == type(solution)
        assert case == solution

    def test_number_spiral_diagonals_case_2(self):
        case = hw.number_spiral_diagonals(3)
        solution = 25
        assert type(case) == type(solution)
        assert case == solution

    def test_number_spiral_diagonals_case_3(self):
        case = hw.number_spiral_diagonals(5)
        solution = 101
        assert type(case) == type(solution)
        assert case == solution

    def test_number_spiral_diagonals_case_4(self):
        case = hw.number_spiral_diagonals(1001)
        solution = 669171001
        assert type(case) == type(solution)
        assert case == solution

    def test_number_spiral_diagonals_type_error(self):
        assert hw.number_spiral_diagonals("111") == False
