#!/bin/bash
#机器root账户密码
PASSWD='Alibaba%1688%'
#并发进程数
NUM=5
function check-vg() {
    vg_count=`sshpass -p $PASSWD ssh -o StrictHostKeyChecking=no $1 "vgs | sed '1d' | wc -l"  2>/dev/null | awk '{print int($0)}'`
    if [ $vg_count -ne "1" ]
    then
      echo "$1的vg不符合要求"
      exit 1
      else
        vg=`sshpass -p $PASSWD ssh -o StrictHostKeyChecking=no $1 "vgs | sed '1d' | awk '{print $1}'"  2>/dev/null`
    fi
}
function create-lv() {
    sshpass -p $PASSWD ssh $1 "lvcreate -n docker -L 150G $vg"
    sshpass -p $PASSWD ssh $1 "lvcreate -n kubelet -L 150G $vg"
    sshpass -p $PASSWD ssh $1 "mkfs.ext4 -f /dev/mapper/${{vg}}-docker"
    sshpass -p $PASSWD ssh $1 "mkfs.ext4 -f /dev/mapper/${{vg}}-kubelet"
    sshpass -p $PASSWD ssh $1 "mkdir -pv /var/lib/docker;mkdir -pv /var/lib/kubelet"
    sshpass -p $PASSWD ssh $1 "mount  /dev/mapper/${{vg}}-docker /var/lib/docker;mount  /dev/mapper/${{vg}}-kubelet /var/lib/kubelet"
}
trap "exec 6>&- ; exec 6<&- ;rm -rf /tmp/netdivce.txt;rm -rf /tmp/checkDNS.txt;exit 0" 2
mkfifo /tmp/tmpfifo
exec 6<>/tmp/tmpfifo
rm -rf /tmp/tmpfifo

for i in `seq 1 $NUM`;
do
  echo " " >&6
done

  for i in `cat iplist.txt`;
  do
    {   read -u6
        check-vg $i
        create-lv $i
        echo " " >&6
    }&
  done
  wait