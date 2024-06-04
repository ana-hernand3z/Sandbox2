# Sandbox 2 - GP and Data Cardinality

This is an assignment for Genetic Algorithms class at Dalhousie University under Professor Malcom Heywood.

The objective was to extend a canonical GP (Sandbox 1) and give training data that requires resampling for better results. In this sandbox, the data was re sampled using a value $\tau$. For this sandbox, the runs performed were focused on changing the value of $\tau$

This GP 's fitness function is the following:
$A = \frac{1}{N} \sum_{c=1...|C|} \text{tp(c)}$

Where $N$ is the length of the data subset and $tp(c)$ is the true positives for each class. 

Once the training is done, the testing begins. The testing performs a run using the accuracy as fitness function and then looks for the highest class detection rate. The class detection rate is determined by the following equation
$\textnormal{DR} = \frac{1}{|C|} \sum_{c=1...|C|} \textnormal{DR(c) where DR(c)} = \frac{tp(c)}{tp(c)+fn(c)}$

Which calculates the true positive counts for each class divided by the true positives and false negatives count of the class. 

Therefore, at the end of each run, we have a program that was chosen and trained based on the highest accuracy and a second one that was chosen but not trained on class detection. 
