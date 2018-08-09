
tr -d '\r' < MANDAPA.txt > output
cat output | while read Line
do 
wget $Line
done