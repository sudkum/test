
tr -d '\r' < GOPURAM.txt > output
cat output | while read Line
do 
wget $Line
done