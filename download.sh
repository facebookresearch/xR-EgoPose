#!/usr/bin/env bash
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

dataset_dir=${PWD}/data/Dataset
declare -a a_test=("female_004_a_a"
				"female_008_a_a"
				"female_010_a_a"
				"female_012_a_a"
				"female_012_f_s"
				"male_001_a_a"
				"male_002_a_a"
				"male_004_f_s"
				"male_006_a_a"
				"male_007_f_s"
				"male_010_a_a"
				"male_014_f_s")
declare -a a_train=("female_001_a_a"
				"female_002_a_a"
				"female_002_f_s"
				"female_003_a_a"
				"female_005_a_a"
				"female_006_a_a"
				"female_007_a_a"
				"female_009_a_a"
				"female_011_a_a"
				"female_014_a_a"
				"female_015_a_a"
				"male_003_f_s"
				"male_004_a_a"
				"male_005_a_a"
				"male_006_f_s"
				"male_007_a_a"
				"male_008_f_s"
				"male_009_a_a"
				"male_010_f_s"
				"male_011_f_s"
				"male_014_a_a")
declare -a a_val=("male_008_a_a")

download_set () {
	arr=("$@")

	for s in "${arr[@]}"
	do

        # download all parts for character
        for p in {a..j}
        do
            url=https://github.com/facebookresearch/xR-EgoPose/releases/download/v1.0/$s.tar.gz.parta$p

            # Ensure files are continued in case the script gets interrupted halfway through
            wget --continue $url
            wgetreturn=$?
            echo $wgetreturn
            if [[ $wgetreturn -ne 0 ]]; then
                break
            fi
		done

        # extract data
        cat $s.tar.gz.part?? | unpigz -p 32  | tar -xvC ./

        # remove compressed data
        rm -rf $s.tar.gz*

	done
}

# Abort on error
set -e

# Create the destination directory if it doesn't exist yet
mkdir -p ${dataset_dir}
cd ${dataset_dir}

# Download and process Validation set
echo "Downloading and extracting Validation set"
mkdir -p ValSet
cd ValSet
download_set "${a_val[@]}"

# Download and process Train set
echo "Downloading and extracting Train set"
cd ${dataset_dir}
mkdir -p TrainSet
cd TrainSet
download_set "${a_train[@]}"

# Download and process Test set
echo "Downloading and extracting Test set"
cd ${dataset_dir}
mkdir -p TestSet
cd TestSet
download_set "${a_test[@]}"
