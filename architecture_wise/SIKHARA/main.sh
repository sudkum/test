
tr -d '\r' < SIKHARA.txt > output
cat output | while read Line
do 
wget $Line
done