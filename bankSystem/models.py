from django.db import models

# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=255)

    # to edit the name of the branch in adamin dasheborad
    class Meta:
        verbose_name_plural = "Branches"

    def json_object(self):
        return {"name": self.name, "address": self.address}

    def __str__(self):
        return self.name


class Bank(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def json_object(self):
        return {"name": self.name}

    def __str__(self):
        return self.name


class ClientManager(models.Model):
    name = models.CharField(max_length=255)

    def json_object(self):
        return {"name": self.name}

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def json_object(self):
        return {"name": self.name, "address": self.address}

    def __str__(self) -> str:
        return self.name


class Account(models.Model):
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100)
    open_date = models.CharField(max_length=100)

    def json_object(self):
        return {
            "clients": self.clients,
            "open_date": self.open_date,
            "account_type": self.account_type,
            "bank": self.bank,
        }

    def __str__(self):
        return self.account_type


class Transfer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def json_object(self):
        return {"account": self.account, "branch": self.branch}

    def __str__(self):
        return "Account Transfered to {} Branch".format(self.branch.name)


class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Deposite(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
