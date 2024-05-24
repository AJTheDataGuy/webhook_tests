from django.db import models

class JobCreated(models.Model):
    """When a job is booked"""
    job = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job

class DriverAssigned(models.Model):
    """When a primary or secondary driver is assigned to a job"""
    job = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver

class DriverUnAssigned(models.Model):
    """When a primary or secondary driver is unassigned from a job"""
    job = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver

class DriverArrivedPickup(models.Model):
    """When a driver arrives at the pickup location. 
    This can be triggered by either the driver updating
    the job status or entering a geo-fence"""
    job = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver

class DriverPickedUp(models.Model):
    """When a driver picks up the consignment"""
    job = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver

class DriverArrivedDropOff(models.Model):
    """When a driver arrives at the drop-off location. 
    This can be triggered by either the driver updating the job status
      or entering a geo-fence"""
    job = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver

class JobDelivered(models.Model):
    """When the consignment is delivered (completed)"""
    job = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    deliver_at = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job

class JobCanceled(models.Model):
    """When the consignment is canceled"""
    job = models.CharField(max_length=100)
    canceled_by = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job

class JobDetailsUpdated(models.Model):
    """When job details change 
    (pick-up or delivery address, contact information, package(s) data,
      freight code, or service type)"""
    job = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job

class JobDamagedFreight(models.Model):
    """When a driver has reported damaged freight"""
    job = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    files = models.CharField(max_length=200)
    note = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job

class JobFutilePickup(models.Model):
    """When a driver has reported futile pickup"""
    job = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job

class DriverBreakdown(models.Model):
    """When a driver flags a breakdown from the app"""
    driver = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver

class DriverBreakdownCleared(models.Model):
    """When a driver clears a previously flagged breakdown from the app"""
    driver = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver

class TripSheetCreated(models.Model):
    """When a trip sheet is created"""
    trip_sheet = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trip_sheet

class TripSheetUpdated(models.Model):
    """When any trip sheet details are updated that are NOT already captured by the more specific web hooks"""
    trip_sheet = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trip_sheet

class TripSheetStatusUpdated(models.Model):
    """When a trip sheet status is updated"""
    trip_sheet = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trip_sheet

class TripSheetManifestAssigned(models.Model):
    """When a manifest is assigned to a tripsheet"""
    trip_sheet = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trip_sheet

class TripSheetDriverAssigned(models.Model):
    """When a driver is assigned (primary or secondary) to a tripsheet"""
    trip_sheet = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trip_sheet

class TripSheetAssetAssigned(models.Model):
    """When an asset is assigned to a tripsheet"""
    trip_sheet = models.CharField(max_length=100)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trip_sheet