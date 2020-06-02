#!/usr/bin/env bash

env=$1
bucket=blog-test-cn
if [[ $env == 'prod' ]]
then
  bucket=blog-cn
fi
echo "部署 ${bucket}"
files="""
hexo/public/
"""

pytext="import os;names = os.listdir('hexo/public'); print(names)"

files=`python -c "import os;names = os.listdir('hexo/public'); names =['hexo/public/' + o + '/' if os.path.isdir('hexo/public/' + o) else 'hexo/public/' +o for o in names]; print(str(names))"`
# files=`python -c ${pytext}`
# echo $files


# for f in  $files
# do
  # echo $f
  # if [[ $f == */ ]]
  # then
    # ossutilmac64 cp $f oss://${bucket}/$f -rfu
  # else
    # ossutilmac64 cp $f oss://${bucket}/$f -fu
  # fi

# done

ossutil cp hexo/public oss://${bucket}/ -rfu --jobs 100
