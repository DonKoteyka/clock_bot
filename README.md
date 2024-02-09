# БОТ ПОГОДЫ

команды для установленного интерпретатора python 

1. Установка компонентов (Ubuntu)
```bash
sudo apt install python3-venv python3-pip
```
2. Установка среды
```bash
python3 -m venv env
```
```bash
source env/bin/activate
```
3. Установка библиотек
```bash
pip install -r requirements.txt
```
4. Для первого запуска может понадобиться инициализация ДБ:
```bash
python models.py
```

5. Запуск бота
```bash
python main.py
```
все желающие должны отправить команду `/start` боту `https://t.me/Wether_Krd_bot` для регистрации в расслке
внеочередное получение прогноза `/weather`

5. Запуск таймера
```bash
python clock.py
```
для настойки таймера нужно установить время рассылки `RING_TIME=08:00` в файле `.env`