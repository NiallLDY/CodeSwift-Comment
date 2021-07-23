import os

# For Chirpy 4.1.0
class UpdateTheme:

    def __init__(self):
        super().__init__()
        self.file_dir = '/var/lib/gems/2.7.0/gems/'
        # self.file_dir = '/Users/lvdingyang/Desktop/'
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


    def change_post(self):
        file_path = self.theme_path + '/_layouts/post.html'

        before = '''</div> <!-- #post-extend-wrapper -->'''
        content = '''
      <!-- 评论功能 -->
      <div class="utterances">
        <script src="https://utteranc.es/client.js" 
                repo="XXXX" 
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
        
        old_string = '''      <p class="mb-0">
        {% capture _platform %}
          <a href="https://jekyllrb.com" target="_blank" rel="noopener">Jekyll</a>
        {% endcapture %}

        {% capture _theme %}
          <a href="https://github.com/cotes2020/jekyll-theme-chirpy" target="_blank" rel="noopener">Chirpy</a>
        {% endcapture %}

        {{ site.data.locales[site.lang].meta
          | default: 'Powered by :PLATFORM with :THEME theme.'
          | replace: ':PLATFORM', _platform | replace: ':THEME', _theme
        }}

      </p>
'''
        new_string = '''      <p class="mb-0">
        <a href="https://beian.miit.gov.cn/" target="_blank">苏ICP备XXXX号-1</a>
        <!-- &nbsp;&nbsp;&nbsp;&nbsp; -->
        <!-- <a href="https://beian.miit.gov.cn/" target="_blank">苏ICP备XXXX号-1</a> -->
      </p>'''
        self.replace(file_path, old_string, new_string)

        before = '''    </div>

    <div class="footer-right">'''
        content = '''      <p class="mb-0">
        {% capture _platform %}
          <a href="https://jekyllrb.com" target="_blank" rel="noopener">Jekyll</a>
        {% endcapture %}

        {% capture _theme %}
          <a href="https://github.com/cotes2020/jekyll-theme-chirpy" target="_blank" rel="noopener">Chirpy</a>
        {% endcapture %}

        {{ site.data.locales[site.lang].meta
          | default: 'Powered by :PLATFORM with :THEME theme.'
          | replace: ':PLATFORM', _platform | replace: ':THEME', _theme
        }}

      </p>
'''
        self.insert(file_path, before, content)


    def change_404(self):
        file_path = self.theme_path + '/assets/404.html'
        
        old_string = '''title: "404: Page not found"'''
        new_string = '''title: "404错误: 页面不存在"'''
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
        theme.change_post()
        theme.change_modetoggle()
        theme.change_footer()
        theme.change_404()
    else:
        pass