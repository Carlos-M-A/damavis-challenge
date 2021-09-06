class Snake:

    def number_of_available_different_paths(self, board: list, snake:list, depth:int) -> int:
        self._check_inputs(board, snake, depth)
        
        self._board = board
        self._directions = 'LRUD'
        return self._count_available_different_paths(snake, depth) % 1_000_000_007
    
    def _count_available_different_paths(self, snake:list, depth:int) -> int:
        if depth == 0:
            return 1
        else:
            paths_quantity = 0
            for direction in self._directions:
                if self._is_move_correct(snake, direction):
                    new_snake = self._new_snake(snake, direction)
                    paths_quantity += self._count_available_different_paths(new_snake, depth - 1)
            return paths_quantity
    
    def _is_move_correct(self, snake:list, direction:str) -> bool:
        head = snake[0]
        new_head = self._new_head_of_snake(head, direction)
        return self._is_new_head_in_a_correct_position(snake, new_head)

    def _is_new_head_in_a_correct_position(self, snake:list, new_head:list) -> bool:
        if new_head[0] < self._board[0] and new_head[1] < self._board[1]:
            if new_head[0] >= 0 and new_head[1] >= 0:
                if new_head not in snake[:-1]:
                    return True
                else:
                    return False
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
        return new_head

    def _check_inputs(self, board:list, snake:list, depth:int):
        if len(board) != 2:
            raise ValueError('board length must be 2')
        if board[0] < 1 or board[0] > 10 or board[1] < 1 or board[1] > 10:
            raise ValueError("board's columns or rows must be between 1 and 10")
        if len(snake) < 3 or len(snake) > 7:
            raise ValueError('snake length must be between 3 and 7')
        for part in snake:
            self._check_snake_part(board, part)
        self._check_snake_structure(snake)
        if depth < 1 or depth > 20:
            raise ValueError('depth must be between 1 and 20')

    def _check_snake_part(self, board:list, part:list):
        if len(part) != 2:
            raise ValueError('Every part of snake must be a list with lenght=2')
        if part[0] < 0 or part[0] > board[0] or part[1] < 0 or part[1] > board[1]:
            raise ValueError('Every part of snake must be inside the board')
    
    def _check_snake_structure(self, snake):
        for i, part in enumerate(snake[1:]):
            check_sum = abs(snake[i][0] - part[0]) + abs(snake[i][1] - part[1])
            if check_sum != 1:
                raise ValueError("snake's structure is NOT correct")