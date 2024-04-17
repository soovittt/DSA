cmake_minimum_required(VERSION 3.27)
project(DSA)

set(CMAKE_CXX_STANDARD 14)

add_executable(DSA
        Arrays/1_Array_DS_Basic.cpp
        Arrays/2_Array_DS_hourglass.cpp
        Graphs/3_find_Center_graph.cpp
        "Problem Solving/2_Climbing_Leaderboard.cpp"
        "Problem Solving/4_Queens_Attack.cpp"
        "Problem Solving/5_grading_policy.cpp"
        "Problem Solving/6_Organising_Container.cpp"
        Stacks/stacks_using_vector.cpp
        Tree/BinaryTree.py
        Tree/tree_breadth_first.py
        Tree/tree_depth_first.py
        Tree/tree_includes.py
        Tree/tree_min_value.py)
