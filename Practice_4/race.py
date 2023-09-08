from import_this import RACE_DATA

def retreive_racer_data(race_data: RACE_DATA) -> dict[dict]:
    all_racers = {}
    for i in race_data.values():
        all_racers.update({i.get("FinishedPlace"):i})
    return all_racers

def convert_time(seconds: int) -> str:
    return f"{seconds//3600:02d}:{seconds%3600//60:02d}:{seconds%3600%60:02d}"      # :02d -- выводить всегда 2 цифры (даже если частное однозначно)

def display_finish_message(race_data: RACE_DATA):
    sorted_racers = retreive_racer_data(race_data)

    print(f"Выиграл - {sorted_racers.get(1).get('RacerName')}!!! Поздравляем!!")
    print("_"*40, "\n")
    print("Первые три места: \n\n")

    for i in range(1, 4):
        print(f"Гонщик на {i} месте:")
        print(f"\tИмя: {sorted_racers.get(i).get('RacerName')}\n\tКоманда: {sorted_racers.get(i).get('RacerTeam')}\n\tВремя: {convert_time(sorted_racers.get(i).get('FinishedTimeSeconds'))} (H:M:S)\n")

if __name__ == "__main__":
    display_finish_message(RACE_DATA)