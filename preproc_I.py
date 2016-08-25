import nipype.interfaces.ants as ants
from nipype.interfaces.ants import N4BiasFieldCorrection
import nipype.interfaces.fsl as fsl
import nipype.pipeline.engine as pe  
from nipype.interfaces.freesurfer import MRIConvert
from nipype.interfaces.ants import antsBrainExtraction
import os

FreeSubjectDir='/Applications/freesurfer/subjects/'
subject='107_1' #In format: SUBJECTCODE_PROJECTCODE

#Testcase MRI image is T1MPRAGE 0.6mm isotropic and similar PD GRE that are aligned and 
#T1 divided by GRE which was beforehand thresholded to only contain >3000 intensity voxels. Result multiplied by 1000
#Commands:
# fslmaths 109_PDGRE06.nii -thr 3000 109_PDGRE06_thr
# fslmaths 109_T1MPRAGE06.nii -div 109_PDGRE06_thr.nii.gz 109_T1divPD_imp
# fslmaths 109_T1divPD_imp.nii.gz -mul 34000 109_T1divPD_imp.nii.gz
# Voxels over 30000 in intensity are set to 30000
# Matlabscript in /Users/ling-men/Documents/MATLAB/setMaxVoxelIntensity.m

#Create all files necessary for talairach transformation
#After -motioncor step in FreeSurfer
os.chdir(FreeSubjectDir+subject+'/mri')
mc = MRIConvert()
mc.inputs.in_file = 'orig.mgz'
mc.inputs.out_file = 'orig.nii'
mc.run()

n4 = N4BiasFieldCorrection()
n4.inputs.dimension = 3
n4.inputs.input_image = 'orig.nii'
n4.inputs.shrink_factor = 2
n4.run()

mc.inputs.in_file = 'orig.nii'
mc.inputs.out_file = 'orig_nu.mgz'
mc.run()

#Corresponding to rest of Talairach moment in -autorecon1. Might need sudo to work. 
os.system("talairach_avi --i orig_nu.mgz --xfm transforms/talairach.auto.xfm")
os.system("cp transforms/talairach.auto.xfm transforms/talairach.xfm")
os.system("talairach_afd -T 0.005 -xfm transforms/talairach.xfm")
os.system("awk -f $FREESURFER_HOME/bin/extract_talairach_avi_QA.awk transforms/talairach_avi.log")
os.system("cp orig_nu.mgz nu.mgz")

#Run normalization step
mc.inputs.in_file = 'T1.mgz'
mc.inputs.out_file = 'T1.nii'
mc.run()

brainEx = antsBrainExtraction()
brainEx.inputs.anatomical_image = 'T1.nii'
brainEx.inputs.brain_probability_mask = 'T_template0ProbabilityMask.nii.gz'
brainEx.inputs.brain_template = 'T_template0.nii.gz' #NEEDS PROPER DIRECTIONS
brainEx.run()

