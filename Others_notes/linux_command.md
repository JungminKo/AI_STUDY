
# Commonly Used Linux Command

- check disk space : `df -h` _(df : disk free)_
- display each subdirectory size : `du -sh /*` _(du : disk usage)_

- count number of directories in current directory : `ls -l | grep ^d | wc -l`
- count number of files in current directory : `ls -l | grep ^- | wc -l`
- count number of sub files in current directory : `find . -type f | wc -l`
