from django.core.context_processors import csrf
from mako.lookup import TemplateLookup
from mako import exceptions
from django import http


# 模板过滤器，None转化为字符串的结果为“None”，实际应用通常需要显示为“”，这个函数作为过滤器使用可以达到效果
def none_empty(o):
    return o if o else ''


# mako无法直接使用{%csrf%}，因此编写下面函数
def csrf_token(request):
    return '<input type="hidden" name="csrfmiddlewaretoken" value="%s" />'\
        % csrf(request)["csrf_token"]


# 使用form中的数据填写obj中名字相同字段，采用反射的机制实现
def model_from_form(obj, form):
    cd = form.cleaned_data
    [setattr(obj, v, cd[v]) for v in vars(obj) if v in cd]


# 封装mako的模板render
class TemplateRender(object):

    # 设定相关的参数，传入模板路径，以及需要额外的import
    def __init__(self, template_dirs, imports):
        myimport = [
            'from jiemoutils.django_views import none_empty, csrf_token']
        if imports:
            myimport.extend(imports)
        self.lookup = TemplateLookup(
            directories=template_dirs,
            input_encoding='utf-8',
            output_encoding='utf-8',
            default_filters=['none_empty', 'h', ],
            imports=myimport,
        )

    def render_to_response(self, filename, ctx):
        try:
            tp = self.lookup.get_template(filename)
            cont = tp.render(**ctx)
            return http.HttpResponse(cont)
        except Exception as e:
            print(e.__str__())
            return http.HttpResponse(exceptions.html_error_template().render())
