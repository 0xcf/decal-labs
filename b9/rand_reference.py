import argparse
import random

MAX_ITERATIONS = 100
MAX_SIDES = 20

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        dest="object",
        choices=["coin", "dice"],
        help="Use 'coin' to flip a coin or 'dice' to roll a die"
    )

    parser.add_argument(
        "-i", "--iterations",
        dest="iterations",
        type=int,
        default=1,
        help="Number of times to flip a coin or roll dice (max=100)"
    )

    # COMMIT 1: Add -s flag for number of sides on a die
    parser.add_argument(
        "-s", "--sides",
        dest="sides",
        type=int,
        default=6,
        help="Number of sides on a die (max=20; ignored when flipping a coin)"
    )

    args = parser.parse_args()

    if args.object == "coin":
        flip_coin(args.iterations)
    elif args.object == "dice":
        roll_dice(args.iterations, args.sides)


def flip_coin(iterations):

    if iterations > MAX_ITERATIONS or iterations < 0:
        print("Number of flips must be in the range [0 - {}]"
                .format(MAX_ITERATIONS))
        return

    coinRecord, numHeads, numTails = [], 0, 0
    for i in range(iterations):
        flip = random.randint(0, 1)
        if flip == 0:
            numHeads += 1
            coinRecord.append("H")
        else:
            numTails += 1
            coinRecord.append("T")

    print("{} coin flip(s) resulted in {} Heads and {} Tails:"
            .format(iterations, numHeads, numTails))
    print(*coinRecord, sep=', ')


def roll_dice(iterations, sides):

    # COMMIT 3: Restrict input range for dice iterations and sides
    if iterations > MAX_ITERATIONS or iterations < 0:
        print("Number of rolls must be in the range [0 - {}]"
                .format(MAX_ITERATIONS))
        return

    if sides > MAX_SIDES or sides < 1:
        print("Number of sides must be in the range [1 - {}]"
                .format(MAX_SIDES))
        return

    # COMMIT 2: Add dice rolling logic and output dice sum and sequence
    diceRecord, diceSum = [], 0
    for i in range(iterations):
        roll = random.randint(1, sides)
        diceRecord.append(roll)
        diceSum += roll

    print("{} roll(s) of a {}-sided die resulted in a sum of {}:"
            .format(iterations, sides, diceSum))
    print(*diceRecord, sep=', ')


if __name__ == "__main__":
    main()
