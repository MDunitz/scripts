# read in csv -> {'name': 'choices'}
import csv

import numpy as np


def read_csv():
    name_choice_dict = {}
    name_order = []
    with open('mentorship_match/form_response.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    for line in your_list:
        chocies = line[1].split(',')
        name = line[0]
        name_order.append(name)
        name_choice_dict[name] = chocies


# score against each other (n^2)
## make chocies sets
##


def score_mentor_pair(traits0=[3,4,5], traits1=[1,2,3,4,5], max_traits=10):
    trait_0_len = len(set(traits0))
    trait_1_len = len(set(traits1))
    total_len = len(set(traits0 + traits1))

    matches = (trait_0_len + trait_1_len - total_len)
    print(matches)


def score_mentee_pair(traits0=[3,4,5], traits1=[1,2,3,4,5], max_traits=10):
    trait_0_len = len(set(traits0))
    trait_1_len = len(set(traits1))
    total_len = len(set(traits0 + traits1))

    matches = (trait_0_len + trait_1_len - total_len)
    print(matches)

# propose to each other

def match_for_minimum_score(matrix):
    cost = np.array(matrix)
    from scipy.optimize import linear_sum_assignment
    row_ind, col_ind = linear_sum_assignment(cost)

    cost[row_ind, col_ind].sum()
    return row_ind, col_ind
# propose again with previous removed from comparison



def main():
    score_pair()


if __name__ == "__main__":
    main()
