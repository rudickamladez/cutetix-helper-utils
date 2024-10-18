#!/bin/bash

docker compose exec mariadb mariadb -uroot -p cutetix-backend -e "SELECT DISTINCT email FROM tickets WHERE status != 'cancelled' AND group_id BETWEEN 28 AND 47;" > ~/pohles24-emails.txt

