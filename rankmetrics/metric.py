'''
Implementation of the nDCG metric for ranking evaluation.

Balazs Kovacs, 2017
'''

import numpy as np


def dcg(rel_scores, k=None, use_exp=False):
    '''
    Computes the DCG metric as defined in https://en.wikipedia.org/wiki/Discounted_cumulative_gain

    :param rel_scores: List of relevance scores.
    :param k: We will compute DCG@k. If k is None, we will set it to
    len(rel_scores).
    :param use_exp: If True, we use 2 ** (relevance score) - 1 in the numerator
    instead of (relevance score).

    :returns: The DCG score of the input
    '''

    if k is None:
        k = len(rel_scores)

    rel_scores = np.array(rel_scores, dtype=float)[:k]
    if use_exp:
        num = 2 ** rel_scores - 1
    else:
        num = rel_scores

    den = np.log2(np.arange(k) + 2)
    return np.sum(num / den)


def ndcg(rel_scores, k=None, use_exp=False):
    '''
    Computes the nDCG metric as defined in https://en.wikipedia.org/wiki/Discounted_cumulative_gain#Normalized_DCG

    :param rel_scores: List of relevance scores.
    :param k: We will compute nDCG@k. If k is None, we will set it to
    len(rel_scores).
    :param use_exp: If True, we use 2 ** (relevance score) - 1 in the numerator
    instead of (relevance score).

    :returns: The nDCG score of the input
    '''

    if k is None:
        k = len(rel_scores)

    dcg_val = dcg(rel_scores=rel_scores, k=k, use_exp=use_exp)
    idcg_val = dcg(rel_scores=sorted(rel_scores, reverse=True), k=k, use_exp=use_exp)

    return dcg_val / idcg_val


#if __name__ == '__main__':
    #r = [3, 2, 3, 0, 1, 2]
    #for use_exp in [False, True]:
        #print dcg(rel_scores=r, use_exp=use_exp)
        #print ndcg(rel_scores=r, use_exp=use_exp)
