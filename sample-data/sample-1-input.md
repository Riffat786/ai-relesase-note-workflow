# PIC32MX470F512L Release Notes

(This is a sample release note, that is stored as a word document in a local folder)

Product: PIC32MX470F512L Microcontroller
Version: 2.5.1
Date: March 15 2024

## Overview
The PIC32MX470F512L is a high performance 32 bit microcontroller. We have made several updates and improvements in this release. Users should review this document carefully.

## New Features in v2.5.1
- Added USB 2.0 Full Speed Device support (finally!)
- Improved SPI performance up to 50 Mbps
- New power management features reduce consumption by 30%
- Enhanced debugging capabilities with real time data tracing
- Support for CAN FD (Flexible Data Rate)
- Memory protection features added

## Bug Fixes

Fix for UART timeout issue when baud rate > 115200. SPI clock divider calculation corrected for edge cases. Fixed PWM deadtime insertion not working in certain configurations. USB device suspend mode now properly handled
ADC sampling inconsistency in differential mode resolved. I2C slave mode address recognition bug fixed

## Known Issues
- CAN module may require additional setup for high speed networks (>1Mbps)

- USB Host mode not supported in this version will be added in next release

- Certain optimization levels may cause code size issues investigate compiler settings

## Installation Instructions
1. Download the latest IDE from microchip website
2. Install the IDE to default location C:\Program Files\Microchip
3. Open the IDE
4. Go to Tools menu select Device Family Packs
5. Search for PIC32MX470F512L
6. Click Install
7. Restart the IDE
8. Create new project using the PIC32MX470F512L device
9. Start developing

## Technical Specifications
- CPU Speed: 80 MHz
- RAM: 32 KB
- Flash: 512 KB
- USB Port: 1x USB 2.0
- CAN Port: 1x
- SPI: 2x modules
- I2C: 2x modules
- UART: 2x modules
- ADC: 12 bit 500 ksps

##Support
Contact: support@microchip.com
Website: www.microchip.com
Documentation: docs.microchip.com
