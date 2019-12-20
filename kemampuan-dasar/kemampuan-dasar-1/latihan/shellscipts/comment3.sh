#!/bin/bash
#Initialize the variable n with a number
n=15
: '
The following script will check the number is
Even or odd by dividing the number by 2 and checking the remainder value
'
if (( $n % 2 == 0 ))
then
     echo "The number is even"
else

     echo "The number is odd"
fi
