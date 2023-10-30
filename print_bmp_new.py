tsc_command_begin = '''
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
        BITMAP 0,0,162,236,1,
        '''

tsc_command_end = '''
        PRINT 1,1
        '''

with open('hc_logo.bin', 'rb') as f:
    # Read the entire file into a byte array
    bmp_data = f.read()


def test():
    with open('/dev/usb/lp0', 'wb') as printer:
        # Send commands to printer
        printer.write(tsc_command_begin.encode() + bmp_data + tsc_command_end.encode())


if __name__ == "__main__":
    test()
