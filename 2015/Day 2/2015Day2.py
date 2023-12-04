
with open("2015Day2.txt",'r') as fp:
        runningTotal = 0
        for line in fp:
            l,w,h = line.split('x')
            l,w,h = int(l),int(w),int(h)
            sArea = (2*l*w) + (2*w*h) + (2*h*l)
            slack = min([l*w,w*h,h*l])
            # print(f'{sArea + slack}')
            runningTotal += sArea + slack
        print(runningTotal)
        
        

with open("2015Day2.txt",'r') as fp:
        runningTotal = 0
        for line in fp:
            l,w,h = line.split('x')
            l,w,h = int(l),int(w),int(h)
            volume = l*h*w
            bow = min([2*(l+w),2*(w+h),2*(h+l)])
            # print(f'{volume + bow}')
            runningTotal += volume + bow
        print(runningTotal)