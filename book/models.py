# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Books(models.Model):
    bookid = models.IntegerField(db_column='bookID', primary_key=True)  # Field name made lowercase.
    bookname = models.CharField(db_column='bookName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bookquantity = models.IntegerField(db_column='bookQuantity', blank=True, null=True)  # Field name made lowercase.
    bookinfo = models.CharField(db_column='bookInfo', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bookimgsrc = models.CharField(db_column='bookImgSrc', max_length=300, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    bookconcern = models.CharField(db_column='bookConcern', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bookoutcount = models.CharField(db_column='bookoutCount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bookchar = models.CharField(db_column='bookChar', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'books'


class Booktype(models.Model):
    typeid = models.AutoField(db_column='typeID', primary_key=True)  # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booktype'


class Borrowbook(models.Model):
    borrowid = models.AutoField(db_column='borrowID', primary_key=True)  # Field name made lowercase.
    readerid = models.IntegerField(db_column='readerID', blank=True, null=True)  # Field name made lowercase.
    managerid = models.IntegerField(db_column='managerID', blank=True, null=True)  # Field name made lowercase.
    borrowdate = models.DateTimeField(db_column='borrowDate', blank=True, null=True)  # Field name made lowercase.
    restoredate = models.DateTimeField(db_column='restoreDate', blank=True, null=True)  # Field name made lowercase.
    bookstate = models.CharField(db_column='bookState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bookid = models.IntegerField(db_column='bookID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'borrowbook'


class Manager(models.Model):
    managerid = models.AutoField(db_column='managerID', primary_key=True)  # Field name made lowercase.
    managename = models.CharField(db_column='manageName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    managepass = models.CharField(db_column='managePass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    realityname = models.CharField(db_column='realityName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    roleid = models.IntegerField(db_column='roleID', blank=True, null=True)  # Field name made lowercase.
    dutydate = models.DateTimeField(db_column='dutyDate', blank=True, null=True)  # Field name made lowercase.
    leavedate = models.DateTimeField(db_column='leaveDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manager'


class Reader(models.Model):
    readerid = models.AutoField(db_column='readerID', primary_key=True)  # Field name made lowercase.
    readername = models.CharField(db_column='readerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    readerchar = models.CharField(db_column='ReaderChar', max_length=50, blank=True, null=True)  # Field name made lowercase.
    readerpass = models.CharField(db_column='readerPass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    realityname = models.CharField(db_column='realityName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    readercredit = models.IntegerField(db_column='readerCredit', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    roleid = models.IntegerField(db_column='roleID', blank=True, null=True)  # Field name made lowercase.
    grandid = models.IntegerField(db_column='grandID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reader'


class Readergrade(models.Model):
    grandid = models.AutoField(db_column='grandID', primary_key=True)  # Field name made lowercase.
    grandname = models.CharField(db_column='grandName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='quanTity', blank=True, null=True)  # Field name made lowercase.
    maxmaney = models.CharField(db_column='maxManey', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateamount = models.IntegerField(db_column='dateAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'readergrade'


class Role(models.Model):
    roleid = models.AutoField(db_column='roleID', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='roleName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'
