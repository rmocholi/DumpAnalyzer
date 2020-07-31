class peticion():
    srcIP = ""
    dstIP = ""
    prtcl = ""
    info = ""
    NoTimes = 0

    def __init__(self,src,dst,prt):
        self.srcIP=src
        self.dstIP=dst
        self.prtcl=prt


    def __str__(self):
        return f'"{self.srcIP}","{self.dstIP}","{self.prtcl}","{self.NoTimes}"'


    def __eq__(self,peticion):
        if self.srcIP == peticion.srcIP and self.dstIP == peticion.dstIP and self.prtcl == peticion.prtcl:
            return True
        else:
            return False


    def __hash__(self):
        return hash((self.srcIP, self.dstIP, self.prtcl))

