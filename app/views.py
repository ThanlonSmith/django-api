from django.views import View
from django.http.response import JsonResponse
from . import models
from .forms.user_form import UserForm
import json


class UserView(View):
    def get(self, request):
        """
        查询(所有数据)
        :param request:
        :return:
        """
        query_set = models.User.objects.values('name')  # <QuerySet [{'name': 'Erics'}]>
        ret = {
            'status': 0,
            'data': list(query_set)  # 转换成列表,[{'name': 'Erics'}]
        }
        return JsonResponse(ret)

    def post(self, request):
        """
        增加数据
        :param request:
        :return:
        """
        # request.POST中是没有数据的，需要在body中获取，但是需要先将bytes->符串->反序列化转化成列表对象
        form = UserForm(None, json.loads(request.body.decode()))
        if form.is_valid():
            instance = form.save()
            ret = {
                'status': 0,
                'data': instance.pk
            }
            return JsonResponse(ret)
        else:
            ret = {
                'status': 1,
                'data': form.errors
            }
            return JsonResponse(ret)


class UserDetail(View):
    def get(self, request, pk):
        """
        查询单条数据
        :param request:
        :param pk:
        :return:
        """
        # instence = models.User.objects.filter(pk=pk)
        # print(instence)  # <QuerySet [<User: User object (1)>]>
        instence = models.User.objects.filter(pk=pk).first()
        print(instence)  # User object (1)
        ret = {
            'status': 0,
            'data': {
                'name': instence.name
            }
        }
        return JsonResponse(ret)

    def put(self, request, pk):
        """
        修改数据。restful规定更新数据，用put或者patch，put用得多一些
        :param request:
        :return:
        """
        instence = models.User.objects.filter(pk=pk).first()
        if not instence:
            ret = {
                'status': 1,
                'data': {
                    'name': '数据不存在'
                }
            }
            return JsonResponse(ret)
        # 借助form来修改(form中有新数据),降低了耦合度
        form = UserForm(instence, json.loads(request.body.decode()))
        if form.is_valid():
            instence = form.save()  # instence不更新也是可以的，还是查找到的和要修改的id是一样的
            ret = {
                'status': 0,
                'data': instence.pk
            }
            return JsonResponse(ret)
        else:
            ret = {
                'status': 1,
                'data': form.errors
            }
            return JsonResponse(ret)

    def delete(self, request, pk):
        """
        删除数据(删除单条数据)
        :param request:
        :param pk:
        :return:
        """
        models.User.objects.filter(pk=pk).delete()
        ret = {
            'status': 0,
            'data': []
        }
        return JsonResponse(ret)
