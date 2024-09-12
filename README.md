<h2>ImageMask-Dataset-Multiple-Sclerosis-Brain-MRI  (Updated: 2024/09/13)</h2>
<li>2024/09/13: Added Multiple-Sclerosis-Brain-MRI-Flair-ImageMask-Dataset.</li>
<br>
This is ImageMask Dataset for <a href="https://data.mendeley.com/datasets/8bctsm8jz7/1">
Brain MRI Dataset of Multiple Sclerosis with Consensus Manual Lesion Segmentation and Patient Meta Information. 
</a>
<br>
<br> 
<b>Download T2 ImageMask-Dataset</b><br>
You can download 
<a href="https://drive.google.com/file/d/1lnwZ_lQ9OUBUkEHsJBVZScmLSBk8Obsk/view?usp=sharing">
Multiple-Sclerosis-Brain-MRI-T2-ImageMask-Dataset.zip</a>
, which was derived by us from the original Multiple-Sclerosis-Brain-MRI,
<br>
<br> 
<b>Download Flair ImageMask-Dataset</b><br>
You can download <a href="https://drive.google.com/file/d/1Wf3O5At5VJjxCY995ubh_OGptqdJTuQ0/view?usp=sharing">
Multiple-Sclerosis-Brain-MRI-Flair-ImageMask-Dataset.zip</a>
, which was derived by us from the original Multiple-Sclerosis-Brain-MRI,
<br>
<br>
<h3>1. Dataset Citation</h3>
We used the following dataset to create our ImageMask dataset 
<a href="https://data.mendeley.com/datasets/8bctsm8jz7/1">
Brain MRI Dataset of Multiple Sclerosis with Consensus Manual Lesion Segmentation and Patient Meta Information 
</a>
<br>
Published: 31 March 2022|Version 1|DOI:10.17632/c
<br>

<b>Contributor:</b>Ali M Muslim
<br>
<b>Description</b><br>
Magnetic resonance imaging (MRI) provides a significant key to diagnose and monitor the progression of Multiple Sclerosis (MS) disease. Manual MS-Lesion segmentation, Expanded Disability Status Scale (EDSS) and patient’s meta information can provide a gold standard for research in terms of automated MS-lesion quantification, automated EDSS prediction and identification of the correlation between MS-lesion and patient disability. In this dataset, we provide a novel multi-sequence MRI dataset of 60 MS patients with consensus manual lesion segmentation, EDSS, general patient information and clinical information. On this dataset, three radiologists and neurologist experts segmented and validated the manual MS-lesion segmentation for three MRI sequences T1-weighted, T2-weighted and fluid-attenuated inversion recovery (FLAIR). The dataset can be used to study the relationship between MS-lesion, EDSS and patient clinical information. Furthermore, it also can be used to development of automated MS-lesion segmentation, patient disability prediction using MRI and correlation analysis between patient disability and MRI brain abnormalities include MS lesion location, size, number and type. 
<br>
<b>Licence</b> CC BY 4.0<br>
<br>


<h3>2. Download Multiple-Sclerosis-Brain-MRI Dataset</h3>
Please download the original dataset from 
<a href="https://data.mendeley.com/datasets/8bctsm8jz7/1">
Brain MRI Dataset of Multiple Sclerosis with Consensus Manual Lesion Segmentation and Patient Meta Information 
</a>
<br>
It contains the following Flair, T1, and T2 nii files for 60 patients.<br> 
<pre>
./8bctsm8jz7-1
├─Patient-1
│  ├─1-Flair.nii
│  ├─1-LesionSeg-Flair.nii
│  ├─1-LesionSeg-T1.nii
│  ├─1-LesionSeg-T2.nii
│  ├─1-T1.nii
│  └─1-T2.nii
├─Patient-2
│  ├─2-Flair.nii
│  ├─2-LesionSeg-Flair.nii
│  ├─2-LesionSeg-T1.nii
│  ├─2-LesionSeg-T2.nii
│  ├─2-T1.nii
│  └─2-T2.nii
...
└─Patient-60
   ├─60-Flair.nii
   ├─60-LesionSeg-Flair.nii
   ├─60-LesionSeg-T1.nii
   ├─60-LesionSeg-T2.nii
   ├─60-T1.nii
   └─60-T2.nii

</pre>

<h3>3. Generate T2 ImageMaskDataset </h3>

