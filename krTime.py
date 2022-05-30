from random import randint

hour= randint(8,22)
hour2=hour
start=randint(0,59)
while True:
    end=randint(15,59)
    if end > 15:
        break
end=start+end
if end > 59 :
    hour2=hour+1
    end=end%60
time = f'{hour}:{start}-{hour2}:{end}'

