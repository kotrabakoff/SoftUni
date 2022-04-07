examHour = int(input())
examMinute = int(input())
arrivalHour = int(input())
arrivalMinute = int(input())

totalMinutes_exam = examHour * 60 + examMinute
totalMinutes_arrival = arrivalHour * 60 + arrivalMinute
difference = abs(totalMinutes_exam - totalMinutes_arrival)

if totalMinutes_arrival > totalMinutes_exam:
    print("Late")
elif totalMinutes_exam - 30 <= totalMinutes_arrival <= totalMinutes_exam:
    print("On time")
elif totalMinutes_exam - 30 > totalMinutes_arrival:
    print("Early")

if totalMinutes_exam - 60 < totalMinutes_arrival < totalMinutes_exam:
    print(f"{difference} minutes before the start")
elif totalMinutes_exam - 60 >= totalMinutes_arrival:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif totalMinutes_exam + 60 > totalMinutes_arrival > totalMinutes_exam:
    print(f"{difference} minutes after the start")
elif totalMinutes_exam + 60 <= totalMinutes_arrival:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")

