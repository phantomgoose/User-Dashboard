from django.conf.urls import url
from .views import UsersRegister, UsersLogin, UsersLogout, UsersEdit, UsersUpdate, UsersShow, UsersCreateMessage, UsersCreateComment, UsersIndex, UsersRedirect, UsersAdmin, UsersNew, UsersDestroy, UsersSetAdmin, UsersRevokeAdmin

urlpatterns = [
    url(r'^register$', UsersRegister.as_view(), name='users-register'),
    url(r'^login$', UsersLogin.as_view(), name='users-login'),
    url(r'^logout$', UsersLogout.as_view(), name='users-logout'),
    url(r'^users/new$', UsersNew.as_view(), name='users-new'),
    url(r'^users/edit$', UsersEdit.as_view(), name='users-edit'),
    url(r'^users/edit/(?P<user_id>\d+)$', UsersAdmin.as_view(), name='users-admin'),
    url(r'^users/destroy/(?P<user_id>\d+)$', UsersDestroy.as_view(), name='users-destroy'),
    url(r'^users/update/$', UsersUpdate.as_view(), name='users-update'),
    url(r'^users/show/(?P<user_id>\d+)$', UsersShow.as_view(), name='users-show'),
    url(r'^users/setadmin/(?P<user_id>\d+$)', UsersSetAdmin.as_view(), name='users-set-admin'),
    url(r'^users/revoke/(?P<user_id>\d+$)', UsersRevokeAdmin.as_view(), name='users-revoke-admin'),
    url(r'^users/(?P<user_id>\d+)/messages/create/$', UsersCreateMessage.as_view(), name='users-create-message'),
    url(r'^users/(?P<user_id>\d+)/messages/(?P<message_id>\d+)/comments/create$', UsersCreateComment.as_view(), name='users-create-comment'),
    url(r'^$', UsersIndex.as_view(), name='users-index'),
    url(r'^', UsersRedirect.as_view(), name='users-redirect'),
]