Please run the following command for Python script <a href="./ImageMaskDatasetGenerator.py">ImageMaskDatasetGenerator.py</a>.
<br>
<pre>
> python ImageMaskDatasetGenerator.py T2
</pre>
You can specify dataset type as a command line parameter: Flair, T1, and T2.<br>
<pre>
 python ImageMaskDatasetGenerator.py [Flair|T1|T2]
</pre>
This command will generate augmented 512x512 jpg image and mask datasets of T2.<br>

<pre>
./Multiple-Sclerosis-Brain-MRI-master-T2
├─images
└─masks
</pre>
The genetor script <a href="./ImageMaskDatasetGenerator.py">ImageMaskDatasetGenerator.py</a> is 
really an offline dataset augmentation tool, which supports the following image transformation operations.<br>
<pre>
hflip 
deformation
distortion
barrel_distortion
pincushion_distortion
</pre>

<br>
<h3>4. Split T2 master</h3>
Please run the following command for Python script <a href="./split_master.py">split_master.py</a>.
<br>
<pre>
> python split_master.py T2
</pre>
This command will generate test, train and valid subsets from Multiple-Sclerosis-Brain-MRI-master-T2.<br>
<pre>
./Multiple-Sclerosis-Brain-MRI-T2-ImageMask-Dataset
├─test
│  ├─images
│  └─masks
├─train
│  ├─images
│  └─masks
└─valid
    ├─images
    └─masks
</pre>

<b>train images sample</b><br>
<img src="./asset/train_images.png" width="1024" height="auto">
<br>

<b>train masks sample</b><br>
<img src="./asset/train_masks.png"  width="1024" height="auto">
<br>
<b>Dataset Statistics</b><br>

<img src="./Multiple-Sclerosis-Brain-MRI-T2-ImageMask-Dataset_Statistics.png" width="480" height="auto"><br>
<!--
 -->
 
<h3>5. Generate Flair ImageMaskDataset </h3>

Please run the following command for Python script <a href="./ImageMaskDatasetGenerator.py">ImageMaskDatasetGenerator.py</a>.
<br>
<pre>
> python ImageMaskDatasetGenerator.py Flair
</pre>
This command will generate augmented 512x512 jpg image and mask datasets of Flair.<br>

<pre>
./Multiple-Sclerosis-Brain-MRI-master-Flair
├─images
└─masks
</pre>

<br>
<h3>6. Split Flair master</h3>
Please run the following command for Python script <a href="./split_master.py">split_master.py</a>.
<br>
<pre>
> python split_master.py Flair
</pre>
This command will generate test, train and valid subsets from Multiple-Sclerosis-Brain-MRI-master-Flair.<br>
<pre>
./Multiple-Sclerosis-Brain-MRI-Flair-ImageMask-Dataset
├─test
│  ├─images
│  └─masks
├─train
│  ├─images
│  └─masks
└─valid
    ├─images
    └─masks
</pre>

<b>train images sample</b><br>
<img src="./asset/flair_train_images.png" width="1024" height="auto">
<br>

<b>train masks sample</b><br>
<img src="./asset/flair_train_masks.png"  width="1024" height="auto">
<br>
<b>Dataset Statistics</b><br>

<img src="./Multiple-Sclerosis-Brain-MRI-Flair-ImageMask-Dataset_Statistics.png" width="480" height="auto"><br>



<b>References</b><br>

<b>1. Brain MRI dataset of multiple sclerosis with consensus manual lesion segmentation and patient meta information</b><br>
Ali M. Muslim, Syamsiah Mashohor, Gheyath Al Gawwam, Rozi Mahmud, Marsyita binti Hanafi,<br>
Osama Alnuaimi, Raad Josephine, Abdullah Dhaifallah Almutairi<br>
https://doi.org/10.1016/j.dib.2022.108139<br>

<a href="https://www.sciencedirect.com/science/article/pii/S235234092200347X">https://www.sciencedirect.com/science/article/pii/S235234092200347X</a>
<br>
<br>
<b>2. Multiple Sclerosis Lesion Segmentation in Brain MRI Using Inception Modules Embedded in a Convolutional Neural Network</b><br>

Shahab U. Ansari, Kamran Javed, Saeed Mian Qaisar, Rashad Jillani, Usman Haider<br>
First published: 04 August 2021 https://doi.org/10.1155/2021/4138137<br>
<a href="https://onlinelibrary.wiley.com/doi/10.1155/2021/4138137?msockid=3ec756cfd5d167d7342f47c9d4de66ff">https://onlinelibrary.wiley.com/doi/10.1155/2021/4138137?msockid=3ec756cfd5d167d7342f47c9d4de66ff</a>


