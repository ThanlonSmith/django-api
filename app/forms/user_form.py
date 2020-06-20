from django import forms

from .. import models


class UserForm(forms.Form):
    name = forms.CharField(max_length=10)

    def __init__(self, instence=None, *args, **kwargs):  # 函数传参不要使用可变类型
        self.instence = instence
        super(UserForm, self).__init__(*args, **kwargs)  # 原封不动传过去，这样就可以多传递一个值

    def save(self):
        if self.instence:
            # 通过反射设置新值,不能直接self.instence.name='thanlon'
            # print(self.cleaned_data)
            for k, v in self.cleaned_data.items():
                setattr(self.instence, k, v)
            self.instence.save()
            return self.instence # 更新instence
            # 如果没有数据。校验通过的数据全部放在cleaned_data中，key value组成的字典:{'name': 'thanlon'}
        return models.User.objects.create(**self.cleaned_data)
