Title: Rolling with Pelican
Date: 2015-10-28 13:12
Category: Python
Tags:
Slug: rolling-with-pelican
Authors:

Python的用途真是无处不在，包括制作一个github博客。最近读到[Jake VanderPlas](http://www.astro.washington.edu/users/vanderplas/)的博文[Migrating from Octopress to Pelican](https://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/)，油然产生了利用Pelican制作一个根正苗红的建立在Python上的博客平台，也在此和基于ruby的Octopress说暂别。
<!-- PELICAN_END_SUMMARY -->

Pelican还支持ipython notebook格式(ipynb)，能将博文和Python代码笔记完美结合，没有再好了！

创建Pelican博客，我主要参考了[Making a Static Blog with Pelican](http://nafiulis.me/making-a-static-blog-with-pelican.html)。在我所看到的讲解构建Pelican博客的技术文档中，个人感觉此文最明了也最有借鉴价值。由于习惯markdown语法，我修改了TEMPLATE变量以及make_entry方法。

```
TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Modified:
Category:
Tags:
Slug: {slug}
Authors:


"""

def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}_{:0>2}_{:0>2}_{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,                                
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)
```

运行Fabric的fab命令如下，即会在content目录下生成一篇符合markdown语法抬头的*.md文件。

```
$ fab make_entry:"New Post"
```


####Preview Content
安装livereload，用Fabric自动化生成网页文件。配置完成后只要在本机运行

```
$ fab live_build
```

如果博文源文件有修改，livereload会在网页浏览器内实时显示更新的内容。


####Using Plugins
还没有看明白，但今后为了博文支持ipynb格式，plugin的使用是必须的。


####Hosting on Github Pages
ghp-import可以很轻松的把指定文件夹里的内容import到gh-pages branch。运行如下命令

```
$ ghp-import output
$ git push git@github.com:awesomejie/awesomejie.github.io.git gh-pages:master
```

output文件夹下的内容就同步到awesomejie.github.io repository的master branch。

更好的方法是用fabric automate这两步。在fabfile.py底部添加方法

```
def github(publish_drafts=False): # 2
    try:  # 3
        if os.path.exists('output/drafts'):
            if not publish_drafts:
                local('rm -rf output/drafts')
    except Exception:
        pass

    local('ghp-import output')  # 4
    local('git push '
          'https://github.com/awesomejie/awesomejie.github.io.git '
          'gh-pages:master') # 5
    local('rm -rf output')  # 6
```

Publish到github，只需轻松敲打

```
$ fab github
```


