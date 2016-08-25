import nipype.interfaces.ants as ants
import nipype.interfaces.fsl as fsl
import nipype.pipeline.engine as pe  

#Testcase MRI image is T1MPRAGE 0.6mm isotropic and similar PD GRE that are aligned and 
#T1 divided by GRE which was beforehand thresholded to only contain >3000 intensity voxels. Result multiplied by 1000
#Commands:
# fslmaths 109_PDGRE06.nii -thr 3000 109_PDGRE06_thr
# fslmaths 109_T1MPRAGE06.nii -div 109_PDGRE06_thr.nii.gz 109_T1divPD_imp
# fslmaths 109_T1divPD_imp.nii.gz -mul 34000 109_T1divPD_imp.nii.gz
# Voxels over 30000 in intensity are set to 30000
# Matlabscript in /Users/ling-men/Documents/MATLAB/setMaxVoxelIntensity.m

#Create all files necessary for talairach transformation
