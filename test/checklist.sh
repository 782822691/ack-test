#!/bin/bash
#机器root账户密码
PASSWD='Alibaba%1688%'
#并发进程数
NUM=5
function checkswap() {
  echo -e "$1 swap详情:\n$(sshpass -p $PASSWD ssh $1 "free -g | sed -n '3p'")"
}

function checkumask() {
    sshpass -p $PASSWD ssh $1 "umask" >> checklist.log 2>&1
    UMASK=`sshpass -p $PASSWD ssh $1 "umask"`
    if [ $UMASK -ne "0022" ]
    then
      echo "$1 umask fail"
      else
        echo -e "$1的umask为:$UMASK"
    fi
}

function checkenforce() {
  sshpass -p $PASSWD ssh $1 "getenforce|grep Enable" >> checklist.log 2>&1
  if [ $? -eq 0 ]; then
      echo "$1 not stop selinux"
      else
        sshpass -p $PASSWD ssh $1 "getenforce"
  fi
  sshpass -p $PASSWD ssh $1 "systemctl disable gdm && systemctl stop gdm" >> checklist.log 2>&1
}

function checkOS() {
  echo -e "$1 的内核详情:\n$(sshpass -p $PASSWD ssh $1 "uname -r")"
  echo -e "$1 的架构为:\n$(sshpass -p $PASSWD ssh $1 "arch")"
  sshpass -p $PASSWD ssh $1 "lsmod | grep -w br_netfilter" >> checklist.log 2>&1
  if [ $? -eq 0 ]; then
      sshpass -p $PASSWD ssh $1 "lsmode | egrep -w \"ip_conntrack|nf_conntrack\"" >> checklist.log 2>&1
      if [ $? -ne 0 ]; then
          echo "$1的内核模块未加载"
      fi
      else
        echo "$1的内核模块未加载"
  fi
}

function checkFirewalld() {
    sshpass -p $PASSWD ssh $1 "systemctl status firewalld" >> checklist.log 2>&1
    if [ $? -eq 0 ]; then
        echo "$1 firewalld not disabled"
        else
          echo "$1的防火墙已关闭"
    fi
    sshpass -p $PASSWD ssh $1 "systemctl stop firewalld && systemctl disable firewalld"
}

function checkSSH() {
    sshpass -p $PASSWD ssh $1 "systemctl list-unit-files | grep sshd | grep sshd.service | grep enabled" >> checklist.log 2>&1
    if [ $? -eq 0 ]; then
        sshpass -p $PASSWD ssh $1 "systemctl list-unit-files | grep sshd | grep sshd.socket | grep disable" >> checklist.log 2>&1
        if [ $? -ne 0 ]; then
        echo "$1 ssh not stop sshd.socket"
        else
          echo "$1 ssh启动方式检查无异常"
        fi
    else
        echo "$1 ssh not start with ssh.service"
    fi

}

function checkNET() {
    NET=`sshpass -p $PASSWD ssh $1 "cat /proc/net/dev | sed '1,2d' | grep -w -v lo " | awk 'BEGIN {max=0;net=$1} {if ($2>max) {max=$2;net=$1}} END{print net}'`
    HOST=`sshpass -p $PASSWD ssh $1 "hostname -i"`
    echo "$1网卡为$NET hostname -i显示为$HOST"
    echo "$1 $NET $HOST" >> /tmp/netdivce.txt
}

function checkDNS() {
    DNS=`sshpass -p $PASSWD ssh $1 "cat /etc/resolv.conf " | awk '/([0-9]+\.){3}[0-9]+$/{print $NF}'`| xargs
    echo "$DNS" >> /tmp/checkDNS.txt
    echo "$1的dns服务器地址为$DNS"
}


trap "exec 6>&- ; exec 6<&- ;rm -rf /tmp/netdivce.txt;rm -rf /tmp/checkDNS.txt;exit 0" 2
mkfifo /tmp/tmpfifo
exec 6<>/tmp/tmpfifo
rm -rf /tmp/tmpfifo

for i in `seq 1 $NUM`;
do
  echo " " >&6
done

case $1 in
-a|auto)
  echo "==========开始检查swap分区=========="
  for i in `cat iplist.txt`;
  do
    {   read -u6
        checkswap $i
        echo " " >&6
    }&
  done
  wait
  echo "==========检查swap分区结束=========="
  echo "==========开始检查umask=========="
  for i in `cat iplist.txt`;
  do
    {
      read -u6
      checkumask $i
      echo " " >&6
    }&
  done
  wait
  echo "==========检查umask结束=========="
  echo "==========开始检查selinux=========="
  for i in `cat iplist.txt`;
  do
    {
      read -u6
      checkenforce $i
      echo " " >&6
    }&
  done
  wait
  echo "==========检查selinux结束=========="
  echo "==========开始检查内核=========="
  for i in `cat iplist.txt`;
  do
      {
      read -u6
      checkOS $i
      echo " " >&6
    }&
  done
  wait
  echo "==========检查内核结束=========="
  echo "==========开始检查防火墙=========="
  for i in `cat iplist.txt`;
  do
    {
      read -u6
      checkFirewalld $i
      echo " " >&6
    }&
  done
  wait
  echo "==========检查防火墙结束=========="
  echo "==========开始检查ssh配置=========="
  for i in `cat iplist.txt`;
  do
    {
      read -u6
      checkSSH $i
      echo " " >&6
    }&
  done
  wait
  echo "==========检查ssh配置结束=========="
  echo "==========开始检查网卡和hostname是否一致=========="
  for i in `cat iplist.txt`;
  do
      {
      read -u6
      checkNET $i
      echo " " >&6
      }&
  done
  wait
  awk -vnet="$(cat /tmp/netdivce.txt|awk '{print $2}' | head -n1)" '{if($2 != net) {print $1,":网卡异常"}}' /tmp/netdivce.txt
  awk '{if(NF!=3) {print $1":hostname异常"}}' /tmp/netdivce.txt
  rm -rf /tmp/netdivce.txt
  echo "==========检查网卡和hostname是否一致结束=========="
  echo "==========开始DNS检查=========="
  for i in `cat iplist.txt`;
  do
      {
      read -u6
      checkDNS $i
      echo " " >&6
      }&
  done
  wait
  LEN=`cat /tmp/checkDNS.txt | sort -n | uniq | wc -l`
  if [ $LEN -ne 1 ]; then
      echo "DNS异常"
  fi
  rm -rf /tmp/checkDNS.txt
  echo "==========DNS检查结束=========="
  exec 6>&-
  exec 6<&-
  ;;

-m|myself)
  while [ true ]; do
    read -p "输入你想执行的命令：" CMD
  for i in `cat iplist.txt`;
  do
    read -u6
    {
      echo -e "$i\n$(sshpass -p $PASSWD ssh $i "$CMD")"
      echo " " >&6
    }&
  done
  wait
done
exec 6<&-
exec 6>&-
;;
*)
   echo -e "-a 自动执行检查\n-m 自助命令执行"
   exec 6<&-
   exec 6>&-
;;
esac