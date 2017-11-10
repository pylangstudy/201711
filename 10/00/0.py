import os

print(os.ctermid())
print(os.environ)
print(os.environb)
filename = '0.py'
print(os.fsencode(filename))
print(os.fsdecode(filename))
print(os.fspath(filename))

#print(os.PathLike.__fspath__())#TypeError: __fspath__() missing 1 required positional argument: 'self'
#p = os.PathLike('/media/mint/85f78c06-a96e-4020-ac36-9419b7e456db/mint/root/pj/Do/Python/pylangstudy/201711/10/00/0.py')
#p = os.PathLike()#TypeError: Can't instantiate abstract class PathLike with abstract methods __fspath__
#print(p.__fspath__())

print(os.getenv('PATH'))
print(os.getenvb(b'PATH'))
print(os.get_exec_path())
print(os.getegid())
print(os.geteuid())
print(os.getgid())
print(os.getgrouplist('username', 1000))
print(os.getgroups())
print(os.getlogin())
print(os.getpgid(0))
print(os.getpgrp())
print(os.getpid())
print(os.getppid())
which = os.PRIO_PROCESS
who = 0
print(os.getpriority(which, who))
print(os.PRIO_PROCESS)
print(os.PRIO_PGRP)
print(os.PRIO_USER)
print(os.getresuid())
print(os.getresgid())
print(os.getuid())
#username = 'user'
#gid = 1000
#print(os.initgroups(username, gid))#PermissionError: [Errno 1] Operation not permitted
#print(os.putenv(key, value))
#egid = 0
#print(os.setegid(egid))#PermissionError: [Errno 1] Operation not permitted
#euid = 0
#print(os.seteuid(euid))#PermissionError: [Errno 1] Operation not permitted
gid = 1000
print(os.setgid(gid))
#groups = [1000]
#print(os.setgroups(groups))#PermissionError: [Errno 1] Operation not permitted
print(os.setpgrp())
#print(os.setpgid(pid, pgrp))
#priority = 0
#print(os.setpriority(which, who, priority))
#print(os.setregid(rgid, egid))
#print(os.setresgid(rgid, egid, sgid))
#print(os.setresuid(ruid, euid, suid))
#print(os.setreuid(ruid, euid))
#print(os.getsid(pid))
#print(os.setsid())#PermissionError: [Errno 1] Operation not permitted
#print(os.setuid(uid))
#print(os.strerror(code))
print(os.supports_bytes_environ)
#print(os.umask(mask))
print(os.uname())
#print(os.unsetenv(key))

