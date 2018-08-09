
tr -d '\r' < TORANA.txt > output
cat output | while read Line
do 
wget $Line
done