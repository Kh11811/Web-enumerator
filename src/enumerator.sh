#!/bin/bash

if [ $# -ne 2 ]
then
echo "missing arguments"
exit 1
fi
for word in $`cat $1`
do
response=$(curl -I $2/$word 2>/dev/null | grep HTTP |cut -d " " -f2)
if [ "$response" -le 399 ]
then
echo "$word : $response"

fi
done

