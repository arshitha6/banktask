from django.db import models


class District(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Person(models.Model):
    genderlist = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    account_type = (
        ('savings', 'Savings'),
        ('current', 'Current'),
        ('deposit', 'Deposit')
    )
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=genderlist)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.SET_NULL,null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL,null=True)
    account = models.CharField(max_length=255, choices=account_type)
    debitcard = models.BooleanField('Debit Card', default=False)
    creditcard = models.BooleanField('Credit Card', default=False)
    passbook = models.BooleanField('Passbook', default=False)
    checkbook = models.BooleanField('Check Book', default=False)

    def __str__(self):
        return self.name

