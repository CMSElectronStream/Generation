Generation
==========

Generation of signal

W>enu

Working here:

    /home/amassiro/ECAL/HLT/CMSSW_6_2_3/src/Generation

Prepare:

    git-cms-addpkg Configuration/Generator

run:

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


    cp Generation/WToENu_TuneZ2star_13TeV_pythia8_cff.py Configuration/Generator/python/
    scramv1 b -j 8

    cmsDriver.py Configuration/Generator/python/WToENu_TuneZ2star_13TeV_pythia8_cff.py \
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


and run

    cmsRun WToENu_TuneZ2star_13TeV_pythia6_cff_py_GEN_SIM.py
    cmsRun WToENu_TuneZ2star_13TeV_pythia8_cff_py_GEN_SIM.py

and test:

    cmsRun  ~/public/CMSSW/DrawTree.py inputFiles=file:WToENu_TuneZ2star_13TeV_pythia8_cff_py_GEN_SIM.root
    cmsRun  ~/public/CMSSW/DrawTree.py inputFiles=file:WToENu_TuneZ2star_13TeV_pythia6_cff_py_GEN_SIM.root
