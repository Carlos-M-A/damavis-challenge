from _typeshed import SupportsLenAndGetItem


class Snake:

    def number_of_available_different_paths(self, board: list, snake:list, depth:int) -> int:
        self._board = board
        self._directions = 'LRUD'
        return self._count_available_different_paths(snake, depth)
    
    def _count_available_different_paths(self, snake:list, depth:int) -> int:
        if depth == 0:
            return 1
        else:
            for direction in self._directions:
                if self._is_move_correct(snake, direction):
                    new_snake = self._new_snake(snake, direction)
                    return self._count_available_different_paths(new_snake, depth - 1)
    
    def _is_move_correct(self, snake:list, direction:str) -> bool:
        head = snake[0]
        new_head = self._new_head_of_snake(head, direction)
        return self._is_new_head_in_a_correct_position(snake, new_head)

    def _is_new_head_in_a_correct_position(self, snake:list, new_head:list) -> bool:
        if new_head[0] < self._board[0] and new_head[1] < self._board[1]:
            if new_head not in snake[:-1]:
                return True
            else:
                return False
        else:
            return False

    def _new_snake(self, snake: list, direction: str) -> list:
        new_snake = list()
        new_snake.append(self._new_head_of_snake(snake[0], direction))
        for part in snake[:-1]:
            new_snake.append(part.copy())
        return new_snake


    def _new_head_of_snake(self, head:list, direction:str) -> list:
        new_head = head.copy()
        if direction == 'L':
            new_head[1] -= 1
        elif direction == 'R':
            new_head[1] += 1
        elif direction == 'U':
            new_head[0] -= 1
        elif direction == 'D':
            new_head[0] += 1
    