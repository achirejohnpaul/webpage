from django.db import models


class SiteInfor(models.Model):
    company_name = models.CharField(max_length=255)
    about = models.TextField()
    company_definition = models.TextField(blank=True, null=True)
    company_vision = models.TextField(blank=True, null=True)
    company_addi_info = models.TextField(blank=True, null=True)
    phone_contact_one = models.CharField(max_length=15, blank=True, null=True)
    phone_contact_two = models.CharField(max_length=15, blank=True, null=True)
    email_add_one = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class Partnership(models.Model):
    partner_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_contact = models.CharField(max_length=15)
    email_add = models.EmailField()
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.partner_name


