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
declare -a max_test=("i" "i" "i" "f" "a" "i" "j" "a" "i" "a" "i" "a")
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
declare -a max_train=("i" "j" "a" "f" "i" "i" "h" "i" "f" "f" "j" "a" "i" "j" "a" "i" "a" "h" "a" "a" "i")
declare -a a_val=("male_008_a_a")
declare -a max_val=("i")

download_set () {

	case "$1" in

		ValSet)
			echo "ValSet"
			arr=("${a_val[@]}")
			max=("${max_val[@]}")
			;;

		TestSet)
			echo "TestSet"
			arr=("${a_test[@]}")
			max=("${max_test[@]}")
			;;

		TrainSet)
			echo "TrainSet"
			arr=("${a_train[@]}")
			max=("${max_train[@]}")
			;;

		*)
			break
			;;

	esac

	echo "Downloading and extracting" $1
	mkdir -p $1
	cd $1

	for i in "${!arr[@]}"
	do
		s=${arr[$i]}
		m=${max[$i]}
        # download all parts for character
        for p in $(eval echo {a..$m})
        do
            url=https://github.com/facebookresearch/xR-EgoPose/releases/download/v1.0/$s.tar.gz.parta$p

            # Ensure files are continued in case the script gets interrupted halfway through
            wget --continue $url
		done

        # extract data
        cat $s.tar.gz.part?? | unpigz -p 32  | tar -xvC ./

        # remove compressed data
        rm -rf $s.tar.gz*

	done

	cd ..
}

# Abort on error
set -e

# Create the destination directory if it doesn't exist yet
mkdir -p ${dataset_dir}
cd ${dataset_dir}

# Download and process Validation set
download_set "ValSet"

# Download and process Train set
download_set "TrainSet"

# # Download and process Test set
download_set "TestSet"
