from django.db import models

# Create your models here.
class University(models.Model):
    universityID = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    about = models.TextField()
    website = models.URLField(max_length=250)
    ranking = models.IntegerField(null=True, blank=True) 
    programs = models.ManyToManyField('Program', related_name='universities')  # Many-to-many with Program
    scholarships = models.ManyToManyField('Scholarship', related_name='universities')  # Many-to-many with Scholarship
    short_description = models.CharField(max_length=255, default='Your default value here')


    def __str__(self):
        return f"{self.name} | {self.location}"

    def showDetails(self):
        return {
            "universityID": self.universityID,
            "name": self.name,
            "location": self.location,
            "about": self.about,
            "website": self.website,
            "ranking": self.ranking,
        }

    def updateDetails(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
        return True


class School(models.Model):
    schoolID = models.IntegerField(unique=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='schools')
    name = models.CharField(max_length=250)
    fees = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.university.name}"

    def showSchool(self):
        return {
            "schoolID": self.schoolID,
            "university": self.university.name,
            "name": self.name,
            "fees": self.fees,
        }

    def updateSchool(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
        return True


class Program(models.Model):
    programID = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    about = models.TextField()
    short_description = models.CharField(max_length=255, default='Your default value here')


    def __str__(self):
        return self.name

    def showProgram(self):
        return {
            "programID": self.programID,
            "name": self.name,
            "about": self.about,
        }

    def updateProgram(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
        return True


class Scholarship(models.Model):
    scholarshipID = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    about = models.TextField()
    amount = models.FloatField()
    short_description = models.CharField(max_length=250, default="No description provided")

    def __str__(self):
        return self.name

    def getDetails(self):
        return {
            "scholarshipID": self.scholarshipID,
            "name": self.name,
            "about": self.about,
            "amount": self.amount,
        }

    def updateScholarship(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
        return True
    

    """
    uni1 = University.objects.create(universityID=101, name="Cairo University", location="Giza, Egypt", about="Cairo University is a public university in Egypt.", website="https://www.cairouni.com", ranking= 1, short_description = 'One of the best universities in Egypt')
    uni2 = University.objects.create(universityID=102, name="Ain Shams University", location="Ain Shams, Egypt", about="Ain Shams is a public university in Egypt.", website="https://www.asuuni.com", ranking= 2, short_description = "A prestigious university in Egypt")
    uni3 = University.objects.create(universityID=103, name="Helwan University", location="Helwan, Egypt", about="Helwan University is a public university in Egypt.", website="https://www.helwanuni.com", ranking= 3, short_description = 'A well-known University in Egypt')
    uni4 = University.objects.create(universityID=104, name="Mansoura University", location="Dakahlia, Egypt", about="Mansoura University is a public university in Egypt.", website="https://www.mansourauni.com", ranking= 4, short_description = 'One of the finest educational universities')    
    """

    """
    scholarshipID = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    about = models.TextField()
    amount = models.FloatField()
    short_description = models.CharField(max_length=250, default="No description provided")

    scho1 = Scholarship.objects.create(about = "This scholarship is awarded to people with academic excellence.", amount = 50.0, scholarshipID = "11", name = "Undergraduate Merit Scholarship", short_description = "Awarded to high-achieving students pursuing undergraduate degrees.")
    scho2 = Scholarship.objects.create(about = "This scholarship is awarded to people who want are seeking research studies after graduation.", amount = 75.0, scholarshipID = "12", name = "Graduate Research Scholarship", short_description = "Supports postgraduate students engaged in research activities.")
    scho3 = Scholarship.objects.create(about = "This scholarship is awarded to people who aim to study abroad for a semester or more.", amount = 20.0, scholarshipID = "13", name = "International Exchange Scholarship", short_description = "For students participating in international exchange programs.")
    scho4 = Scholarship.objects.create(about = "This scholarship is awarded to people who are interested in STEM subjects", amount = 100.0, scholarshipID = "14", name = "STEM Excellence Scholarship", short_description = "Encourages excellence in science, technology, engineering, and math.")

    "Search for scholarships by name, eligibility, or field..."
    
    """