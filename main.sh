
tr -d '\r' < 6_all.txt > output
cat output | while read Line
do 
wget $Line
done