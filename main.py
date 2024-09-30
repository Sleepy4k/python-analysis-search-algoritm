try:
  import random
  from datetime import datetime
except ImportError as e:
  print(f"Import error: {e}")
  print("Please make sure you have installed the required libraries.")

def calculate_time(func):
  """ Make a decorator to calculate the time elapsed of a function
  Arguments:
    func: a function that will be calculated the time elapsed, can be any function as long as it has output
  Returns:
    function: The wrapper function that calculates the time elapsed of the function
  """
  def wrapper(*args, **kwargs):
    start = datetime.now()
    result = func(*args, **kwargs)
    end = datetime.now()
    elapsed = (end - start).total_seconds() * 1000
    print(f"Time elapsed: {elapsed} second(s)")
    return result

  return wrapper

def get_random_number(numbers):
  """ Get a random number from the provided list of numbers
  Arguments:
    numbers: a list of numbers
  Returns:
    int: Selected random number from the list
  """
  return numbers[random.randint(0, len(numbers) - 1)]

def generate_numbers(n):
  """ Generate a list of random numbers with the provided length (n)
  Arguments:
    n: length of the generated list of numbers
  Returns:
    list: A list of random numbers
  """
  return [random.randint(1, 1000) for _ in range(n)]

@calculate_time
def sequential_search(target, numbers):
  position = 0

  while position < len(numbers):
    if numbers[position] == target:
      break
    position += 1

  return position if position < len(numbers) else -1

@calculate_time
def binary_search(target, numbers):
  left = 0
  right = len(numbers) - 1

  numbers.sort() # Sort the list of numbers first

  while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
      return middle
    elif numbers[middle] < target:
      left = middle + 1
    else:
      right = middle - 1

  return -1

if __name__ == "__main__":
  try:
    length = int(input("Input length of number: "))
    numbers = generate_numbers(length)
    target = get_random_number(numbers)

    print(f"Sequential search found target on {sequential_search(target, numbers)} step(s)")
    print(f"Binary search found target on {binary_search(target, numbers)} step(s)")
  except ValueError:
    print("Input must be an integer, Please try again.")
    exit()
  except KeyboardInterrupt:
    print("Program is terminated.")
    exit()
  except Exception as e:
    print(f"An error occured: {e}")
    exit()
