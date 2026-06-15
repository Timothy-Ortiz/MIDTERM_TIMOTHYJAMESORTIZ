mkdir -p MIDTERM/{PythonScripts,PostmanCollection,Documentation,Screenshots,Recordings,Backup}

touch MIDTERM/Documentation/student_info.txt
touch MIDTERM/Documentation/log.txt

echo "Complete Name: Timothy James B. Ortiz" > MIDTERM/Documentation/student_info.txt
echo "Course and Section: BSIT-2" >> MIDTERM/Documentation/student_info.txt
echo "Date Executed: $(date)" >> MIDTERM/Documentation/student_info.txt

echo "Current Date and Time:"
date

echo "Current User:"
whoami

echo "Current Working Directory:"
pwd

echo "IP Address:"
hostname -I

cp MIDTERM/Documentation/* MIDTERM/Backup/

tar -czvf backup.tar.gz MIDTERM/Backup

ls -R MIDTERM
