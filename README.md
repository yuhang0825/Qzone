# Qzone
**QQ直播视频批量下载（目前为半自动）**  
（linux系统可用，文件缓存路径自己根据自己的电脑修改)
* QQ空间直播视频不能下载，而且一般有权限设定，
  发现通过浏览器F12，可以查看视频流中的TS文件链接，一般2个小时的直播视频，被分割成千多个TS文件，没有权限限制，可直接下载，而且可用时长很久

* Windows在cmd合并时，容易出现视频与语音不同步

* 为了方便批量下载，可以将准备下载的直播视频的最后一个ts链接（为了确定单次直播视频中一共有多少个ts文件）
  按照如下格式写入txt文件，路径在main代码中指定

  1.31 am 化学 http://2001.tbovod.myqcloud.com/xzonesz/31002_b8357d671d818c5d_1264.ts  
  1.30 am 数学 http://2001.tbovod.myqcloud.com/xzonesh/31002_b8357d671d7a6cd6_1397.ts  
  1.30 am 英语 http://2001.tbovod.myqcloud.com/xzonesz/31002_b8357d671d7a0854_968.ts  
  
  这段代码将会
  1. 把所有的视频按照日期，上下午，视频名称分别写入不同的文件夹，下载所有的ts文件  
  2. 下载时有超时限制，防止程序因网络原因卡死。  
  3. 校正一次是否所有的文件已被下载，未下载的再次下载（只进行了一次校正，测试中已经足够）并且将校正的文件名输出到对应的txt文件
  4. 如果已经校正完全，将每个直播视频（多个ts文件）合并成单个文件，并输出到指定文件夹中
 
 
 
 