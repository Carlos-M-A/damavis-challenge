import pytest
from snake import Snake

def test_snake_case_OK():
    snake_challenge = Snake()
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