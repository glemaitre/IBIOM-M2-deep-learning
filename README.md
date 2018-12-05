# IBIOM-M2: Introduction to deep-learning

### Instructors

* Guillaume Lemaitre - Inria, Paris-Saclay Center for Data Science

### Obtaining the Tutorial Material

If you have a GitHub account, it is probably most convenient if you clone or
fork the GitHub repository. You can clone the repository by running:

```bash
git clone https://github.com/glemaitre/IBIOM-M2-deep-learning
```

If you are not familiar with git or don't have an GitHub account, you can
download the repository as a `.zip` file by heading over to the GitHub
repository (https://github.com/glemaitre/IBIOM-M2-deep-learning) in your
browser and click the green “Download” button in the upper right.

Please note that we may add and improve the material until shortly before the
tutorial session, and we recommend you to update your copy of the materials one
day before the tutorials. If you have an GitHub account and cloned the
repository via GitHub, you can sync your existing local repository with:

```bash
git pull origin master
```

If you don't have a GitHub account, you may have to re-download the `.zip`
archive from GitHub.

### Requirements

To check if your system have the required libraries, you can execute the
following script:

```bash
python check_environment.py
```

If you are using `conda`, you can create a specific environment for this
tutorial with the following commands:

```bash
conda env create environment.yml
conda activate ibiom  # or source activate pyparis_sklearn
```

### References

This material is based on the fruitful work of the
[course](https://github.com/m2dsupsdlclass/lectures-labs) of O. Grisel and
C. Ollion, and more broadly to the Pythonista of the whole data science
community.
