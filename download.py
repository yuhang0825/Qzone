from Date import *


def dl(date1, date2, lesson, home_path, url, num):
    global p
    import urllib.request
    import socket
    from multiprocessing import Process

    data = date1 + '/' + date2 + '/' + lesson + '/'

    def dl(n, error):
        path = home_path + data + str(n) + '.ts'
        print(path)
        urln = url + str(n) + '.ts'
        print(urln)
        try:
            socket.setdefaulttimeout(30)
            urllib.request.urlretrieve(urln, path)
            print(str(n)+' success')
        except Exception as e1:
            print(str(n)+' error ' + str(e1))
            error.append(n)

    error0 = []

    def dl_P(P_n1, P_n2):
        for i in range(P_n1, P_n2):
            dl(i, error0)

    batchSize = (num+1) // process_n

    for i in range(process_n):
        if i != process_n-1:
            p = Process(target=dl_P, args=(i*batchSize+1, (i+1)*batchSize+1))
        else:
            p = Process(target=dl_P, args=(i*batchSize+1, num+1))
        p.start()
    p.join()

    print(error0)

    if len(error0) == 0:
        return 1
    else:
        error0_path = home_path + '错误信息细节/' + date1 + date2 + lesson + 'error.txt'
        with open(error0_path, 'a') as error0_file:
            for error in error0:
                error0_file.write(str(error) + ' ')
            error0_file.write('\n')

        error1 = []
        for j in error0:
            j1 = str(j)
            dl(j1, error1)
        if len(error1) != len(error0):
            with open(error0_path, 'a') as error1_file:
                for error in error0:
                    error1_file.write(str(error) + ' ')
                error1_file.write('已修复' + '\n')
            if len(error1) == 0:
                return 1
            else:
                return error1

        else:
            return error0
