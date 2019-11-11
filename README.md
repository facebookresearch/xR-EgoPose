# *x*R-EgoPose

The *x*R-EgoPose Dataset has been introduced in the paper ["*x*R-EgoPose: Egocentric 3D Human Pose from an HMD Camera"](http://openaccess.thecvf.com/content_ICCV_2019/papers/Tome_xR-EgoPose_Egocentric_3D_Human_Pose_From_an_HMD_Camera_ICCV_2019_paper.pdf) (ICCV 2019, oral). It is a dataset of ~380 thousand photo-realistic *egocentric*  camera images in a variety of indoor and  outdoor spaces.

![img](doc/teaser.png)


The code contained in this repository is a PyTorch implementation of the data loader with additional evaluation functions for comparison.

## Citing *x*R-EgoPose

```
@inproceedings{tome2019xr,
  title={xR-EgoPose: Egocentric 3D Human Pose from an HMD Camera},
  author={Tome, Denis and Peluse, Patrick and Agapito, Lourdes and Badino, Hernan},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  pages={7728--7738},
  year={2019}
}
```

The license agreement for the data usage implies citation of the paper. Please notice that citing the dataset URL instead of the publication would not be compliant with this license agreement.

## Download on Mac OS and Linux

Make sure pigz and wget are installed:
```
# on Mac OS
brew install wget pigz
# on Ubuntu
sudo apt-get install pigz
```

To download and decompress the dataset use the download.sh script:
```
./download.sh
```

which will dowload and set-up the dataset folder for training and testing the model.
Make sure to have **~1TB free space** for storing the data.
After that, run ```demo.py```. This shows how to load and evaluate the model.

## *x*R-EgoPose Dataset

Character names in the dataset follow the convention **gender**\_**id**\_**body-type**\_**height**

- *gender*: male/female
- *id*: integer
- *body-type*: a/f (average/full)
- *height*: a/s (average/short)

|Train-set| Test-set | Val-set |
|---------|----------|---------|
|female_001_a_a |female_004_a_a | male_008_a_a |
|female_002_a_a |female_008_a_a | |
|female_002_f_s |female_010_a_a | |
|female_003_a_a |female_012_a_a | |
|female_005_a_a |female_012_f_s | |
|female_006_a_a |male_001_a_a | |
|female_007_a_a |male_002_a_a | |
|female_009_a_a |male_004_f_s | |
|female_011_a_a |male_006_a_a | |
|female_014_a_a |male_007_f_s | |
|female_015_a_a |male_010_a_a | |
|male_003_f_s |male_014_f_s | |
|male_004_a_a | | |
|male_005_a_a | | |
|male_006_f_s | | |
|male_007_a_a | | |
|male_008_f_s | | |
|male_009_a_a | | |
|male_010_f_s | | |
|male_011_f_s | | |
|male_014_a_a | | |

### Structure

For each set and for each character the structure is identical, and structured as follows

```
TrainSet
├── female_001_a_a
│   ├── env 01
│   │   └── cam_down
│   │   	├── depth
│   │   	├── json
│   │   	├── objectId
│   │   	├── rgba
│   │   	├── rot
│   │   	└── worldp
│   ├── ...
│   └── env 03
└── ...
```

Frame information is organized in different folders, each containing one file per frame

- depth: 8-bit png per frame
- json: json file with camera and pose information 
- objectId: semantic segmentation
- rgba: 8-bit png per frame
- rot: json file with joint rotations
- worldp: world position per pixel

### Actions

A set of nine broad action categories have been included in the dataset

| Action Name |
|-------------|
| Gaming |
| Gesticulating |
| Greeting |
| Lower Stretching |
| Patting |
| Reacting |
| Talking |
| Upper Stretching |
| Walking |

where each of those categories is the collection of many different and specific actions.

E.g. *Gaming* includes Boxing, Shooting Gun, Playing Golf, Playing Baseball just to cite a few.

## Results

| Action | Martinez [1] | Ours - single branch |  Ours - dual branch |
|--------|--------------|---------------|---------------------|
| Gaming | 109.6 | 138.3 | 56.0 |
| Gesticulating | 105.4 | 108.5 | 50.2 |
| Greeting | 119.3 | 100.3 | 44.6 |
| Lower Stretching | 125.8 | 133.3 | 51.1 |
| Patting | 93.0 | 117.8 | 59.4 |
| Reacting | 119.7 | 175.6 | 60.8 |
| Talking | 111.1 | 93.5 | 43.9 |
| Upper Stretching | 124.5 | 129.0 | 53.9 |
| Walking |  130.5 | 131.9 | 57.7 |
| **All (mm)** | 122.1 | 130.4 | **58.2** |

## License

See the LICENSE file for details.