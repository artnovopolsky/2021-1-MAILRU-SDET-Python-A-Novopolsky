#!/bin/bash

CURRENT_DIR=$(realpath $(dirname "$0"))
LOG_FILE=$(dirname "$CURRENT_DIR")/access.log
RES_FILE=$(dirname "$CURRENT_DIR")/results/bash_results.txt

# Задание 1
echo "Общее количество запросов:" > "$RES_FILE"
wc -l "$LOG_FILE" | awk '{print $1}' >> "$RES_FILE"

# Задание 2
echo -e "\nОбщее количество запросов по типу:" >> "$RES_FILE"
cat "$LOG_FILE" | awk '{print $6}' | sed 's/^"//' | sort | uniq -c | sort -rnk1 | awk '{printf "%d - %s\n", $1, $2}' >> "$RES_FILE"

# Задание 3
echo -e "\nТоп-10 самых частых запросов:" >> "$RES_FILE"
cat "$LOG_FILE" | awk '{print $7}' | sort | uniq -c | sort -rnk1 | head | \
    awk '{printf "URL: %s - Число запросов: %d.\n", $2, $1}' >> "$RES_FILE"

# Задание 4
echo -e "\nТоп-5 самых больших по размеру запросов, которые завершились клиентской (4XX) ошибкой:" >> "$RES_FILE"
cat "$LOG_FILE" | awk '{if ($9 ~ /4../) printf "%s %d %d %s\n", $7, $9, $10, $1}' | sort -rnk3 | head -n 5 | \
    awk '{printf "URL: %s - Статус: %d - Размер: %d - IP: %s.\n", $1, $2, $3, $4}' >> "$RES_FILE"

# Задание 5
echo -e "\nТоп-5 пользователей по количеству запросов, которые завершились серверной (5XX) ошибкой:" >> "$RES_FILE"
cat "$LOG_FILE" | awk '{if ($9 ~ /5../) print $1}' | sort -t "." -rnk1 | uniq -c | sort -rnk1 | head -n 5 | \
    awk '{printf "IP-адрес: %s. Кол-во запросов: %d\n", $2, $1}' >> "$RES_FILE"
