from django.urls import path, include
from . import views
from .views import index, registro, recuperar_pswd, email_recuperar_pswd, detalle_producto, carrito, pago, finpago \
                 , filtro, favs, perfil, editar_perfil, historial_compra, detalle_pedido, add_producto, pedidos_adm, usuarios_adm, \
                 productos_adm, mod_producto, delete_producto,salir, actualizarCarrito, agregar_al_carrito, eliminar_del_carrito, quitar_del_carrito, ver_carrito, detalle_boleta,compra

#URLS APP
urlpatterns = [
    path('', index, name='index'),
    path('recuperar_pswd/', recuperar_pswd, name='recuperar_pswd'),
    path('email_recuperar_pswd/', email_recuperar_pswd, name='email_recuperar_pswd'),
    path('detalle_prodcuto/<id>/', detalle_producto, name='detalle_producto'),
    path('carrito/', carrito, name='carrito'),
    path('pago/', pago, name='pago'),
    path('finpago/', finpago, name='finpago'),
    path('filtro/', filtro, name='filtro'),
    path('favs/', favs, name='favs'),
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('historial_compra/', historial_compra, name='historial_compra'),
    path('detalle_pedido/', detalle_pedido, name='detalle_pedido'),
    path('add_producto/', add_producto, name='add_producto'),
    path('pedidos_adm/', pedidos_adm, name='pedidos_adm'),
    path('usuarios_adm/', usuarios_adm, name='usuarios_adm'),
    path('productos_adm/', productos_adm, name='productos_adm'),
    path('mod_producto/<id>/', mod_producto, name='mod_producto'),
    path('delete_producto/<id>/', delete_producto, name='delete_producto'),
    path('salir/',salir,name='salir'),
    path('registro/', registro, name="registro"),
    path('actualizar_carrito/', actualizarCarrito, name='actualizar_carrito'),
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('quitar-del-carrito/<int:producto_id>/', quitar_del_carrito, name='quitar_del_carrito'),
    path('eliminar-del-carrito/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('ver-carrito/', ver_carrito, name='ver_carrito'),
    path('detalle_boleta/<id>', detalle_boleta, name='detalle_boleta'),
    path('compra/<int:producto_id>/', compra, name='compra'),
    path('historial_compra/', views.historial_compra, name='historial_compra'),
    path('eliminar_boleta/<uuid:boleta_id>/', views.eliminar_boleta, name='eliminar_boleta'),
    path('filtro/', views.filtro, name='filtro'),
    path('historial/', views.historial_compra, name='historial_compra'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
   
]


