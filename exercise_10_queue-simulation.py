from collections import deque

def run_queue(operations):
    """Apply enqueue/dequeue operations and return the remaining queue."""
    queue = deque()
    result = []
    for operation in operations:
        if isinstance(operation, (tuple, list)):
            name = operation[0]
            if name == 'enqueue':
                queue.append(operation[1])
            elif name == 'dequeue':
                result.append(queue.popleft() if queue else None)
        elif operation == 'dequeue':
            result.append(queue.popleft() if queue else None)
    return list(queue), result
