import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        # given in problem we assume the correct datatypes are made
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    dna_dbase = sys.argv[1]
    with open(dna_dbase, "r") as f:
        reader = csv.DictReader(f)
        dbase = list(reader)

    # print(dbase)

    # TODO: Read DNA sequence file into a variable
    dna_seq = sys.argv[2]
    with open(dna_seq, "r") as g:
        # read returns contents of file as one string
        DNA_sequence = g.read()

    # there are more than 3 :)
    # str_list = ["AGAT","AATG","TATC"]

    nr_substr = {}

    # get all required subsequences (keys) from the one dictionary out of the list,
    # beginning from the 2nd (or in coding number, 1st)
    subsequences = list(dbase[0].keys())[1:]

    # print(subsequences)

    # TODO: Find longest match of each STR in DNA sequence
    for sub in subsequences:
        nr_substr[sub] = longest_match(DNA_sequence, sub)

    # TODO: Check database for matching profiles
    for person in dbase:
        match_count = 0
        for sub in subsequences:
            if int(person[sub]) == nr_substr[sub]:
                match_count += 1

        if match_count == len(subsequences):
            print(person["name"])
            return

    print("No match.")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
