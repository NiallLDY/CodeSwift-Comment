import os

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

    def change_404(self):
        file_path = self.theme_path + '/assets/404.html'
        
        old_string = '''title: "404: Page not found"'''
        new_string = '''title: "404错误: 页面不存在"'''
        self.replace(file_path, old_string, new_string)

    def add_featuredImage(self):
        file_path = self.theme_path + '/_layouts/home.html'
        
        old_string = '''<div id="post-list">

{% for post in posts %}

  <div class="post-preview">
    <h1>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </h1>

    <div class="post-content">
      <p>
        {% include no-linenos.html content=post.content %}
        {{ content | markdownify | strip_html | truncate: 200 | escape }}
      </p>
    </div>

    <div class="post-meta text-muted d-flex">

      <div class="mr-auto">
        <!-- posted date -->
        <i class="far fa-calendar fa-fw"></i>
        {% include timeago.html date=post.date tooltip=true %}

        <!-- time to read -->
        <i class="far fa-clock fa-fw"></i>
        {% include read-time.html content=post.content %}

        <!-- categories -->
        {% if post.categories.size > 0 %}
          <i class="far fa-folder-open fa-fw"></i>
          <span>
          {% for category in post.categories %}
            {{ category }}
            {%- unless forloop.last -%},{%- endunless -%}
          {% endfor %}
          </span>
        {% endif %}
      </div>

      {% if post.pin %}
      <div class="pin">
        <i class="fas fa-thumbtack fa-fw"></i>
        <span>{{ site.data.locales[lang].post.pin_prompt }}</span>
      </div>
      {% endif %}

    </div> <!-- .post-meta -->

  </div> <!-- .post-review -->

{% endfor %}

</div> <!-- #post-list -->'''
        new_string = '''<div id="post-list">

{% for post in posts %}

  <div class="post-preview-with-image">
    
    <div class="preview-image">
      <a href="{{ post.url | relative_url }}">
        {% if post.image.src %}
          {% capture bg %}
            {% unless post.image.no_bg %}{{ 'bg' }}{% endunless %}
          {% endcapture %}
          <img data-src="{{ post.image.src }}" class="my-image"
              alt="{{ post.image.alt | default: "Preview Image" }}"
              src="{{ post.image.src }}">
        {% endif %}
      </a>
    </div>
    <div class="post-preview-post-alone">

      <h1>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h1>

      <div class="post-content">
        <p>
          {% include no-linenos.html content=post.content %}
          {{ content | markdownify | strip_html | truncate: 200 | escape }}
        </p>
      </div>

      <div class="post-meta text-muted d-flex">

        <div class="mr-auto">
          <!-- posted date -->
          <i class="far fa-calendar fa-fw"></i>
          {% include timeago.html date=post.date tooltip=true %}

          <!-- time to read -->
          <i class="far fa-clock fa-fw"></i>
          {% include read-time.html content=post.content %}

          <!-- categories -->
          {% if post.categories.size > 0 %}
            <i class="far fa-folder-open fa-fw"></i>
            <span>
            {% for category in post.categories %}
              {{ category }}
              {%- unless forloop.last -%},{%- endunless -%}
            {% endfor %}
            </span>
          {% endif %}
        </div>

        {% if post.pin %}
        <div class="pin">
          <i class="fas fa-thumbtack fa-fw"></i>
          <span>{{ site.data.locales[lang].post.pin_prompt }}</span>
        </div>
        {% endif %}

      </div> <!-- .post-meta -->
    </div>
  </div> <!-- .post-review -->

{% endfor %}

</div> <!-- #post-list -->'''
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
        theme.add_featuredImage()
        theme.change_404()

    else:
        pass
