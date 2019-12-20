#!/bin/bash
<<LongComment
This script is used to
Calculate the cube of
a number with value 5
LongComment
#Set the value of n
n=5
#Calculate 5 to the power 3
((result=$n*$n*$n))
#Print the area
echo $result
