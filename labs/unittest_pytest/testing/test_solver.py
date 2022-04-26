from unittest import TestCase
from solver import Solver
from pytest import fixture, mark, param, raises

########################################
# Unittest
########################################


class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.solver = Solver(2, 3)

    def test_add(self):
        res = self.solver.add()
        self.assertEqual(5, res)

    def test_mul(self):
        res = self.solver.mul()
        self.assertEqual(6, res)


########################################
# Pytest
########################################

@fixture
def solver_inst():
    solver = Solver(4, 5)
    return solver


@fixture
def solver_inst2(request) -> Solver:
    a, b = request.param
    solver = Solver(a, b)
    return solver


class TestSolver:
    def test_add(self, solver_inst):
        res = solver_inst.add()
        assert res == 9

    # Здесь делаем параметризацию и флаг indirect указывает на какие параметры надо перенести ,
    # если indirect=True то мы будем передавать все параметры
    @mark.parametrize(
        "solver_inst2, expected_result",
        [
            [(3, 4), 12],
            param((5, 6), 30, id="five_on_six"),
            param((5, 0), 0, id="zero"),
        ],
        indirect=["solver_inst2"],
    )
    def test_mul(self, solver_inst2, expected_result):
        res = solver_inst2.mul()
        assert res == expected_result

    @mark.parametrize(
        "solver_inst2",
        [
            param(("a", "b"), id="check_raises_by_str"),
        ],
        indirect=True,
    )
    def test_mul_raises(self, solver_inst2: Solver):
        s = solver_inst2

        with raises(TypeError) as exc_info:
            s.mul()
        assert str(exc_info.value) == s.EXC_TYPE_ERROR_TEXT


# Здесь тест делается атомарным потому что если мы просто
# подряд сделаем тесты, то assert сработает только один а не все
