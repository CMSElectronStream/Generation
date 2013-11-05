Generation
==========

Generation of signal

W>enu

git-cms-addpkg Configuration/Generator

cp Generation/WToENu_TuneZ2star_13TeV_pythia6_cff.py Configuration/Generator/python/
scramv1 b -j 8

    cmsDriver.py Configuration/Generator/python/WToENu_TuneZ2star_13TeV_pythia6_cff.py \
    --step GEN,SIM --beamspot Realistic8TeVCollision \
    --conditions START62_V1::All \
    --pileup NoPileUp \
    --datamix NODATAMIXER \
    --eventcontent RAWSIM \
    --datatier GEN-SIM \
    -n 200000 \
    --no_exec




    cmsDriver.py WE_14TeV_cfi.py \
    --step GEN,SIM --beamspot Realistic8TeVCollision \
    --conditions START62_V1::All \
    --pileup NoPileUp \
    --datamix NODATAMIXER \
    --eventcontent RAWSIM \
    --datatier GEN-SIM \
    -n 200000 \
    --no_exec



To be fixed:

    Realistic13TeVCommision


cmsRun WToENu_TuneZ2star_13TeV_pythia6_cff_py_GEN_SIM.py