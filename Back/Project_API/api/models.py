# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_description = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'categories'
    
    def __str__(self):
      return self.cat_description


class Customers(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_nit = models.CharField(max_length=12)
    cus_fir_name = models.CharField(max_length=45)
    cus_last_name = models.CharField(max_length=45)
    cus_phone = models.CharField(max_length=15, blank=True, null=True)
    cus_email = models.CharField(max_length=45, blank=True, null=True)
    cus_address = models.CharField(max_length=45)
    cus_city = models.CharField(max_length=20)
    cus_datetime_add = models.DateTimeField()
    cus_datetime_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customers'


class DetailOrders(models.Model):
    dt_ord_id = models.AutoField(primary_key=True)
    ord = models.ForeignKey('Orders', models.DO_NOTHING)
    prod = models.ForeignKey('Products', models.DO_NOTHING)
    dt_ord_description = models.CharField(max_length=45)
    dt_ord_unit_price = models.DecimalField(max_digits=14, decimal_places=2)
    dt_ord_quantity = models.PositiveIntegerField()
    dt_ord_total = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_orders'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Employees(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_nit = models.CharField(max_length=12)
    emp_fir_name = models.CharField(max_length=45)
    emp_last_name = models.CharField(max_length=45)
    emp_phone = models.CharField(max_length=15, blank=True, null=True)
    emp_address = models.CharField(max_length=45)
    emp_user = models.CharField(max_length=20)
    emp_key = models.CharField(max_length=8)
    emp_position = models.CharField(max_length=45)
    emp_datetime_ingress = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employees'


class Orders(models.Model):
    ord_id = models.AutoField(primary_key=True)
    cus = models.ForeignKey(Customers, models.DO_NOTHING)
    cus_address = models.CharField(max_length=45)
    cus_city = models.CharField(max_length=20)
    ord_total = models.DecimalField(max_digits=14, decimal_places=2)
    ord_datetime_order = models.DateTimeField()
    ord_datetime_dispatch = models.DateTimeField()
    emp = models.ForeignKey(Employees, models.DO_NOTHING)
    ord_observation = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_description = models.CharField(max_length=100)
    prod_unit_price = models.DecimalField(max_digits=14, decimal_places=2)
    prod_stock = models.PositiveIntegerField()
    cat = models.ForeignKey(Categories, models.DO_NOTHING)
    prov = models.ForeignKey('Provider', models.DO_NOTHING)
    prod_datetime_ingress = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'

    def __str__(self):
      return self.prod_description


class Provider(models.Model):
    prov_id = models.AutoField(primary_key=True)
    prov_nit = models.CharField(max_length=12)
    prov_tradename = models.CharField(max_length=45)
    prov_address = models.CharField(max_length=100)
    prov_contact_fir_name = models.CharField(max_length=45)
    prov_contact_last_name = models.CharField(max_length=45)
    prov_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    prov_email = models.CharField(max_length=50, blank=True, null=True)
    prov_datetime_ingress = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'provider'

    def __str__(self):
      return self.prov_tradename
