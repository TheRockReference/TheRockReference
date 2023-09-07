#!/bin/bash
echo " "
echo "--------------------------------"
echo -n "\$0" is the script name = 
echo "$0"
echo "---------------------------------"

echo " "
echo "---------------------------------"
echo -n "\$PWD" is the script path = 
echo "$PWD"
echo "---------------------------------"
echo " "
echo "---------------------------------"
python3 "/home/slaroche/Documents/GitHub/TheRockReference/python/learning_test/print/print_2-end_Fibonacci.py"
echo " "
echo "---------------------------------"
echo " "

echo "The script you are running has:"
echo "basename: [$(basename "$0")]"
echo "dirname : [$(dirname "$0")]"
echo "pwd     : [$(pwd)]"

python3 "/home/slaroche/Documents/GitHub/TheRockReference/python/learning_test/print/print_1-several_variables_separated_by_comma.py"

python3 --version
