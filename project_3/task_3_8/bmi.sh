echo "Введите массу тела (в кг):"
read weight

echo "Введите рост (в метрах):"
read height

bmi=$(echo "$weight $height" | awk '{printf "%d", $1 / ($2 * $2)}')

echo "Ваш индекс массы тела: $bmi"
