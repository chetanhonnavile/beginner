#find cidr with the given netmask


class net():

    def __init__(self,netmask):

        self.netmask = netmask
        cidr = 0
        #li = netmask.split(".")
        li = map(int,netmask.split("."))
        li = map(lambda x:bin(x),li)
        cidr = sum(i.count("1") for i in li )
        print cidr


ob = net("255.255.20.0")
