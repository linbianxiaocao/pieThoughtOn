Title: Rolling with Git
Date: 2015-9-24 13:50
Category: 

前前后后我使用git也有个把年头了，可是中间常被不同事务打扰，每当再拾起git，曾经熟练掌握的命令又变得好生疏。为了能够让知识的储备尽可能的不被中断，这里记录下我经常使用到的一些git命令。今后即使又有好久不碰git，期望回到这里能尽快恢复到我的记忆存储点。

<!-- PELICAN_END_SUMMARY -->

###新开一个project
```
mkdir ~/Hello-World
cd ~/Hello-World
git init
touch README
git add README
git commit -m 'first commit'
git remote add origin https://github.com/awesomejie/Hello-World.git
git push -u origin master
```

###remote和branch
```
git remote -v
git remote show origin
# changes URL for the remote origin
git remote set-url origin https://github.com/awesomejie/Hello-World.git
git branch -a,-v,-vv
git branch --merged, --no-merged
git branch hotfix; git checkout hotfix # 等同于git checkout -b hotfix
git branch -d hotfix 
```

###git的一些拓展运动
```
git push origin serverfix
git push origin serverfix:awesomebranch
git push origin :serverfix  # delete serverfix branch from server
git push
git pull
```

When you do `git fetch origin` that brings down new remote branch serverfix, you don't automatically have a new local serverfix branch - you only have an origin/serverfix pointer. To merge this branch into your current workin branch, you can run
```
git merge origin/serverfix
``` 

If you want your own serverfix branch that you can work on,
```
git checkout -b serverfix origin/serverfix
```
gives a local branch that starts where origin/serverfix is. Tracking is enabled also. 

###查看commit历史和diff不同的commits
```
git log -p, --stat
git diff  # to see what you've changed but not yet staged
git diff SHA_a SHA_b
git diff -cached (-staged)  # compare staged changes to last commit
```

###删除和重命名
```
git rm
git rm --cached README.txt  # tell git to ignore the file
# 文件重命名
# 以下命令等同于mv README.txt README; git rm README.txt; git add README
git mv README.txt README
```

###修改和undo
```
git commit --amend
git reset HEAD README  # unstage file README
git checkout -- README  # revert change back to last commit
                        # this is a dangerous command. use with caution.
```


