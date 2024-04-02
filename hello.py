print(2+2)
awk -F '|' 'NR > 2 && NF > 1 {gsub(/^[ \t]+|[ \t]+$/, "", $2); gsub(/^[ \t]+|[ \t]+$/, "", $3); print "Library:", $2, "Vulnerability ID:", $3}' trivy_output.txt
