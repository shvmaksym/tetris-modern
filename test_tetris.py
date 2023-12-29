import pytest
from blocks import *
from run_game import Run  


@pytest.fixture
def game():
    return Run()


def test_reset(game):
    game.score = 100
    game.level = 5
    game.reset()
    assert game.score == 0
    assert game.level == 1


def test_change_speed(game):
    game.score = 90
    initial_speed = game.speed
    game.change_speed()
    assert game.speed == initial_speed

    game.score = 100
    game.change_speed()
    assert game.speed < initial_speed
    assert game.level == 2


def test_change_score(game):
    initial_score = game.score
    game.change_score(5, 0)
    assert game.score == initial_score + 5

    game.change_score(0, 1)
    assert game.score == initial_score + 5 + 100


def test_get_random_block(game):
    block1 = game.get_random_block()
    block2 = game.get_random_block()
    assert block1 is not block2


def test_move_left(game):
    initial_position = game.current.get_positions()[0]
    game.move_left()
    assert game.current.get_positions()[0].column < initial_position.column

