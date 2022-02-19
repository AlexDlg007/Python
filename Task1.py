duration = input('Введите промежуток')

duration = int(duration)

if duration < 60: # секунды
    print(duration, ' сек.')
elif duration >= 60 and duration < 3600: # минуты

    Minutes = duration // 60
    Secunds = duration % 60

    print(Minutes, ' мин., ', Secunds, ' сек.')

elif duration >= 3600 and duration < 86400:  # часы

    Hours = duration  // 3600
    Minutes = (duration - (Hours * 3600)) // 60
    Secunds = duration % 60

    print(Hours, ' ч., ', Minutes, ' мин., ', Secunds, ' сек.')

else:

    Days = duration // 86400
    Hours = (duration - (Days * 86400)) // 3600
    Minutes = (duration - (Days * 86400) - (Hours * 3600)) // 60
    Secunds = duration % 60
    print(Days, 'д.', Hours, ' ч., ', Minutes, ' мин., ', Secunds, ' сек.')

