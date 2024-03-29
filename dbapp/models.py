from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Customers(models.Model):
    cno = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=18, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=6, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "customers"


class Employees(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=18, blank=True, null=True)
    zip = models.CharField(max_length=6, blank=True, null=True)
    hdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "employees"


class Parts(models.Model):
    pno = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=30, blank=True, null=True)
    qoh = models.IntegerField(blank=True, null=True)
    prices = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )  # Adjusted max_digits
    wlevel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "parts"


class Orders(models.Model):
    ono = models.IntegerField(primary_key=True)
    cno = models.ForeignKey(
        Customers, on_delete=models.CASCADE, db_column="cno", blank=True, null=True
    )
    eno = models.ForeignKey(
        Employees, on_delete=models.CASCADE, db_column="eno", blank=True, null=True
    )
    received = models.DateField(blank=True, null=True)
    shipped = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orders"


class Odetails(models.Model):
    id = models.AutoField(primary_key=True)  # Adding an explicit ID for the primary key
    ono = models.ForeignKey(
        Orders, on_delete=models.CASCADE, db_column="ono", blank=True, null=True
    )
    pno = models.ForeignKey(
        Parts, on_delete=models.CASCADE, db_column="pno", blank=True, null=True
    )
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "odetails"


class Zipcodes(models.Model):
    zip = models.CharField(max_length=6, primary_key=True)
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "zipcodes"
