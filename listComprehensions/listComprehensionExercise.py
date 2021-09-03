# --- 1 ---
def part1():
    just_a_string = 'this is a string'
    List = [c for c in just_a_string]
    print(f"part 1 ={List}")


def part2():
    # --- 2 - calculate time to do list comprehension ---
    import time

    # function of a simple for loop
    def for_loop(n):
        result = []
        for i in range(n):
            result.append(i**2)
        return result

    # function of list comprehension

    def list_comprehension(n):
        return [x**2 for x in range(n)]

    begin = time.time()
    for_loop(10**6)
    end = time.time()

    print('Time taken for loop', round(end-begin, 2))

    begin = time.time()
    list_comprehension(10**6)
    end = time.time()

    print('Time taken for list comprehension', round(end-begin, 2))


# part 3 - nested list comprehensions
def part3():
    nested_list = [[i for i in range(5)] for x in range(3)]
    print(f'part 3 - {nested_list}')


# part 4 - List comp and Lambda
def part4():
    # the list function will return a list
    # the map function takes 2 params. 1. the function, 2. the iterable (list, dict, tuples)
    # lambda is short for function. In this case, it can also be written as function(i): i*10
    numbers = list(map(lambda i: i*10, [i for i in range(1, 6)]))
    print(numbers)

# part 5 - conditional list comprehension


def part5():
    # Getting square of even numbers from 1 to 10
    squares = [n**2 for n in range(1, 11) if n % 2 == 0]

    # Display square of even numbers
    print(squares)

# Transpose
def part6():
    # Assign matrix
    twoDMatrix = [[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]]

    # Generate transpose
    trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix))]

    print(trans)

# Toggle case of each character in string
def part7():
    # Initializing string
    string = 'Geeks4Geeks'
    
    # Toggle case of each character
    List = list(map(lambda i: chr(ord(i)^32), string))
    
    # Display list
    print(List)

def part8():
    # Reverse each string in tuple
    # string[::-1] - slice notation (reverse)
    List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]
    
    # Display list
    print(List)

def part9():
    # Explicit function
    def digitSum(n):
        dsum = 0
        for ele in str(n):
            dsum += int(ele)
        return dsum
    
    
    # Initializing list
    List = [367, 111, 562, 945, 6726, 873]
    
    # Using the function on odd elements of the list
    # condition: compare i to 1 using the bitwise operator. Only works on integers
    newList = [digitSum(i) for i in List if i & 1]
    
    # Displaying new list
    print(newList)    

if __name__ == '__main__':
    # change the part to run
    part9()
