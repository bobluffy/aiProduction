#!/bin/bash
rm -rf release release.tgz build
mkdir -pv release
#cp demo.py config.py release/
python setup.py build_ext
mv build/lib.linux-x86_64-3.7/app release/
cp -rf deploy/Dockerfile release/
#cp -rf app/inner_confs/data release/app/inner_confs/
#cp -rf app/inner_confs/hdfs release/app/inner_confs/
#cp -rf confs models deploy/* test release/
time=$(date "+%Y%m%d-%H%M%S")
tar zcvf release_$time.tgz release
du -hs release*