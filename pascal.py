def pascal_line(n):
    # Base case
    if n == 0:
        return [[1]]
    else:
        # Our current row, it will always start with one.
        current = []
        current.append(1)
        # Recursive step
        answer = pascal_line(n-1)
        # Previous row is one above our current one.
        prev = answer[-1]
        # The amount of elements that is not one for
        # current row is always one less than total amount
        # of all elements for previous row. 
        for i in range(len(prev)-1):
            # An element on pascals triangle is computed by
            # the sum of the 2 elements over it.
            current.append(prev[i] + prev[i+1])
        # Row always ends with 1.
        current.append(1)
        answer.append(current)
    return answer


def pascal_rec(n):
    return pascal_line(n)


print(pascal_rec(2))