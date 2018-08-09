
tr -d '\r' < AMALAKA.txt > output
cat output | while read Line
do 
wget $Line
done