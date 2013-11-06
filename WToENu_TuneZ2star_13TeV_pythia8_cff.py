import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *


generator = cms.EDFilter("Pythia8GeneratorFilter",
    crossSection = cms.untracked.double(19551.),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        processParameters = cms.vstring(
	   'Main:timesAllowErrors = 10000',
           'ParticleDecays:limitTau0 = on',
           'ParticleDecays:tauMax = 10',
           'Tune:ee 3',
           'Tune:pp 5',

           'WeakSingleBoson:ffbar2W = on',
           '24:onMode = off',
           '24:onIfAny = 11 12',
          ),
        parameterSets = cms.vstring('processParameters')
     )
)
