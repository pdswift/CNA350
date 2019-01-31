from subprocess import Popen, PIPE

    def running_vms():
        """
        Return list of running vms
        """
        f = Popen(r'vboxmanage --nologo list runningvms', stdout=PIPE).stdout
        data = [ eachLine.strip() for eachLine in f ]
        return data

    def restore_vm(name='', snapshot=''):
        """
        Restore VM to specific snapshot uuid

        name = VM Name
        snapshot = uuid of snapshot  (uuid can be found in the xml file of your machines folder)
        """
        command = r'vboxmanage --nologo snapshot %s restore %s' % (name,snapshot)
        f = Popen(command, stdout=PIPE).stdout
        data = [ eachLine.strip() for eachLine in f ]
        return data

    def launch_vm(name=''):
        """
        Launch VM

        name = VM Name
        """
        command = r'vboxmanage --nologo startvm %s ' % name
        f = Popen(command, stdout=PIPE).stdout
        data = [ eachLine.strip() for eachLine in f ]
        return data