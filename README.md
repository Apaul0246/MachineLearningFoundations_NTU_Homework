# MachineLearningFoundations_NTU_Homework
Python code for assignments of Machine Learning Foundations from National Taiwan University (Hsuan-Tien Lin).
http://www.csie.ntu.edu.tw/~htlin/mooc/

Homework 1 Question 15 

Implement a version of PLA by visiting examples in the naive cycle using the order of examples in the data set. Run the algorithm on the data set. What is the number of updates before the algorithm halts? What is the index of the example that results in the “last” mistake?

See Naive_PLA.py

Homework 1 Question 16

Implement a version of PLA by visiting examples in fixed, pre-determined random cycles throughout the algorithm. Run the algorithm on the data set. Please repeat your experiment for 2000 times, each with a different random seed. What is the average number of updates before the algorithm halts? Plot a histogram to show the number of updates versus frequency.

Homework 1 Question 17

Implement a version of PLA by visiting examples in fixed, pre-determined random cycles throughout the algorithm, while changing the update rule to be
**_wt+1 ← wt + ηyn(t)xn(t)_**
with η = 0.5. Note that your PLA in the previous problem corresponds to η = 1. Please repeat your experiment for 2000 times, each with a different random seed. What is the average number of updates before the algorithm halts? Plot a histogram to show the number of updates versus frequency. Compare your result to the previous problem and briefly discuss your findings

See Random_Cycle_PLA.py