#!/bin/bash
#This script will create the necessary directories in $SUBJECTS_DIR
#Takes T1divPD-file and its parent directory as input and creates necessary directories. 
#Assumes SUBJECTCODE_PROJECTCODE_KINDOFFILE.EXTENSIONS structure in filename. SUBJECTCODE_PROJECTCODE will become freesurfer subject.
#Must be run as super user.

INFILE=$1
DATADIR=$2
if [ -e ${DATADIR}/${INFILE} ]
then 
	echo "File found."
else
	echo "File not found. Aborting script."
	exit
fi

cd /Applications/freesurfer/subjects

mkdir ${INFILE%_*}
cd ${INFILE%_*}
mkdir bem
mkdir label
mkdir mri
mkdir scripts
mkdir src
mkdir stats
mkdir surf
mkdir tmp
mkdir 'touch'
mkdir trash