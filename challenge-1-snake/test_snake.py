import pytest
from snake import Snake

@pytest.fixture
def snake_challenge():
    return Snake()

@pytest.fixture
def board_OK():
    board = [4, 5]
    return board

@pytest.fixture
def snake_OK():
    snake = [[5,5], [5,4], [4,4], [4,5]]
    return snake

@pytest.fixture
def depth_OK():
    return 4

def test_snake_case_OK(snake_challenge):
    board = [4, 3]
    snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
    depth = 3
    result = snake_challenge.number_of_available_different_paths(board, snake, depth)
    assert result == 7
    
    board = [2, 3]
    snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    depth = 10
    result = snake_challenge.number_of_available_different_paths(board, snake, depth)
    assert result == 1

    board = [10, 10]
    snake = [[5,5], [5,4], [4,4], [4,5]]
    depth = 4
    result = snake_challenge.number_of_available_different_paths(board, snake, depth)
    assert result == 81

def test_board_incorrect(snake_challenge, board_OK, snake_OK, depth_OK):
    with pytest.raises(ValueError):
        snake_challenge.number_of_available_different_paths([2], snake_OK, depth_OK)
    with pytest.raises(ValueError):
        snake_challenge.number_of_available_different_paths([2, 3, 4], snake_OK, depth_OK)
    with pytest.raises(ValueError):
        snake_challenge.number_of_available_different_paths([2, 11], snake_OK, depth_OK)

def test_snake_incorrect(snake_challenge, board_OK, snake_OK, depth_OK):
    snake_NOT_OK_1 = [[5,5], [5,-1], [4,4], [4,5]]
    snake_NOT_OK_2 = [[5,5], [5,6], [4,4], [4,5]]
    snake_NOT_OK_3 = [[5,5], [5,4]]
    snake_NOT_OK_4 = [[5,5], [5,4], [4,4], [4,5], [4,4], [4,5], [4,4], [4,5]]

    with pytest.raises(ValueError):
        snake_challenge.number_of_available_different_paths(board_OK, snake_NOT_OK_1, depth_OK)
    with pytest.raises(ValueError):
        snake_challenge.number_of_available_different_paths(board_OK, snake_NOT_OK_2, depth_OK)
    with pytest.raises(ValueError):
        snake_challenge.number_of_available_different_paths(board_OK, snake_NOT_OK_3, depth_OK)
    with pytest.raises(ValueError):
        snake_challenge.number_of_available_different_paths(board_OK, snake_NOT_OK_4, depth_OK)

def test_depth_incorrect(snake_challenge, board_OK, snake_OK, depth_OK):
    with pytest.raises(ValueError):
        snake_challenge.number_of_available_different_paths(board_OK, snake_OK, 0)
    with pytest.raises(ValueError):
        snake_challenge.number_of_available_different_paths(board_OK, snake_OK, 21)