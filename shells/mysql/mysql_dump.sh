#!/usr/bin/env expect

ENV=$1
DB=$2
if [ ! $DB ]
then
	DB='tmddev'
fi
REMOTE_NAME='root'

dump(){
	echo ${4}.sql
	mysqldump --default-character-set=utf8mb4 --routines --single-transaction --force -v \
		--add-drop-table --create-options --quick --extended-insert --compress \
		-u ${REMOTE_NAME} -p -h $1 -P $2 $3 > ${4}.sql

	mysql -u root -p -h $5 -P $6 $3 < ${4}.sql
} 

main(){
	FILE=$4/$3_`date +%Y-%m-%d_%H:%M:%S`
	dump $1 $2 $3 $FILE $5 $6
}

if [ ! ${ENV} ]
then
	echo "Uage:./mysql_dump.sh <local|dev|prod>"
else
	if [ ${ENV} == 'local' ]
	then
		main 192.168.99.100 32770 $DB /data/sql 127.0.0.1 3306
	elif [ $ENV == 'wxnacy' ]
	then
		main 101.200.193.65 3506 $DB /data/sql 127.0.0.1 3306
	elif [ ${ENV} == 'dev' ]
	then
		REMOTE_NAME='hamsterroot'
		main hamster-dev.cz0vfyqftzrn.us-west-2.rds.amazonaws.com 3306 $DB /data/sql 127.0.0.1 3306
	elif [ ${ENV} == 'prod' ]
	then
		REMOTE_NAME='hamsterapiserver'
		main hamsterprd.cz0vfyqftzrn.us-west-2.rds.amazonaws.com 3306 $DB /data/sql 127.0.0.1 3306
	fi
fi



# tmddev | gzip > temdev.sql.gz

# mysql -u root -p -h 127.0.0.1 -P 3306 tmddev < temdev.sql

