import os
import combine
import download

home_path = '/home/yuh/'
path_yuh = '/home/yuh/rs/'
error_main = []

with open("/home/yuh/rs/dl.txt", "r", encoding='utf') as dl:
    for line in dl:
        one = line.split(' ', 4)
        # print(one)
        month = one[0]
        time = one[1]
        lesson = one[2]
        url = one[3].split('_')[0] + '_' + one[3].split('_')[1] + '_'
        num = int(one[3].split('_')[2].split('.')[0])
        # print(month, time, lesson, url, num)

        os.makedirs(home_path+month+'/'+time+'/'+lesson, mode=0o777, exist_ok=True)
        os.makedirs(home_path+'错误信息细节', mode=0o777, exist_ok=True)

        print('"' + home_path+month+'/'+time+'/'+lesson + '" ' "目录已创建")

        right = download.dl(month, time, lesson, home_path, url, num)

        error_main = []
        if right == 1:
            combine.cb(month, time, lesson, home_path, num, path_yuh)
        else:
            error = month + ' ' + time + ' ' + lesson + ': ' + url + ' ' + str(right)
            print(error)
            with open('/home/yuh/rs/错误信息.txt', 'a') as f:
                f.write(str(error))
                f.write('\n')
            error_main.append(error)

print(error_main)

# 1.25 am 物理 http://2001.tbovod.myqcloud.com/xzonesz/31002_b8357d671d9688f1_17.ts
# 1.25 pm 化学 http://2001.tbovod.myqcloud.com/xzonesz/31002_b8357d671d9688f1_7.ts
# 1.26 eve 语文 http://2001.tbovod.myqcloud.com/xzonesz/31002_b8357d671d9688f1_27.ts
