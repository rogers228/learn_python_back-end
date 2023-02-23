import jinja2

def render_jinja_html(template_loc,file_name,**context):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_loc+'/')
    ).get_template(file_name).render(context)

def test1():
    # 渲染
    h = render_jinja_html(r'C:\Users\user\Documents\GitHub\Learn_python\note\module\18_jinja2_html渲染',
        'test.html', name = 'Allen')

    print(h)

    # 成功渲染! 這樣一來html可以獨立為view模板 邏輯層由python負責

if __name__ == '__main__':
    test1()    