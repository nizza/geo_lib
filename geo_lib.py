from __future__ import division
import numpy as np
import unittest

def project_geo_stats(A, method = "weighted_avg"):
    """
    Project a statistic p from from a list of input geometries A_1,...,A_n, to an output geometry B.

    The inputs of the function are:

        - a list A_1,...,A_n, of input geometries, where each geometry A_j defined as a tuple (p_j, I_j),where, 
            *  p_j is the statistic associated with the geometry
            *  I_j is the surface of the intersection between the the geometry A_j, and the geometry B;
        - method, a string defining the aggregation method for the statistics. The available option being,
            * weighted_sum => the output statistic is a weighted of the input statistic, using the overlap surface 
            as weights;
            * weighted_avg => the output statistic is a weighted of the input statistic, using the overlap surface 
            as weights;
    """

    # Weighting each statistic pj by the intersection area
    P_w = [p_j*I_j for p_j,I_j in A]
    
    # Computing the resulting statistic
    if method == "weighted_avg":
        return np.sum(P_w) / np.sum([a[1] for a in A])
    elif method == "weighted_sum":
        return np.sum(P_w) 
    else:
        raise Exception('Invalid method: {0}'.format(method))

        
def distibute_geo_stats(p, W):
    """
    Distributes a statistic p to a list of geometries A_1,...,A_n according to their respective relative weights W_1,...,W_n .

    The inputs of the function are:
    
        - the statistic p to be distributed;
        
        - a list W_1,...,W_n with the realtive weights of the target geometries

    """

    # Normalizing the weights
    W_n = [W_i/sum(W) for W_i in W]
    
    # Redistributing the static 
    P_w = [p * W_i for W_i in W_n]
    
    return P_w
    


class MyTest(unittest.TestCase):
    
    # project_geo_stats
    def test_1(self):
        " weighted_avg with same weight"
        A = [(5,1), (10,1)]
        self.assertEqual(project_geo_stats(A), 7.5)
    
    def test_2(self):
        " weighted_avg weight different weight"
        A = [(5,4), (10,1)]
        self.assertEqual(project_geo_stats(A), 6)

    def test_3(self):
        " weighted_sum with same weight"
        A = [(5,1), (10,1)]
        self.assertEqual(project_geo_stats(A, "weighted_sum"), 15)
        #self.assertTrue(True)
    
    def test_4(self):
        " weighted_sum weight different weight"
        A = [(5,4), (10,1)]
        self.assertEqual(project_geo_stats(A, "weighted_sum"), 30) 
    
    # distibute_geo_stats
    def test_5(self):
        " same weight"
        W= [1, 1]
        self.assertEqual(distibute_geo_stats(5, W), [2.5, 2.5])

    def test_6(self):
        " different weight"
        W= [2, 1]
        self.assertEqual(distibute_geo_stats(6, W), [4, 2])

if __name__ == '__main__':
    unittest.main()


