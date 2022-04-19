---
date-created: 2022-04-18
---

Conda
=====

# Why conda ?

1. Environment Manager 
    Every project has it's own dependencies. One project might use Tensorflow and another might use XGBoost. There is no reason why these two project should be in the same enviroment. Conda lets you create different enviroments for every project ( or every type of project )

2. Share your environments
    If you are working with a team, it is essentials that you develop on the same enviroment so as to avoid dependency issues. You would not only be tracking your python package dependencies but also python version itself. 

---
# Installation 

1. Download Installer ( for Linux )
```bash
wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
```
2. Install 
```bash
bash ./Anaconda3-2021.11-Linux-x86_64.sh
```
3. Follow the instruction prompt 
```{tip} 
Choose the installtion location depending on storage space. Conda enviroment tend to take up to few GBs per enviroment 
```
when installer prompts “Do you wish the installer to initialize Anaconda3 by running conda init?” **Choose “yes”**. This will start conda with every terminal session.
1. Restart the terminal or enter the following 
```bash
source ~/.bashrc
```
you should see "(base)" in your bash prompt

---
# Usage 

## Activate and Deactivate   

</br>

```bash
which python
``` 
> this should point to `base` environment's python. For example :  `~/anaconda3/bin/python` 

</br>

```bash
conda deactivate && which python
```
> this deactivates conda's base env and now 'python' should point to : `/usr/bin/python`

</br>

```bash
conda activate base 
```

> to activate the base env 

</br>

This applies to `pip` as well. So packages installed through pip inside the base environment will not be avaiable in the system's python ( after deactivating ). 
> try 'which pip' inside and outside the base env 

---
## Custom Environment

### Create environment with a specific python version
```bash
conda create -n custom_env python=3.8.2
```
> Note: `custom_env` is the name of the environment and `-n` is short hand for `--name` 

### Activate environment
```bash
conda activate custom_env
```
> try `which python` and `python --version` after this step 

`conda deactivate` will take you to base environment.

### Save environment to file

```bash
conda env export > custom_env_file.yml
``` 

This file can be inside your project and be tracked via git. 

### Remove environment 

```bash 
conda remove -n custom_env --all 
``` 
make sure to deactivate the environment before removing the environment

### Load environment from file 

```bash 
conda env create -f custom_env_file.yml 
```

it will create `custom_env`. The name of the environment is also stored in the file. 

> look at the file after installing some package with pip and conda


## Installing Package 

You can also use conda to install packages. These packages will be install from the default anaconda channels

```bash 
conda install pandas 
```

will install pandas similar to `pip install pandas`

> not all packages are avaiable in conda but you can use pip inside the environment and it will also be tracked as dependencies. 

# Cheatsheet

[link](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf) to conda's cheet sheet ( from conda's documentation )