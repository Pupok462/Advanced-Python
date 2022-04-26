from pytest import mark, fixture, param, raises
from vector import (
    SumException,
    MulException,
    Point,
    Vector
)


@fixture
def point_inst_1(request) -> Point:
    x, y, z = request.param
    point_1 = Point(x, y, z)
    return point_1


@fixture
def point_inst_2(request) -> Point:
    x, y, z = request.param
    point_2 = Point(x, y, z)
    return point_2


@fixture
def vector_inst(point_inst_1, point_inst_2) -> Vector:
    res = Vector(point_inst_1, point_inst_2)
    return res


class TestVector:
    @mark.parametrize(
        "vector_1, vector_2, res_vector",
        [
            param(Vector(Point(0, 0, 0), Point(1, 2, 3)), Vector(Point(0, 0, 0), Point(4, 5, 6)),
                  Vector(Point(0, 0, 0), Point(5, 7, 9)), id="123 + 456 = 579"),
            param(Vector(Point(1, 1, 1), Point(1, 1, 1)), Vector(Point(1, 1, 1), Point(5, 5, 5)),
                  Vector(Point(1, 1, 1), Point(6, 6, 6)), id="111 + 555 = 666"),
            param(Vector(Point(-1, -1, -1), Point(4, 0, 4)), Vector(Point(-1, -1, -1), Point(100, 3, 2)),
                  Vector(Point(-1, -1, -1), Point(104, 3, 6)), id="404 + 10032 = 10436")
        ]
    )
    def test_add(self, vector_1, vector_2, res_vector):
        assert vars(res_vector) == vars(vector_2 + vector_1)

    @mark.parametrize(
        "vector_1, vector_2, res_vector",
        [
            param(Vector(Point(0, 0, 0), Point(1, 2, 3)), Vector(Point(0, 0, 0), Point(4, 5, 6)),
                  Vector(Point(0, 0, 0), Point(-3, 6, -3)), id="123 * 456 = -36-3"),
            param(Vector(Point(0, 0, 0), Point(3, 3, 3)), Vector(Point(0, 0, 0), Point(-3, -3, -3)),
                  Vector(Point(0, 0, 0), Point(0, 0, 0)), id="333 * -3-3-3 = 000"),
            param(Vector(Point(0, 0, 0), Point(1, 2, 0)), Vector(Point(0, 0, 0), Point(4, 5, 0)),
                  Vector(Point(0, 0, 0), Point(0, 0, -3)), id="333 * -3-3-3 = 00-3"),

        ]
    )
    def test_mul(self, vector_1, vector_2, res_vector):
        assert vars(vector_1 * vector_2) == vars(res_vector)

    @mark.parametrize(
        "vector, expected_result",
        [
            param(Vector(Point(0, 0, 0), Point(3, 4, 0)), 5, id="(3,4 -> 5)"),
            param(Vector(Point(0, 0, 0), Point(5, 12, 0)), 13, id="(5,12 -> 13)"),
            param(Vector(Point(0, 0, 0), Point(8, 15, 0)), 17, id='(8, 15) -> 17'),
        ],
    )
    def test_length(self, vector, expected_result):
        res = vector.length()
        assert res == expected_result

    # Тест через фикстуры ( бесполезный но вдруг )
    # @mark.parametrize(
    #     "point_inst_1, point_inst_2, start, end",
    #     [
    #         param((1, 1, 1), (3, 4, 5), (0, 0, 0), (2, 3, 4), id='-1 -1 -1'),
    #         param((1, 2, 3), (7, 8, 9), (0, 0, 0), (6, 6, 6), id='-1 -2 -3'),
    #         param((5, 5, 5), (1, 2, 3), (0, 0, 0), (-4, -3, -2), id='-5 -5 -5'),
    #     ],
    #     indirect=['point_inst_1', 'point_inst_2']
    # )
    # def test_parallel_transfer(self, vector_inst, start, end):
    #     vector_inst.parallel_transfer()
    #     expected_res = vector_inst(start, end)
    #     assert vector_inst == expected_res

    @mark.parametrize(
        "vector, expected_vector",
        [
            [Vector(Point(1, 2, 3), Point(7, 8, 9)), Vector(Point(0, 0, 0), Point(6, 6, 6))],
            [Vector(Point(1, 1, 1), Point(3, 4, 5)), Vector(Point(0, 0, 0), Point(2, 3, 4))],
            param(Vector(Point(5, 5, 5), Point(1, 2, 3)), Vector(Point(0, 0, 0), Point(-4, -3, -2)))
        ],
    )
    def test_parallel_transfer(self, vector, expected_vector):
        vector.parallel_transfer()
        assert vars(vector) == vars(expected_vector)

    @mark.parametrize(
        "vector_1, vector_2",
        [
            param(Vector(Point(1, 1, 0), Point(1, 2, 3)), Vector(Point(0, 0, 0), Point(4, 5, 6))),
        ]
    )
    def test_add_raise(self, vector_1, vector_2):
        with raises(SumException) as exc_info:
            vector_1 + vector_2
        assert str(exc_info.value) == Vector.EXC_INFO_SUM

    @mark.parametrize(
        "vector_1, vector_2",
        [
            param(Vector(Point(1, 1, 0), Point(1, 2, 3)), Vector(Point(0, 0, 0), Point(4, 5, 6))),
        ]
    )
    def test_mul_raise(self, vector_1, vector_2):
        with raises(MulException) as exc_info:
            vector_1 * vector_2
        assert str(exc_info.value) == Vector.EXC_INFO_MUL
