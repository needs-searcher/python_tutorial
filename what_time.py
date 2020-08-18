clock = int(input('what time is it?'))
hour = int(str(clock)[:-2])
minit = int(str(clock)[-2:])

if hour>=12:
    if minit<=59:
        print('%d시 %d분은 오후입니다' %(hour, minit))
    else:
        print("")
else:
    if minit<=59:
        print('%d시 %d분은 오전입니다' %(hour, minit))
    else:
        print("")
