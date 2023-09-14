import datetime

class label_printing():

    def printing_logo(msg):
        # Define TSC commands as a string
        tsc_commands = '''
        SET RIBBON OFF
        SIZE 110 mm,20 mm
        GAP 2 mm,0 mm
        REFERENCE 0,0
        SPEED 5
        DENSITY 8
        SET PEEL OFF
        SET CUTTER OFF
        SET PARTIAL_CUTTER OFF
        SET TEAR ON
        DIRECTION 0,0
        SHIFT 0
        OFFSET 0 mm
        CLS
        PUTBMP 10,10, "LOGO1.bmp"
        PRINT 1,1
        '''

        # Open the printer device file for writing
        with open('/dev/usb/lp0', 'wb') as printer:
            # Send commands to printer
            printer.write(tsc_commands.encode())

    def printing(msg, dev, version, date):
         # Define TSC commands as a string
        tsc_commands = '''
        SET RIBBON OFF
        SIZE 110 mm,20 mm
        GAP 2 mm,0 mm
        REFERENCE 0,0
        SPEED 5
        DENSITY 8
        SET PEEL OFF
        SET CUTTER OFF
        SET PARTIAL_CUTTER OFF
        SET TEAR ON
        DIRECTION 0,0
        SHIFT 0
        OFFSET 0 mm
        CLS
        QRCODE 40,10,H,4,A,0,"{}"
        TEXT 225,14,"4",0,1,1,"{}"
        TEXT 225,80,"4",0,1,1,"Version:{}"
        TEXT 225,146,"4",0,1,1,"Date:{}"
        QRCODE 660,10,H,4,A,0,"{}"
        TEXT 845,14,"4",0,1,1,"{}"
        TEXT 845,80,"4",0,1,1,"Version:{}"
        TEXT 845,146,"4",0,1,1,"Date:{}" 
        PRINT 1,1
        '''.format(msg, dev, version, date, msg, dev, version, date)

        # Open the printer device file for writing
        with open('/dev/usb/lp0', 'wb') as printer:
            # Send commands to printer
            printer.write(tsc_commands.encode())

    def datamatrix():
        # Define TSC commands as a string
        tsc_commands = '''
            SET RIBBON OFF
            SIZE 110 mm,20 mm
            GAP 2 mm,0 mm
            REFERENCE 0,0
            SPEED 5
            DENSITY 8
            SET PEEL OFF
            SET CUTTER OFF
            SET PARTIAL_CUTTER OFF
            SET TEAR ON
            DIRECTION 0,0
            SHIFT 0
            OFFSET 0 mm
            CLS
            DMATRIX 40,10,20,20,10,10,"ALLCAN-4/00002318/2023-09-13/00004843.00002318.00000000.003d0039"
            PRINT 1,1
            '''

        # Open the printer device file for writing
        with open('/dev/usb/lp0', 'wb') as printer:
            # Send commands to printer
            printer.write(tsc_commands.encode())

if __name__ == "__main__":
    # msg = f"ALLCAN-4/00002318/2023-09-13/00004843.00002318.00000000.003d0039"
    # # msg = f"ALLCAN-4"
    # dev = f"ALLCAN-4"
    # version = f"003d0039" 
    
    # label_printing.printing(msg, dev, version, datetime.date.today())

    label_printing.datamatrix()