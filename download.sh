#!/usr/bin/env bash

root_dir=${PWD}

mkdir -p data/Dataset
cd data/Dataset

# # Abort on error
# set -e

# for p in {a..i}
# do
#   # Ensure files are continued in case the script gets interrupted halfway through
#   wget --continue https://github.com/facebookresearch/Replica-Dataset/releases/download/v1.0/replica_v1_0.tar.gz.parta$p
# done

# # Create the destination directory if it doesn't exist yet
# mkdir -p $1


# download all files...
# loop trough sets and extract

# tmp let's do a test with tmp / replace with set name (works)
# cd Tmp
# cat male_008_a_a.tar.gz.part?? | unpigz -p 32  | tar -xvC ./
# rm -rf male_008_a_a.tar.gz*