> shutil是高级的 文件、文件夹、压缩包 处理模块

- shutil.copyfile( src, dst) 从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
- shutil.move( src, dst)  移动文件或重命名
- shutil.copymode( src, dst) 只是会复制其权限其他的东西是不会被复制的
- shutil.copystat( src, dst) 复制权限、最后访问时间、最后修改时间
- shutil.copy( src, dst)  复制一个文件到一个文件或一个目录
- shutil.copy2( src, dst)  在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西

