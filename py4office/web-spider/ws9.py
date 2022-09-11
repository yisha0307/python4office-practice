# css选择器
html_doc = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello World</h4>   
    </div>
    
    <div class="panel-body">
        <ul class="list" id="list-1">
           <li class="element">Foo</li>
           <li class="element">Bar</li>
           <li class="element">Jay</li>
        </ul>
        
        <ul class="list list-samll" id="list-2">
           <li class="element">Foo</li>
           <li class="element">Bar</li>
           <li class="element">Jay</li>
        </ul>
    </div>
    </div>
</div>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
print(soup.select('.panel .panel-heading'))  # select：返回列表
print(soup.select('ul li'))
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
