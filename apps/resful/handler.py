import tornado.web

from abc import ABC
from tornado.escape import json_encode
from apps.resful.model import UserModel
from apps.base.base_handler import BaseHandler


class UserListHandler(tornado.web.RequestHandler, ABC):

    def get(self):
        users = UserModel.get_all()
        self.write(json_encode(users))

    def post(self):
        name = self.get_argument("name")
        age = self.get_argument("age")

        UserModel.create(name, age)

        resp = {"code": 200, "msg": "create success"}
        self.write(json_encode(resp))


class UserHandler(BaseHandler, ABC):

    def get(self, user_id):
        try:
            user = UserModel.get(int(user_id))
        except KeyError:
            return self.set_status(404)

        self.write(json_encode(user))

    def put(self, user_id):
        age = self.get_argument("age")
        UserModel.update(int(user_id), age)
        resp = {"code": 200, "msg": "update success"}
        self.write(json_encode(resp))

    def delete(self, user_id):
        UserModel.delete(int(user_id))
        resp = {"code": 200, "msg": "delete success"}
        self.write(json_encode(resp))
