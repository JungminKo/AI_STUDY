
# Commonly Used Linux Command

- check disk space : `df -h` _(df : disk free)_
- display each subdirectory size : `du -sh /*` _(du : disk usage)_

### 
- copy directory to another directory : `cp -r dir1/ dir2/`
- move directory to another directory : `mv dir/ dir2/`, `mv dir/* dir/2`

### 
- count number of directories in current directory : `ls -l | grep ^d | wc -l`
- count number of files in current directory : `ls -l | grep ^- | wc -l`
- count number of sub files in current directory : `find . -type f | wc -l`

###
- Nvidia GPUs usage monnitoring : `nvidia-smi`
- Nvidia GPUs usage monnitoring for every second : `watch -d -n 1 nvidia-smi`

###
- zip zip : `zip a.zip -r ./*`
- unzip zip : `unzip a.zip -d ./target`
- zip tar : `tar -cvf a.tar`
- unzip tar : `tar -xvf a.tar`
