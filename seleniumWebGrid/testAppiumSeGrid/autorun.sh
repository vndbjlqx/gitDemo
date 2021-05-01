for i in `adb devices |grep 'device$' |awk '{print $1}'`
do
  echo $i
  udid=$i pytest /path for you test_case.py &
done