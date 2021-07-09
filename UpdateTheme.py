import os

class UpdateTheme:

    def __init__(self):
        super().__init__()
        self.file_dir = '/var/lib/gems/2.7.0/gems/'
        # self.file_dir = '/Users/lvdingyang/Desktop/Test/'
        self.theme_path = ''

        self.get_latest_theme_dir(self.file_dir)
    

    def get_latest_theme_dir(self, path):
        # 获取所有的 jekyll-theme-chirpy 文件夹路径
        dirs = []
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                if 'jekyll-theme-chirpy-' in file_path:
                    dirs.append(file)
        # print(dirs)
        assert (len(dirs) > 0), "未找到 jekyll-theme-chirpy 主题！"
        
        # 获得最新的版本
        def max_versions(v1, v2):
            list1 = str(v1).split(".")
            list2 = str(v2).split(".")
            for i in range(len(list1)):
                if int(list1[i]) == int(list2[i]):
                    pass
                elif int(list1[i]) < int(list2[i]):
                    return v2
                else:
                    return v1
        
        latest_version = '0.0.0'
        for dir in dirs:
            assert (len(dir) > 20), "jekyll-theme-chirpy 无版本号！"
            version = dir[20:]
            latest_version = max_versions(version, latest_version)
        latest_version_path = path + 'jekyll-theme-chirpy-' + latest_version
        # print(latest_version_path)
        
        self.theme_path = latest_version_path


    def replace(self, file, old, new):
        with open(file, 'r') as f:
            content = f.read()
            if old in content:
                content = content.replace(old, new, -1)
                with open(file, 'w') as f:
                    f.write(content)
            else:
                print(file + "更改失败，未找到替换内容，请手动修改！")

    def insert(self, file, before, content):
        with open(file, 'r') as f:
            file_content = f.read()
            if content in file_content:
                print("内容已存在！")
                return

            if before in file_content:
                content = content + '\n' + before
                file_content = file_content.replace(before, content, -1)
                with open(file, 'w') as f:
                    f.write(file_content)
            else:
                print(file + "添加失败，未找到定位内容！")



    def change_sidebar(self):
        file_path = self.theme_path + '/_includes/sidebar.html'

        old_string = '''<span>{{ "HOME" }}</span>'''
        new_string = '''<span>{{ "主页" }}</span>'''
        self.replace(file_path, old_string, new_string)

    def change_topbar(self):
        file_path = self.theme_path + '/_includes/topbar.html'

        old_string = '''<a href="{{ '/' | relative_url }}">{{ 'Home' }}</a>'''
        new_string = '''<a href="{{ '/' | relative_url }}">{{ '主页' }}</a>'''
        self.replace(file_path, old_string, new_string)

        old_string = '''{{ item | capitalize }}'''
        new_string = '''{{ '主页' }}'''
        self.replace(file_path, old_string, new_string)

        old_string = '''<span>{{ 'Posts' }}</span>'''
        new_string = '''<span>{{ '文章' }}</span>'''
        self.replace(file_path, old_string, new_string)

        old_string = '''<span id="search-cancel" >Cancel</span>'''
        new_string = '''<span id="search-cancel" >取消</span>'''
        self.replace(file_path, old_string, new_string)


        old_string = '''<div id="topbar-title">
      {% if page.layout == 'home' %}
        {{- site.title -}}
      {% elsif page.dynamic_title %}
        {{- page.title -}}
      {% else %}
        {{- page.layout | capitalize -}}
      {% endif %}
    </div>'''
        new_string = '''<div id="topbar-title">
      {% if page.layout == 'home' %}
        {{- site.title -}}
      {% elsif page.dynamic_title %}
        {{- page.title -}}
      {% else %}
        {% if page.layout == 'post' %}
          {{ '文章' }}
        {% elsif page.layout == 'category' %}
          {{ '分类' }}
        {% else %}
          {{ '标签' }}
        {% endif %}
        <!-- {{- page.layout | capitalize -}} -->
      {% endif %}
    </div>'''
        self.replace(file_path, old_string, new_string)


    def change_readtime(self):
        file_path = self.theme_path + '/_includes/read-time.html'

        old_string = '''title="{{ words }} words">'''
        new_string = '''title="{{ words }} 字">'''
        self.replace(file_path, old_string, new_string)
    
    def change_postsharing(self):
        file_path = self.theme_path + '/_includes/post-sharing.html'

        old_string = '''title="Copy link"></i>'''
        new_string = '''title="拷贝链接"></i>'''
        self.replace(file_path, old_string, new_string)
    
    def change_homeminjs(self):
        file_path = self.theme_path + '/assets/js/dist/home.min.js'

        old_string = '''toLocaleString("en-US"'''
        new_string = '''toLocaleString("zh-CN"'''
        self.replace(file_path, old_string, new_string)

        old_string = '''" day"+(r>1?"s":"")+" ago"'''
        new_string = '''" 天前"'''
        self.replace(file_path, old_string, new_string)

        old_string = '''" hour"+(i>1?"s":"")+" ago"'''
        new_string = '''" 小时前"'''
        self.replace(file_path, old_string, new_string)

        old_string = '''" minute"+(d>1?"s":"")+" ago"'''
        new_string = '''" 分钟前"'''
        self.replace(file_path, old_string, new_string)

        old_string = '''"just now"'''
        new_string = '''"刚刚"'''
        self.replace(file_path, old_string, new_string)

    def change_postminjs(self):
        file_path = self.theme_path + '/assets/js/dist/post.min.js'

        old_string = '''toLocaleString("en-US"'''
        new_string = '''toLocaleString("zh-CN"'''
        self.replace(file_path, old_string, new_string)

        old_string = '''" day"+(i>1?"s":"")+" ago"'''
        new_string = '''" 天前"'''
        self.replace(file_path, old_string, new_string)

        old_string = '''" hour"+(r>1?"s":"")+" ago"'''
        new_string = '''" 小时前"'''
        self.replace(file_path, old_string, new_string)

        old_string = '''" minute"+(c>1?"s":"")+" ago"'''
        new_string = '''" 分钟前"'''
        self.replace(file_path, old_string, new_string)

        old_string = '''"just now"'''
        new_string = '''"刚刚"'''
        self.replace(file_path, old_string, new_string)

        old_string = '''alert("Link copied successfully!")'''
        new_string = '''alert("链接拷贝成功！")'''
        self.replace(file_path, old_string, new_string)
        
    def change_pageminjs(self):
        file_path = self.theme_path + '/assets/js/dist/page.min.js'
        
        old_string = '''alert("Link copied successfully!")'''
        new_string = '''alert("链接拷贝成功！")'''
        self.replace(file_path, old_string, new_string)
    
    def change_archives(self):
        file_path = self.theme_path + '/_layouts/archives.html'
        
        old_string = '''{% capture this_month %}{{ post.date | date: "%b" }}{% endcapture %}'''
        new_string = '''{% capture this_month %}{{ post.date | date: "%m" }}{% endcapture %}'''
        self.replace(file_path, old_string, new_string)

        old_string = '''<span class="date day">{{ this_day }}</span>
        <span class="date month small text-muted">{{ this_month }}</span>'''
        new_string = '''<span class="date month">{{ this_month }}</span>-
        <span class="date day">{{ this_day }}</span>'''
        self.replace(file_path, old_string, new_string)

    def change_post(self):
        file_path = self.theme_path + '/_layouts/post.html'

        old_string = '''{% include timeago.html date=page.date prep="on" tooltip=true %}'''
        new_string = '''{% include timeago.html date=page.date prep="发布于" tooltip=true %}'''
        self.replace(file_path, old_string, new_string)

        old_string = '''class="lastmod" prefix="Updated" tooltip=true %}'''
        new_string = '''class="lastmod" prefix="最近更新" tooltip=true %}'''
        self.replace(file_path, old_string, new_string)

        old_string = '''This post is licensed under
            <a href="{{ site.data.rights.license.link }}">{{ site.data.rights.license.name }}</a>
            by the author.'''
        new_string = '''该博客文章由作者通过
            <a href="{{ site.data.rights.license.link }}">{{ site.data.rights.license.name }}</a>
            进行授权。'''
        self.replace(file_path, old_string, new_string)

        before = '''</div> <!-- #post-extend-wrapper -->'''
        content = '''
      <!-- 评论功能 -->
      <div class="utterances">
        <script src="https://utteranc.es/client.js" 
                repo="NiallLDY/CodeSwift-Comment" 
                issue-term="pathname"
                theme='github-light' 
                crossorigin="anonymous" async>
        </script>
        <script type="text/javascript">
          $(function () {
            window.onmessage = evt => {
              if (evt.origin === 'https://utteranc.es') {
                toggle.updateCommentStyle();
                window.onmessage = null;
              }
            }
          });
        </script>
      </div>
      <!-- 评论功能 -->'''

        self.insert(file_path, before, content)

    def change_modetoggle(self):
        file_path = self.theme_path + '/_includes/mode-toggle.html'

        before = '''updateMermaid() {'''
        content = '''updateCommentStyle() {
      var theme = "github-light";
      if (this.modeStatus === ModeToggle.DARK_MODE) {
        theme = "photon-dark";
      }
      let comment = document.querySelector("iframe.utterances-frame");
      if (comment == null) {
        return;
      }
      comment.contentWindow.postMessage({
        type: "set-theme",
        theme: theme
      },
        "https://utteranc.es/");
    }
'''
        self.insert(file_path, before, content)

        before = '''this.updateMermaid();'''
        content = '''
        this.updateCommentStyle();
'''
        self.insert(file_path, before, content)


    def change_footer(self):
        file_path = self.theme_path + '/_includes/footer.html'
        
        old_string = '''Powered by
        <a href="https://jekyllrb.com" target="_blank" rel="noopener">Jekyll</a>
        with
        <a href="https://github.com/cotes2020/jekyll-theme-chirpy"
          target="_blank" rel="noopener">Chirpy</a>
        theme.'''
        new_string = '''<a href="https://beian.miit.gov.cn/" target="_blank">苏ICP备2021010146号-1</a>
        <!-- &nbsp;&nbsp;&nbsp;&nbsp; -->
        <!-- <a href="https://beian.miit.gov.cn/" target="_blank">苏ICP备2021010146号-1</a> -->'''
        self.replace(file_path, old_string, new_string)

    def change_404(self):
        file_path = self.theme_path + '/assets/404.html'
        
        old_string = '''<div class="lead">
  <p>Sorry, we've misplaced that URL or it's pointing to something that doesn't exist. </p>
  <p>
    <a href="{{ '/' | relative_url }}">Head back Home</a>
    to try finding it again, or search for it on the
    <a href="{{ 'archives' | relative_url }}">Archives page</a>.
  </p>
</div>'''
        new_string = '''<div class="lead">
  <p>抱歉，该URL不存在🙅‍♂️。 </p>
  <p>
    <a href="{{ '/' | relative_url }}">返回首页</a>
    再试一次, 或者在
    <a href="{{ 'archives' | relative_url }}">归档页</a>查找。
  </p>
</div>'''
        self.replace(file_path, old_string, new_string)
        old_string = '''title: "404: Page not found"'''
        new_string = '''title: "404错误: 页面不存在"'''
        self.replace(file_path, old_string, new_string)

    def change_categories(self):
        file_path = self.theme_path + '/_layouts/categories.html'
        
        old_string = '''{% if sub_categories_size > 1 %}categories{% else %}category{% endif %},'''
        new_string = '''个类别&nbsp;&nbsp;'''
        self.replace(file_path, old_string, new_string)

        old_string = '''post{% if top_posts_size > 1 %}s{% endif %}'''
        new_string = '''篇文章'''
        self.replace(file_path, old_string, new_string)

        old_string = '''post{% if posts_size > 1 %}s{% endif %}'''
        new_string = '''篇文章'''
        self.replace(file_path, old_string, new_string)


if __name__ == "__main__":
    theme = UpdateTheme()
    print('本次更新的是' + theme.theme_path + '，是否继续(y/n)？')
    choice = input()
    choices = ['y', 'Y', 'n', 'N']
    while len(choice) != 1 or choice not in choices:
        print("请重新输入：")
        choice = input()
    
    if choice == 'y' or choice == 'Y':
        theme.change_sidebar()
        theme.change_topbar()
        theme.change_readtime()
        theme.change_postsharing()
        theme.change_homeminjs()
        theme.change_postminjs()
        theme.change_pageminjs()
        theme.change_archives()
        theme.change_post()
        theme.change_modetoggle()
        theme.change_footer()
        theme.change_404()
        theme.change_categories()
    else:
        pass