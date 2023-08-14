# this file contains a simple algorithm that returns the number of steps it takes to reach 1


import numpy as np


def collatz(n: int) -> np.ndarray:
    """
    Collatz conjecture

    This function generates the Collatz sequence for a given number
    """

    # create an empty array to store the sequence
    sequence = np.array([])

    # while n is not 1
    while n != 1:
        # append n to the sequence
        sequence = np.append(sequence, n)

        # if n is even
        if n % 2 == 0:
            # divide n by 2
            n = n // 2
        # if n is odd
        else:
            # multiply n by 3 and add 1
            n = 3 * n + 1

    # append 1 to the sequence
    sequence = np.append(sequence, n)

    # return the sequence
    return sequence


def plot_collatz(n: np.ndarray) -> None:
    """
    Plot the Collatz sequence for a given number
    """
    import matplotlib.pyplot as plt
    
    plt.plot(sequence)  # get the sequence
    plt.title("Collatz Conjecture")  # set the title
    plt.show()  # show the plot


if __name__ == "__main__":
    # sequence = collatz(int(input("Enter a number: ")))  # get the sequence
    sequence = collatz(27)  # get the sequence

    print(f"{sequence}\nNumber of steps: {len(sequence) - 1}")  # print the number of steps

    plot_collatz(sequence)

#? Output -------------------------------------------------------------------------------------
