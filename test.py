# pyunit test
import unittest

# python3 -m unnittest test.py


class Test(unittest.TestCase):
    @unittest.skip("solved")
    def test_1918(self):
        from class4.ex_1918 import solution

        self.assertEqual("ABC+*", solution("A*(B+C)"))
        self.assertEqual("AB+", solution("A+B"))
        self.assertEqual("ABC*+", solution("A+B*C"))
        self.assertEqual("ABC*+DE/-", solution("A+B*C-D/E"))

    @unittest.skip("solved")
    def test_5639(self):
        from class4.ex_5639 import solution
        node_list = [50, 30, 24, 5, 28, 45, 98, 52, 60]
        result_list = [5, 28, 24, 45, 30, 60, 52, 98, 50]

        self.assertEqual(result_list, solution(node_list))

    # -----dp 방식----
    @unittest.skip("solved")
    def test_11444(self):
        from class4.ex_11444_dp import solution
        n = 1000

        self.assertEqual(517691607, solution(n))

    @unittest.skip("solved")
    def test_11444_range17(self):
        from class4.ex_11444_dp import solution
        fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                    55, 89, 144, 233, 377, 610, 987, 1597]

        for i in range(2, len(fib_list)):
            self.assertEqual(fib_list[i], solution(i))

    @unittest.skip("solved")
    def test_11444_time_limit(self):
        from class4.ex_11444_dp import solution
        max = 1000000000000000000 - 1
        solution(max)

    # ------분할 정복 방식-----
    @unittest.skip("solved")
    def test_11444(self):
        from class4.ex_11444_div_con import solution
        n = 1000

        self.assertEqual(517691607, solution(n))

    @unittest.skip("solved")
    def test_11444_range17(self):
        from class4.ex_11444_div_con import solution
        fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                    55, 89, 144, 233, 377, 610, 987, 1597]

        for i in range(2, len(fib_list)):
            self.assertEqual(fib_list[i], solution(i))

    @unittest.skip("solved")
    def test_11444_time_limit(self):
        from class4.ex_11444_div_con import solution
        max = 1000000000000000000 - 1
        solution(max)

    @unittest.skip("solved")
    def test_12865(self):
        from class4.ex_12865 import solution
        N, K = 4, 7
        backpack = [[6, 13], [4, 8], [3, 6], [5, 12]]
        result = 14
        
        self.assertEqual(result, solution(N, K, backpack))

    @unittest.skip("solved") 
    def test_12865_edge(self):
        from class4.ex_12865 import solution
        N, K = 1, 2
        backpack = [[1, 3] ]
        result = 3
        
        self.assertEqual(result, solution(N, K, backpack))

    @unittest.skip("solved") 
    def test_12865_edge2(self):
        from class4.ex_12865 import solution
        N, K = 10, 999
        backpack = [[46, 306],[60, 311],[33, 724],[18, 342],[57, 431],[49, 288],[12, 686],[89, 389],[82, 889],[16, 289]]
        result = 4655
        
        self.assertEqual(result, solution(N, K, backpack))

    @unittest.skip("solved") 
    def test_12865_edge3(self):
        from class4.ex_12865 import solution
        N, K = 3, 5
        backpack = [[4, 2], [3, 4], [1, 5]]
        result = 9
        
        self.assertEqual(result, solution(N, K, backpack))
    
    def test_22352_1(self):
        from ex_22352 import Ex_22352
        N, M = 4, 4
        before = [
            [2, 2, 2, 1],
            [2, 2, 1, 3],
            [2, 1, 3, 3],
            [1, 3, 3, 3]
        ]
        after = [
            [4, 4, 4, 1],
            [4, 4, 1, 3],
            [4, 1, 3, 3],
            [1, 3, 3, 3]
        ]
        ex = Ex_22352(N, M, before, after)
        ex.solve()
        self.assertEqual(None, ex.find_diff_node())
        
    def test_22352_2(self):
        from ex_22352 import Ex_22352
        N, M = 4, 4
        before = [
            [2, 2, 2, 1],
            [2, 2, 1, 3],
            [2, 1, 3, 3],
            [1, 3, 3, 3]
        ]
        after = [
            [2, 2, 2, 1],
            [2, 2, 1, 3],
            [2, 1, 3, 3],
            [1, 3, 3, 3]
        ]
        ex = Ex_22352(N, M, before, after)
        ex.solve()
        self.assertEqual(None, ex.find_diff_node())
    
    def test_22352_3(self):
        from ex_22352 import Ex_22352
        N, M = 4, 4
        before = [
            [2, 2, 2, 1],
            [2, 2, 1, 3],
            [2, 1, 3, 3],
            [1, 3, 3, 3]
        ]
        after = [
            [2, 2, 2, 1],
            [2, 2, 2, 3],
            [2, 1, 3, 3],
            [1, 3, 3, 3]
        ]
        ex = Ex_22352(N, M, before, after)
        ex.solve()
        self.assertEqual(None, ex.find_diff_node())
        
    def test_22352_4(self):
        from ex_22352 import Ex_22352
        N, M = 4, 4
        before = [
            [2, 2, 2, 1],
            [2, 2, 1, 2],
            [2, 1, 2, 2],
            [1, 2, 2, 2]
        ]
        after = [
            [3, 3, 3, 1],
            [3, 3, 1, 3],
            [3, 1, 3, 3],
            [1, 3, 3, 3]
        ]
        ex = Ex_22352(N, M, before, after)
        ex.solve()
        self.assertNotEqual(None, ex.find_diff_node())
        
    def test_22352_5(self):
        from ex_22352 import Ex_22352
        N, M = 3, 5
        before = [
            [1, 1, 1, 3, 3],
            [1, 1, 2, 3, 3],
            [1, 1, 2, 2, 4]
        ]
        after = [
            [1, 1, 1, 4, 4],
            [1, 1, 2, 4, 4],
            [1, 1, 2, 2, 4]
        ]
        ex = Ex_22352(N, M, before, after)
        ex.solve()
        self.assertEqual(None, ex.find_diff_node())