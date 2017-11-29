import platform
print(platform.architecture())
print(platform.machine())
print(platform.node())
print(platform.platform())
print(platform.processor())
print(platform.python_build())
print(platform.python_compiler())
print(platform.python_branch())
print(platform.python_implementation())
print(platform.python_revision())
print(platform.python_version())
print(platform.python_version_tuple())
print(platform.release())
print(platform.system())
system = ''
release = ''
version = ''
print(platform.system_alias(system, release, version))
print(system, release, version)
print(platform.version())
print(platform.uname())

#16.14.2. Java プラットフォーム
print(platform.java_ver())
#16.14.3. Windows プラットフォーム
print(platform.win32_ver())
#16.14.4. Mac OS プラットフォーム
print(platform.mac_ver())
#16.14.5. Unix プラットフォーム
print(platform.dist())
print(platform.linux_distribution())
print(platform.libc_ver())

