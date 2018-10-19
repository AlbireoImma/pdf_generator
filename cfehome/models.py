# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm, DateField
from datetime import datetime
#from MasFondos import settings

class UsuAuxCuotas(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    rut = models.CharField(max_length=22, blank=True, null=True)
    cuota = models.TextField(blank=True, null=True)
    valor = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True,auto_now_add=True)


    @classmethod
    def crear(cls,usuario,cuota, monto):
        UsuAuxCuotas=cls(id=str(usuario)+str(cuota),rut=usuario,cuota=cuota,valor=monto)
        return UsuAuxCuotas



    class Meta:
        managed = False
        db_table = 'usu_aux_cuotas'

    def __str__(self):
        return u'%s' % (self.id)



class CartolaResumen(models.Model):

    cliente_id = models.IntegerField()
    contrato_id = models.IntegerField()
    afp_id = models.IntegerField()
    periodo = models.IntegerField()
    saldo_inicial = models.IntegerField()
    saldo_actual = models.IntegerField()
    saldo_diferencia = models.IntegerField()
    total_cotizacion = models.IntegerField(blank=True, null=True)
    bono_reconoc = models.IntegerField(blank=True, null=True)
    total_ganancia = models.IntegerField(blank=True, null=True)
    monto_ult_cotizacion = models.IntegerField(blank=True, null=True)
    valor_cuota = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    num_cuota_ganada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    num_meses_ganado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rentabilidad_ganada = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rentabidad_sin_coti = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rentabidad_con_coti = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartola_resumen'


