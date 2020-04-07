# メモ書き

[enhanced]

 参考：https://qiita.com/b4b4r07/items/2cf90da00a4c2c7b7e60

 sudo pip install percol

 git clone https://github.com/b4b4r07/enhancd

 source enhancd/init.sh

[spacefm]

 参考：https://ameblo.jp/gokurakuhaze/entry-12212109760.html

 apt-get install spacefm udevil

[parcellite]

 参考：http://d.hatena.ne.jp/weblinuxmemo/20091012/p1

 apt-get install parcellite

[byobu]

 参考：https://qiita.com/kayama0fa/items/82d3ebab8bb297bdfd23

 sudo apt-get install byobu

[pulseaudio]

  RTPで受け
  
  　load-module module-rtp-recv
   
  RTPで送り
  
  　load-module module-null-sink sink_name=rtp format=s16be channels=2 rate=44100 sink_properties="device.description='RTP Multicast Sink'"
   
  　load-module module-rtp-send source=rtp.monitor

[python atom]

  参考：https://www.web-jozu.com/python/python-atom/  
       https://prog-8.com/languages/python  
       https://www.sejuku.net/blog/76158
       
[cygwinでssh-server]  
    apt-cyg install openssh openssl  
    ssh-host-config  
    vi /etc/sshd_config  
    cygrunsrv -S cygsshd  

[crc16 左送り]  
    https://kyouichisato.blogspot.com/2014/09/crc-16-ccitt.html?m=0  

[clang-format]  
    https://blog.takuchalle.dev/post/2018/04/26/setup_clang_format/  

[0xff]埋め  
    $ tr "\000" "\377" < /dev/zero | dd ibs=1k count=1000 of=0xffFile.bin
