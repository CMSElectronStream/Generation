Generation
==========

Generation of signal

W>enu


cmsDriver.py WToENu_TuneZ2star_13TeV_pythia6_cff.py \
   --step GEN,SIM --beamspot Realistic13TeVCollision \
   --conditions START62_V1::All \
   --pileup NoPileUp \
   --datamix NODATAMIXER \
   --eventcontent RAWSIM \
   --datatier GEN-SIM \
   -n 200000 \
   --no_exec
