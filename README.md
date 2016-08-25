Code for analyzing sub-millimeter resolved subjects in FreeSurfer. Preprocessing steps performed outside FreeSurfer for not being subject to adverse image manipulations because of rogue voxels in the scalp due to the T1 divided by PD images, which is assumed to exist prior to running these scripts. 

All scripts in nipype.

HOW TO USE:
1. Fix T1divPD-image volume according to instructions in preproc_I.py
2. Run mkallDirsFreeSurfer.sh as super user and include name of image volume file to be used as base for freesurfer analyses and directory path to that file as argument 1 and 2, respectively.
3. 