class Clientes(models.Model):
    id=models.IntegerField(primary_key=True)
    rut = models.CharField(unique=True, max_length=20)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=13)
    genero = models.CharField(max_length=9)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nacionalidad_id = models.IntegerField()
    direccion = models.CharField(max_length=255)
    numero = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    piso = models.CharField(max_length=255, blank=True, null=True)
    villa = models.CharField(max_length=255, blank=True, null=True)
    ciudad_id = models.IntegerField()
    comuna_id = models.IntegerField()
    region_id = models.IntegerField()
    telefono_fijo = models.CharField(max_length=255, blank=True, null=True)
    telefono_celular = models.CharField(max_length=255, blank=True, null=True)
    telefono_otro = models.CharField(max_length=255, blank=True, null=True)
    correo1 = models.CharField(max_length=255)
    correo2 = models.CharField(max_length=255, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    nombre_cargo = models.CharField(max_length=100, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    autor_id = models.IntegerField(blank=True, null=True)
    actualizador_id = models.IntegerField(blank=True, null=True)
    termino_id = models.IntegerField(blank=True, null=True)
    token_cel = models.CharField(max_length=4000, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'

    def __str__(self):
        return u'%s' % (self.nombre+" "+self.apellido_paterno)

class Regiones(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    pais_id = models.IntegerField()
    codigo = models.CharField(max_length=5)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regiones'

class Contratos(models.Model):
    id = models.IntegerField(primary_key=True)
    numero_contrato = models.CharField(max_length=255)
    numero_renovacion = models.IntegerField()
    cliente_id = models.IntegerField()
    cliente_asociado_id = models.IntegerField(blank=True, null=True)
    fecha_contrato = models.DateField(blank=True, null=True)
    fecha_vigencia = models.DateField(blank=True, null=True)
    fecha_pac = models.DateField(blank=True, null=True)
    estado_id = models.IntegerField()
    descripcion_termino = models.CharField(max_length=255, blank=True, null=True)
    descripcion_rechazo = models.TextField(blank=True, null=True)
    autor_id = models.IntegerField(blank=True, null=True)
    actualizador_id = models.IntegerField(blank=True, null=True)
    ejecutivo_id = models.IntegerField(blank=True, null=True)
    plan_id = models.IntegerField(blank=True, null=True)
    promocion = models.CharField(max_length=255, blank=True, null=True)
    convenio_id = models.IntegerField(blank=True, null=True)
    documento_estado_id = models.IntegerField(blank=True, null=True)
    renovar_contrato = models.IntegerField()
    fecha_vigencia_hasta = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contratos'
    def __str__(self):
        return u'%s' % (self.id)


class Nacionalidades(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nacionalidades'

    def __str__(self):
        return u'%s' % (self.name)

class Afp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    web = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afp'
    def __str__(self):
        return u'%s' % (self.name)

class ContratosAfp(models.Model):
    contrato_id = models.IntegerField()
    afp_id = models.IntegerField()
    obligatoria = models.IntegerField(blank=True, null=True)
    apv = models.IntegerField(blank=True, null=True)
    cuenta_ahorro = models.IntegerField(blank=True, null=True)
    ahorro_convenio = models.IntegerField(blank=True, null=True)
    clave_acceso = models.CharField(max_length=255, blank=True, null=True)
    clave_seguridad = models.CharField(max_length=255, blank=True, null=True)
    clave_acceso_autoit = models.CharField(max_length=255, blank=True, null=True)
    clave_seguridad_autoit = models.CharField(max_length=255, blank=True, null=True)
    secuencia = models.IntegerField()
    actualizador_id = models.IntegerField(blank=True, null=True)
    autor_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contratos_afp'
    def __str__(self):
        return u'%s' % (self.contrato_id)

class Cities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    codigo = models.CharField(max_length=5)
    cod_region = models.CharField(max_length=5)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'

class Communes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    codigo = models.CharField(max_length=5)
    cod_ciudad = models.CharField(max_length=5)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communes'

class ContratosTiposClientes(models.Model):
    contrato_id = models.IntegerField()
    tipo_cliente = models.CharField(max_length=20)
    autor_id = models.IntegerField(blank=True, null=True)
    actualizador_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contratos_tipos_clientes'

class ContratosPlanPagos(models.Model):
    id = models.IntegerField(primary_key=True)
    contrato_id = models.IntegerField()
    ejecutivo_id = models.IntegerField(blank=True, null=True)
    comision_id = models.IntegerField(blank=True, null=True)
    estado_pago_id = models.IntegerField(blank=True, null=True)
    cobranza_pac_detalle_id = models.IntegerField(blank=True, null=True)
    banco_id = models.IntegerField(blank=True, null=True)
    cuota = models.IntegerField()
    monto = models.IntegerField()
    estado_id = models.IntegerField()
    fecha_cobro = models.DateField()
    fecha_pago = models.DateField(blank=True, null=True)
    numero_boleta = models.IntegerField(blank=True, null=True)
    fecha_boleta = models.DateField(blank=True, null=True)
    neto = models.IntegerField(blank=True, null=True)
    monto_pago = models.IntegerField(blank=True, null=True)
    monto_comision = models.IntegerField(blank=True, null=True)
    estado_venta_id = models.IntegerField(blank=True, null=True)
    fecha_pago_comision = models.DateField(blank=True, null=True)
    contable_year = models.IntegerField(blank=True, null=True)
    contable_month = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contratos_plan_pagos'

class ContratosPagos(models.Model):
    contrato_id = models.IntegerField()
    peridiocidad = models.CharField(max_length=255)
    forma_pagos_id = models.IntegerField()
    dia_pagos = models.IntegerField()
    banco_id = models.IntegerField()
    tipo_cuenta = models.CharField(max_length=20)
    numero_cuenta = models.CharField(max_length=255, blank=True, null=True)
    forma_pago_cuota_id = models.IntegerField()
    monto = models.IntegerField()
    fecha_cobro = models.DateField(blank=True, null=True)
    valor_cuota = models.IntegerField()
    fecha_inicio_pago = models.DateField(blank=True, null=True)
    cheque_banco_id = models.IntegerField(blank=True, null=True)
    fecha_cheque = models.DateField(blank=True, null=True)
    numero_serie_cheque = models.CharField(max_length=255, blank=True, null=True)
    valor_cheque = models.CharField(max_length=255, blank=True, null=True)
    numero_cheque = models.CharField(max_length=255, blank=True, null=True)
    autor_id = models.IntegerField(blank=True, null=True)
    actualizador_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contratos_pagos'

class FormaPagos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forma_pagos'

class DiaPagos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dia_pagos'

class Planes(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planes'


class Convenios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=255)
    descuento_planilla = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenios'
class Ejecutivos(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    rut = models.CharField(unique=True, max_length=20)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=11)
    genero = models.CharField(max_length=9)
    fecha_nacimiento = models.DateField()
    nacionalidad_id = models.IntegerField()
    direccion = models.CharField(max_length=255)
    numero = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    piso = models.CharField(max_length=255, blank=True, null=True)
    villa = models.CharField(max_length=255, blank=True, null=True)
    ciudad_id = models.IntegerField()
    comuna_id = models.IntegerField()
    region_id = models.IntegerField()
    telefono_fijo = models.CharField(max_length=255, blank=True, null=True)
    telefono_celular = models.CharField(max_length=255, blank=True, null=True)
    telefono_otro = models.CharField(max_length=255, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    autor_id = models.IntegerField(blank=True, null=True)
    actualizador_id = models.IntegerField(blank=True, null=True)
    termino_id = models.IntegerField(blank=True, null=True)
    tipo_cuenta = models.CharField(max_length=255)
    numero_cuenta = models.CharField(max_length=255, blank=True, null=True)
    banco_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejecutivos'

    def __str__(self):
        return u'%s' % (self.nombre)

class Estados(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'

class Documentos(models.Model):
    uuid = models.CharField(max_length=36)
    documentable_id = models.IntegerField()
    documentable_type = models.CharField(max_length=255)
    tipo_documento_id = models.IntegerField(blank=True, null=True)
    tipo_cuenta_afp_id = models.IntegerField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos'

class DetalleOrden(models.Model):
    id =models.IntegerField(primary_key=True)
    orden = models.ForeignKey(
        'OrdenCompra', models.DO_NOTHING, db_column='orden_id')
    cuota_id = models.IntegerField()
    fecha_cuota =  models.DateTimeField()
    monto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_orden'


class OrdenCompra(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente_id = models.IntegerField()
    contrato_id = models.IntegerField()
    fecha_orden = models.DateTimeField()
    monto_orden = models.IntegerField()
    cantidad_cuotas = models.IntegerField()
    estado_orden = models.IntegerField()
    cod_autorizacion = models.CharField(max_length=32)
    tipo_pago = models.CharField(max_length=32)
    cod_respuesta = models.CharField(max_length=32)
    cuotas_tarjeta = models.IntegerField()
    nro_tarjeta = models.CharField(max_length=4)
    fecha_tarjeta = models.CharField(max_length=32)
    id_session = models.CharField(max_length=32)
    # Field name made lowercase.
    vci = models.CharField(db_column='VCI', max_length=10)
    fecha_transaccion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_compra'