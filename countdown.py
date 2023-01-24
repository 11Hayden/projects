#!/usr/bin/python3
import sys
import time
import sevseg

# countdown time
secsLeft = 550

try:
    while True:
        # to clear the screen and ensure the countdown is on a diffent page
        print('\n' * 35)

        # to get the hours/minutes/seconds from the secsLeft:
        # to get the hours we divide secsLeft by 3600 which is 60*60
        hours = str(secsLeft // 3600)

        # to get the minutes we take the remainder form secsLeft\
        # mod 3600 and divide it by 60
        minutes = str((secsLeft % 3600) // 60)

        # to get the seconds we calculate secsLeft mod 60
        seconds = str(secsLeft % 60)

        # Get the digit string fom the imported sevseg:
        Hh = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMidRow, hLowRow = Hh.splitlines()

        Mh = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMidRow, mLowRow = Mh.splitlines()

        Sh = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMidRow, sLowRow = Sh.splitlines()

        # display the digits:
        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMidRow + '  *  ' + mMidRow + '  *  ' + sMidRow)
        print(hLowRow + '  *  ' + mLowRow + '  *  ' + sLowRow)

        if secsLeft == 0:
            print()
            print('     ****BOOM!!****      ')
            break
        print()
        print('Press CTRL+c to quit.')

        # for a 1second pause.
        time.sleep(1)
        secsLeft -= 1
except KeyboardInterrupt:
    sys.exit()  # to end program when Ctrl+c is pressed.
