from django.db import models

# Create your models here.


class Census(models.Model):
    id = models.CharField(db_column='Id', max_length=60, blank=True, null=True)  # Field name made lowercase.
    id2 = models.CharField(db_column='Id2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    geography = models.CharField(db_column='Geography', max_length=60, blank=True, null=True)  # Field name made lowercase.
    target_geo_id = models.CharField(db_column='Target Geo Id', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    target_geo_id2 = models.CharField(db_column='Target Geo Id2', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geographic_area = models.CharField(db_column='Geographic area', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geographic_area2 = models.CharField(db_column='Geographic area2', primary_key=True, max_length=60)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    population = models.CharField(db_column='Population', max_length=60, blank=True, null=True)  # Field name made lowercase.
    housing_units = models.CharField(db_column='Housing units', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    area_in_square_miles_total_area = models.CharField(db_column='Area in square miles - Total area', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    area_in_square_miles_water_area = models.CharField(db_column='Area in square miles - Water area', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    area_in_square_miles_land_area = models.CharField(db_column='Area in square miles - Land area', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    density_per_square_mile_of_land_area_population = models.CharField(db_column='Density per square mile of land area - Population', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    density_per_square_mile_of_land_area_housing_units = models.CharField(db_column='Density per square mile of land area - Housing units', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'census'


class Dentalpro(models.Model):
    licenseid = models.CharField(primary_key=True, max_length=32)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    address1 = models.CharField(max_length=32, blank=True, null=True)
    address2 = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    state = models.CharField(max_length=32, blank=True, null=True)
    zip = models.CharField(max_length=32, blank=True, null=True)
    phone1 = models.CharField(max_length=32, blank=True, null=True)
    fax = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    specialty = models.CharField(max_length=32, blank=True, null=True)
    active = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=32, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    pano = models.CharField(max_length=32, blank=True, null=True)
    pllcno = models.CharField(max_length=32, blank=True, null=True)
    county = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dentalpro'

