from rest_framework.permissions import BasePermission 
 
class IsAdmin(BasePermission):
    def has_permission(self,req,view):
        return req.user.is_authenticated and req.user.userrole.role=="admin"
class IsTeacher(BasePermission):
    def has_permission(self,req,view):
        return req.user.is_authenticated and req.user.userrole.role=="teacher"
class IsStudent(BasePermission):
    def has_permission(self,req,view):
        return req.user.is_authenticated and req.user.userrole.role=="student"
 