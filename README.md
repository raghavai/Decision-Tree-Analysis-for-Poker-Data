## Decision Tree Analysis for Poker Hand Data

Decision Tree is a data mining method that is applied on data that assumes discrete values. The tree is partitioned recursively based on a selected attribute until we arrive at a leaf node with a single class distribution or no more attributes remain for further partitioning. In our case, the statistical measure based on which the test attribute is selected is Information Gain.

The test data in this case is Poker Hand Data which is uploaded too. The details of the dataset is provided [here](http://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand.names).

The Decision tree is created as follows:

 * Calculate Entropy for the entire dataset (e0)
 * Calculate Weighted Entropy for each attribute (wc)
 * Calculate Information Gain for each attribute (e0 - wc)
 * The attribute with the maximum Information Gain becomes the splitting factor.
 
###Running the code 

The mapper and reducer are written in Python and run in the Hadoop environment. The mapper takes input from the standard input. I hope you know the basics of running a program in hadoop.

Since the dataset is huge (over 1 million records), I ran it on Hadoop as follows:
```javascript
hs mapper.py reducer.py <input_directory> <output_directory>
```

However, the entire hadoop framework can be simulated on the unix environment for the same dataset with limited records by piping the mapper to the test data and in turn piping it to the reducer as follows:
```javascript
head -50 poker-hand-testing.data > testfile
cat testfile | ./mapper.py | sort | ./reducer.py
```

## General Public License (GPL)
```javascript
Copyright 2014 Aarthi Raghavendra

This is a free software and you can redistribute it or/and modify under the terms of the GNU General Public License as published by Aarthi Raghavendra.

If you have not received a copy of the GNU General Public License along with this program please visit <www.gnu.org/licenses/>.
```

