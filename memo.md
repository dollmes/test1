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

[VsCode]  
    zenkaku  
    Trailing Spaces  
    Bracket Pair Colorizer  
    
[ARN GIC]  
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&cad=rja&uact=8&ved=2ahUKEwiJr7bwvsLpAhXEBIgKHY61DNAQFjAFegQICRAB&url=https%3A%2F%2Fdev.toppers.jp%2Ftrac_user%2Fcontrib%2Fexport%2F306%2Fasp3_wo_tecs%2Ftrunk%2Farch%2Farm_gcc%2Fdoc%2Fgic_memo.txt&usg=AOvVaw0TTZCteN1CfPwucnzzbpuC

[opencv gstreamer raspi]  
https://qiita.com/yamato225/items/0870beca1822c6dccad3  

[Dockerを使ってポータブルなArm64エミュレート環境を構築]  
https://qiita.com/muscat201807/items/468bb6608a61d6f31f1c

[【pyenv-win】pyenv のインストールと実行]  
https://qiita.com/probabilityhill/items/9a22f395a1e93206c846  

[Windowsでpyenv（pyenv-win）とvenvを使ってPythonの仮想環境を構築]  
https://qiita.com/t_koba/items/2e8f9eafbdd7644cff20  
