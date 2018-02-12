
def cb(date1, date2, lesson, home_path, num, path_yuh):

    import subprocess
    import os
    import shutil

    def tss_mp4(n1, n2, n, file_path , file_name, new_file_path='tss_mp4'):

        # (n1,n2)合并的ts文件数目范围
        # n 产生的mp4文件名
        # file_path ts文件所在目录
        # file_name 原来的ts文件命名规律out1.ts 则为out
        # new_file_path 在原来的目录下创建新的目录名
        new_file_paths = file_path + new_file_path

        d = os.path.exists(new_file_paths)

        if not d:
            ml_mkdir = 'mkdir ' + new_file_paths
            out1 = subprocess.Popen(ml_mkdir, shell=True)
            out1.wait()

        new_mp4_name = 'out' + str(n) + '.mp4'

        ff = 'ffmpeg -i '
        file_names = ''

        for i in range(n1, n2):
            file_names = file_names + file_path + file_name + str(i) + '.ts' + '|'

        concat = '"concat:' + file_names + file_path +file_name+ str(n2) + '.ts'

        # print(st)
        ml_ts_tss = ff + concat + '" -acodec copy -vcodec copy -absf aac_adtstoasc ' + new_file_paths + '/' + new_mp4_name

        print(ml_ts_tss)
        # exit()
        out2 = subprocess.Popen(ml_ts_tss, shell=True)
        out2.wait()

    def mp4_ts(old_file_name, old_file_path, new_file_name, new_file_path='mp4_ts'):
        # (n1,n2)合并的ts文件数目范围
        # file_path ts文件所在目录
        # file_name 原来的ts文件命名规律out1.ts 则为out
        # new_file_path 在原来的目录下创建新的目录名

        new_file_paths = old_file_path + new_file_path
        d = os.path.exists(new_file_paths)
        if not d:
            ml_mkdir = 'mkdir ' + new_file_paths
            out1 = subprocess.Popen(ml_mkdir, shell=True)
            out1.wait()

        ff = 'ffmpeg -i '

        ml_mp4_ts = ff + old_file_path + old_file_name + ' -vcodec copy -acodec copy -vbsf h264_mp4toannexb '\
                    + new_file_paths + new_file_name

        # print(ml_mp4_ts)
        # exit()

        out2 = subprocess.Popen(ml_mp4_ts, shell=True)
        out2.wait()

    def tss_ts(n1, n2, n, file_path , file_name, new_file_path='tss_ts'):

        # (n1,n2)合并的ts文件数目范围
        # file_path ts文件所在目录
        # file_name 原来的ts文件命名规律out1.ts 则为out
        # new_file_path 在原来的目录下创建新的目录名

        new_file_paths = file_path + new_file_path
        d = os.path.exists(new_file_paths)
        if not d:
            ml_mkdir = 'mkdir ' + new_file_paths
            out1 = subprocess.Popen(ml_mkdir, shell=True)
            out1.wait()

        new_mp4_name = 'out' + str(n) + '.mp4'

        ff = 'ffmpeg -i '
        file_names = ''

        for i in range(n1, n2):
            file_names = file_names + file_path + file_name + str(i) + '.ts' + '|'

        concat = '"concat:' + file_names + file_path + file_name + str(n2) + '.ts'
        # print(st)
        ml_tss_mp4 = ff + concat + '" -acodec copy -vcodec copy -absf aac_adtstoasc ' + new_file_paths + '/' + new_mp4_name

        print(ml_tss_mp4)
        # exit()
        new_ts = 'out' + str(n) + '.ts'

        ml_mp4_ts = ff + new_file_paths + '/' + new_mp4_name + ' -vcodec copy -acodec copy -vbsf h264_mp4toannexb ' + new_file_paths + '/' + new_ts

        print(ml_mp4_ts)
        # exit()

        out1 = subprocess.Popen(ml_tss_mp4, shell=True)
        out1.wait()
        out2 = subprocess.Popen(ml_mp4_ts, shell=True)
        out2.wait()

    name = date1 + date2 + "." + lesson + ".mp4"

    file_path = home_path + date1 + "/" + date2 + "/" + lesson + "/"

    file_name = ''

    files = os.listdir(file_path)
    j = 0
    print(files)
    for i in files:
        for k in str(i):
            if k == '.':
                j = j + 1
                break

    files_n = j

    print(files_n)

    # exit()

    if num == files_n:

        qu_zheng = files_n // 1000
        print(qu_zheng)

        if qu_zheng != 0:

            for i in range(1, qu_zheng+1):
                print(str((i)), str(i))
                tss_ts((i), (i)*1000, i, file_path, file_name, 'tss_ts')

            tss_ts(qu_zheng*1000, files_n, qu_zheng+1, file_path, file_name, 'tss_ts')
            # exit()
            tss_ts_file_path = file_path + 'tss_ts/'

            if qu_zheng < 1000:
                tss_mp4(1, qu_zheng + 1, qu_zheng + 1, tss_ts_file_path, 'out', 'success')

        else:

            print(str(qu_zheng) + ' ' + str(files_n+1) + ' ' + file_path + ' ' + file_name)

            tss_mp4(qu_zheng+1, files_n, qu_zheng+1, file_path, file_name, 'success')

    if num < 1000:
        cache_path = file_path + "success"
        success_old = file_path + "success/out1.mp4"
        success_new = file_path + "success/" + name

    else:
        cache_path = file_path + "tss_ts"
        success_old = file_path + "tss_ts/success/out2.mp4"
        success_new = file_path + "tss_ts/success/" + name

    os.renames(success_old, success_new)

    shutil.copy(success_new, path_yuh)
    shutil.rmtree(cache_path)