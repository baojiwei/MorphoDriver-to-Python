################################################################################
##  Project        :    OmniDriver
##  File           :    omnidll.py
##  Description    :    dll for spectrum
##  Created by     :    baojiwei@baojiwei.com
##  Created date   :    11/08/2014
################################################################################
##  Reversion history
##  V0.1   11/08/2014   Baojiwei / Initial version
################################################################################

import clr
clr.AddReference('NETOmniDriver')
from OmniDriver import CCoWrapper
from OmniDriver import CCoBoardTemperature
from OmniDriver import CCoCoefficients
       
class omnidll():
    def __init__(self):
        self.obj=CCoWrapper()
        self.tbj=CCoBoardTemperature()
        self.cbj=CCoCoefficients()
    def OpenAllSpectrometers(self):
        return  self.obj.openAllSpectrometers()
    def GetSpectrometerName(self,spectrometerIndex):
        return self.obj.getName(spectrometerIndex)
    def GetNonLinearityCorrectionCoefficient(self,spectrometerIndex):
        self.cbj=self.obj.getCalibrationCoefficientsFromEEProm(spectrometerIndex)
        return self.cbj.getNlCoefficients()
    def GetDetectorSerialNumber(self,spectrometerIndex):
        return self.obj.getSerialNumber(spectrometerIndex)
    def GetTemperature(self,spectrometerIndex):
        self.tbj=self.obj.getFeatureControllerBoardTemperature(spectrometerIndex)
        return self.tbj.getBoardTemperatureCelsius()        
    def SetWindowsOfBox(self,spectrometerIndex,windowsOfBox):
        self.obj.setBoxcarWidth(spectrometerIndex,windowsOfBox)
    def SetIntegrationTime(self,spectrometerIndex,IntegrationTime):
        self.obj.setIntegrationTime(spectrometerIndex,IntegrationTime)
    def SetAverage(self,spectrometerIndex,AverageTimes):
        self.obj.setScansToAverage(spectrometerIndex,AverageTimes)
    def GetWavelength(self,spectrometerIndex):
        return self.obj.getWavelengths(spectrometerIndex)
    def GetSpectrum(self,spectrometerIndex):
        return self.obj.getSpectrum(spectrometerIndex)
