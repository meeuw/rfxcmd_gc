#!/usr/bin/env python
from twisted.internet import protocol
from twisted.internet import reactor
from twisted.internet import task
from twisted.internet.serialport import SerialPort

from twisted.python import log

import sys
import os
import re
import subprocess
import time

from txrfxcom.txrfxcom import RFXCOM


class RFXCOMEmu(RFXCOM):
    def sendall(self):
        self.transport.write(
            self.generate(
                type='FS20',
                eSubtype='FHT8V valve',
                cSeqnbr=0,
                dummy1=1,
                dummy2=2,
                dummy3=3,
                dummy4=4,
                dummy5=5,
                dummy6=6,
            )
        )
        self.transport.write(
            self.generate(
                type='RFXMeter',
                eSubtype='New interval time set',
                cSeqnbr=0,
                dummy1=1,
                dummy2=2,
                sensorId1=3,
                sensorId2=4,
                sensorPower1=5,
                sensorPower2=6,
                sensorPower3=7,
            )
        )
        self.transport.write(
            self.generate(
                type='RFXSensor',
                eSubtype='RFXSensor message',
                cSeqnbr=0,
                temperature1=1,
                temperature2=2,
                signal=0x81,
                dummy1=4,
            )
        )
        self.transport.write(
            self.generate(
                type='WaterUsageSensor',
                eSubtype='Water usage sensor',
                cSeqnbr=0,
            )
        )
        self.transport.write(
            self.generate(
                type='GasUsageSensor',
                eSubtype='Gas usage sensor',
                cSeqnbr=0,
            )
        )
        self.transport.write(
            self.generate(
                type='PowerSensors',
                eSubtype='Revolt',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                voltage=3,
                current1=4,
                current2=5,
                power1=6,
                power2=7,
                cEnergy1=8,
                cEnergy2=9,
                powerfactor=10,
                cFreq=11,
                signal=12,
                dummy1=1,
            )
        )
        self.transport.write(
            self.generate(
                type='CurrentSensor',
                eSubtype='CM180i',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                count=3,
                channel1a=4,
                channel1b=5,
                channel2a=6,
                channel2b=7,
                channel3a=8,
                channel3b=9,
                total1=10,
                total2=11,
                total3=12,
                total4=13,
                total5=14,
                total6=15,
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='EnergySensor',
                eSubtype='CM180',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                count=3,
                instant1=4,
                instant2=5,
                instant3=6,
                instant4=7,
                usage1=8,
                usage2=9,
                usage3=10,
                usage4=11,
                usage5=12,
                usage6=13,
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='CurrentSensor',
                eSubtype='CM180i',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                count=3,
                channel1a=4,
                channel1b=5,
                channel2a=6,
                channel2b=7,
                channel3a=8,
                channel3b=9,
                total1=10,
                total2=11,
                total3=12,
                total4=13,
                total5=14,
                total6=15,
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='DateTimeSensor',
                eSubtype='RTGR328N',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                dateYY=16,
                dateMM=6,
                dateDD=11,
                dateDow=3,
                timeHR=10,
                timeMin=15,
                timeSec=30,
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='UVSensor',
                eSubtype='TFA',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                uv=3,
                dummy1=4,
                temperature=5,
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='WindSensors',
                eSubtype='TFA',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                direction1=3,
                direction2=4,
                avSpeed1=5,
                avSpeed2=6,
                gust1=7,
                gust2=8,
                temperature1=9,
                temperature2=10,
                windChill1=11,
                windChill2=12,
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='RainSensors',
                eSubtype='TFA',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                rainRateHigh=4,
                rainRateLow=5,
                rainTotal1=6,
                rainTotal2=7,
                rainTotal3=8,
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='TemperatureHumidityAndBarometricSensors',
                eSubtype='BTHR918',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                temperature1=60,
                temperature2=70,
                humidity=80,
                eHumstatus="Comfort",
                barometricHigh=70,
                barometricLow=10,
                eForecast="Cloudy",
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='TemperatureAndHumiditySensors',
                eSubtype='WTGR800',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                temperature1=60,
                temperature2=70,
                humidity=80,
                eHumstatus="Normal",
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='HumiditySensors',
                eSubtype='LaCrosse WS2300',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                humidity=50,
                eHumstatus="Normal",
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='HumiditySensors',
                eSubtype='LaCrosse WS2300',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                humidity=50,
                eHumstatus="Normal",
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='TemperatureSensors',
                eSubtype='RTHN318',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                temperature1=50,
                temperature2=60,
                signalbattery=100
            )
        )
        self.transport.write(
            self.generate(
                type='Thermostat3',
                eSubtype='Mertik G6R-H4TB / G6-H4T / G6R-H4T21-Z22',
                cSeqnbr=0,
                unitcode1=1,
                unitcode2=2,
                unitcode3=3,
                eCmnd="On",
                signal=4
            )
        )
        self.transport.write(
            self.generate(
                type='Thermostat2',
                eSubtype='RTS10, RFS10, TLX1206',
                cSeqnbr=0,
                dummy1=1,
                dummy2=2,
                dummy3=3,
                dummy4=4,
            )
        )
        self.transport.write(
            self.generate(
                type='Thermostat1',
                eSubtype='Digimax',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                temperature=50,
                temperature_set=60,
                eStatus="Cooling, No status available",
                signal=50
            )
        )
        self.transport.write(
            self.generate(
                type='RemoteControlAndIR',
                eSubtype='ATI Remote Wonder',
                cSeqnbr=0,
                dummy4=4,
                eCmnd="Power",
                toggle=3
            )
        )
        self.transport.write(
            self.generate(
                type='Camera1',
                eSubtype='X10 Ninja',
                cSeqnbr=0,
                dummy1=1,
                dummy2=2,
                dummy3=3,
            )
        )
        self.transport.write(
            self.generate(
                type='Security1',
                eSubtype='Meiantech',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                sensorId3=3,
                eStatus="Motion",
                signalbattery=11,
            )
        )
        self.transport.write(
            self.generate(
                type='RTS',
                eSubtype='RTS ext (not yet fully implemented)',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                unitcode=2,
                eCmnd="Program",
                signal=5,
                dummy1=1,
                dummy2=2,
                dummy3=3,
                dummy4=4,
            )
        )
        self.transport.write(
            self.generate(
                type='Blinds1',
                eSubtype='BlindsT4 / Raex YR1326',
                cSeqnbr=0,
                dummy1=1,
                dummy2=2,
                dummy3=3,
                dummy4=4,
                dummy5=5,
                dummy6=6,
            )
        )
        self.transport.write(
            self.generate(
                type='Curtain1',
                eSubtype='Harrison Curtain',
                cSeqnbr=0,
                dummy1=1,
                dummy2=2,
                dummy3=3,
                dummy4=4,
            )
        )
        self.transport.write(
            self.generate(
                type='Fan',
                eSubtype='Siemens SF01 - LF959RA50/LF259RB50/LF959RB50',
                cSeqnbr=0,
                dummy1=1,
                dummy2=2,
                dummy3=3,
                dummy4=4,
            )
        )
        self.transport.write(
            self.generate(
                type='Chime',
                eSubtype='RFU',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                eSound="Solo",
                signal=4
            )
        )
        self.transport.write(
            self.generate(
                type='Lighting6',
                eSubtype='Blyss',
                cSeqnbr=0,
                sensor1=1,
                sensor2=2,
                eGroupcode="C",
                eCmnd="group On",
                unitcode=3,
                commandSeqnbr=2,
                seqNbr2=4,
                signal=11
            )
        )
        self.transport.write(
            self.generate(
                type='Lighting5',
                eSubtype='Livolo',
                cSeqnbr=0,
                sensorId1=1,
                sensorId2=2,
                sensorId3=3,
                unitcode=4,
                eCmnd="Group Off",
                level=0,
                signal=10,
            )
        )
        self.transport.write(
            self.generate(
                type='Lighting4',
                eSubtype='PT2262',
                cSeqnbr=0,
                code1=1,
                code2=2,
                code3=3,
                pulse=5,
                pulse1=6,
                signal=7
            )
        )
        self.transport.write(
            self.generate(
                type='Lighting3',
                eSubtype='Ikea Koppla',
                cSeqnbr=0,
                system=0x13,
                fChannel1=1,
                fChannel2=1,
                fChannel3=1,
                fChannel4=0,
                fChannel5=1,
                fChannel6=0,
                fChannel7=1,
                fChannel8=0,
                fChannel9=0,
                fChannel10=0,
                fChannel11=1,
                fChannel12=0,
                fChannel13=1,
                fChannel14=0,
                fChannel15=0,
                fChannel16=0,
                eCmnd="On",
                batterysignal=1,
            )
        )
        self.transport.write(
            self.generate(
                type='Lighting2',
                eSubtype='AC',
                cSeqnbr=0,
                sensorId1=0,
                sensorId2=0,
                sensorId3=0,
                sensorId4=0,
                eCmnd="On",
                dimLevel=0,
                unitcode=0,
                signal=0,
            )
        )
        self.transport.write(
            self.generate(
                type='Lighting1',
                eSubtype='X10 Lighting',
                cSeqnbr=0,
                cCmnd=0,
                eHousecode="A",
                unitcode=0,
                command=0,
                signallevel=0,
            )
        )
        self.transport.write(
            self.generate(
                type='ReceiverTransmitterMessage',
                eSubtype='Error, receiver did not lock',
                cSeqnbr=0,
                cCmnd=0,
            )
        )
        self.transport.write(
            self.generate(
                type='UndecodedMessage',
                eSubtype='ARC',
                cSeqnbr=0,
                cCmnd=0,
            )
        )
        self.transport.write(
            self.generate(
                type='InterfaceMessage',
                eSubtype='InterfaceResponse',
                cSeqnbr=0,
                cCmnd=0,
                eTranceivertype="310MHz",
                cFirmwareVersion=0,
                fUndecoded=1,
                fRFU=0,
                fByronSX=0,
                fRSL=0,
                fLighting4=0,
                fFineOffsetViking=0,
                fRubicson=0,
                fAEBlyss=0,
                fMertik=0,
                fADLightwaveRF=0,
                fHidekiUPM=0,
                fLaCrosse=0,
                fFS20=0,
                fProGuard=1,
                fBlindsT0=0,
                fBlindsT1T2T3T4=0,
                fX10=0,
                fARC=0,
                fAC=0,
                fHomeEasyEU=0,
                fMeiantech=0,
                fOregonScientific=0,
                fATI=0,
                fVisonic=0,
                cMsg1=0,
                cMsg2=0,
                cMsg3=0,
                cMsg4=0,
            )
        )
        self.transport.write(
            self.generate(
                type='InterfaceControl',
                eSubtype='Interface Control',
                cSeqnbr=0,
                eCmnd="quit",
                dummy2=0,
                dummy3=0,
                dummy4=0,
                dummy5=0,
                dummy6=0,
                dummy7=0,
                dummy8=0,
                dummy9=0,
                dummy10=0
            )
        )


    def parseInterfaceControl(self, eSubtype, cSeqnbr, eCmnd, dummy2, dummy3, dummy4, dummy5, dummy6, dummy7, dummy8, dummy9, dummy10):
        if (eCmnd == 'status'):
            self.sendall()

    def parseInterfaceMessage(self, cSeqnbr, cCmnd, eSubtype, eTranceivertype, cFirmwareVersion, fAEBlyss, fRubicson, fFineOffsetViking, fLighting4, fRSL, fByronSX, fRFU, fUndecoded, fMertik, fADLightwaveRF, fHidekiUPM, fLaCrosse, fFS20, fProGuard, fBlindsT0, fBlindsT1T2T3T4, fX10, fARC, fAC, fHomeEasyEU, fMeiantech, fOregonScientific, fATI, fVisonic, cMsg1, cMsg2, cMsg3, cMsg4):
        reactor.stop()


def main():
    p = subprocess.Popen(['socat', '-d', '-d', 'pty,raw,echo=0', 'pty,raw,echo=0'], stderr=subprocess.PIPE)
    buf = b''
    while b'starting data transfer loop' not in buf:
        buf += p.stderr.read(1)
    ttys = []
    for line in buf.splitlines():
        m = re.match(r'.*PTY is (.*)', line)
        if m:
            ttys.append(m.group(1))
    print(ttys)

    logFile = sys.stdout
    log.startLogging(logFile)

    p = subprocess.Popen(['coverage', 'run', 'rfxcmd.py', '-l', '-d', ttys[0], '-o', 'config-test.xml', '-D', '-v'])
    ser = SerialPort(RFXCOMEmu(), ttys[1], reactor)

    reactor.run()
    p.wait()

if __name__ == "__main__":
    main()
