# This package provides unique id in distribute system
# the algorithm is inspired by Twitter's famous snowflake
# its link is: https:#github.com/twitter/snowflake/releases/tag/snowflake-2010
#

# +---------------+----------------+----------------+
# |timestamp(ms)42  | worker id(10) | sequence(12) |
# +---------------+----------------+----------------+

# Copyright (C) 2022 by yu-liang.info

import time

CEpoch         = 1474802888000
CWorkerIdBits  = 10 # Num of WorkerId Bits
CSenquenceBits = 12 # Num of Sequence Bits

CWorkerIdShift  = 12
CTimeStampShift = 22

CSequenceMask = 0xfff
CMaxWorker    = 0x3ff

class IdWorker:
    def __init__(self, workerId):
        self.maxWorkerId = -1 ^ (-1 << CWorkerIdBits)

        if workerId > self.maxWorkerId or workerId < 0 :
            print("worker not fit")
            exit()
        self.workerId = workerId
        self.lastTimeStamp = -1
        self.sequence = 0

    def timeGen(self):
        return int(time.time() * 1000)

    def timeReGen(self, last):
        ts = int(time.time() * 1000)
        while True:
            if ts <= last:
                ts = self.timeGen()
            else:
                break
        return ts
        
    def NextId(self):
        ts = self.timeGen()
        if ts == self.lastTimeStamp:
            self.sequence = (self.sequence + 1) & CSequenceMask
            if self.sequence == 0:
                ts = self.timeReGen(ts)
        else:
            self.sequence = 0

        if ts < self.lastTimeStamp:
            print("Clock moved backwards, Refuse gen id")
            exit()
        self.lastTimeStamp = ts
        ts = (ts-CEpoch)<<CTimeStampShift | self.workerId<<CWorkerIdShift | self.sequence
        return ts

if __name__ == '__main__':
    iw = IdWorker(1)
    for i in range(20):
        print(iw.NextId())
