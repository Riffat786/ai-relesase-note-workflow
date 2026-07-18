## **Sample Unformatted Release Note**

**Product:** PIC18F47Q10 Microcontroller Family  
**Version:** 2.5.1  
**Release Date:** January 15, 2024

### **What's New**

This release includes new features for the PIC18F47Q10 microcontroller family. Users can now use enhanced PWM capabilities and improved ADC performance. A new debugging interface has been added for better development experience.

### **New Features**

- Added support for 16-bit PWM with programmable dead-band control on modules PWM1 through PWM4
- Enhanced ADC with 12-bit resolution and simultaneous sampling capability
- New UART interface with hardware flow control support
- Improved I2C communication with multi-master arbitration
- Added real-time clock module with battery backup capability
- New debugging interface compatible with MPLAB X IDE version 6.0 and later

### **Improvements**

Performance optimizations have been made to reduce power consumption by 15% during sleep mode. Memory access time has been improved for faster data transfers. The compiler now generates more efficient code for interrupt handlers.

### **Known Issues**

There is a known issue with the CAN module where occasional frame loss may occur under high traffic conditions. Users should implement software retry logic as a workaround. This will be fixed in the next release.

The ADC may read incorrect values if multiple channels are switched rapidly without proper settling time. It is recommended to add a 10µs delay between channel selections.

### **Bug Fixes**

- Fixed UART baud rate calculation error for non-standard clock frequencies
- Corrected I2C acknowledge bit timing issue
- Resolved SPI mode 3 clock polarity inversion problem
- Fixed timer overflow interrupt flag clearing bug

### **Supported Tools**

- MPLAB X IDE version 6.0 and later
- XC8 Compiler version 2.45 or higher
- MPLAB Code Configurator version 5.2 and later

### **Installation Instructions**

Download the latest device pack from the Microchip website. Extract files to your MPLAB plugins directory. Restart MPLAB X IDE to load the new device definitions.

### **Documentation**

Complete datasheet available at www.microchip.com. Application note AN1234 provides detailed PWM programming examples. Technical support available through the Microchip support portal.
