from django.db import models

# Create your models here.
LABEL_CHOICES = (
    ('Công nghệ', 'Công nghệ'),
    ('Du lịch', 'Du lịch'),
    ('Giáo dục', 'Giáo dục'),
    ('Giải trí', 'Giải trí'),
    ('Kinh doanh', 'Kinh doanh'),
    ('Nhịp sống', 'Nhịp sống'),
    ('Phim ảnh', 'Phim ảnh'),
    ('Pháp luật', 'Pháp luật'),
    ('Sống trẻ', 'Sống trẻ'),
    ('Sức khỏe', 'Sức khỏe'),
    ('Thế giới', 'Thế giới'),
    ('Thể thao', 'Thể thao'),
    ('Thời sự', 'Thời sự'),
    ('Thời trang', 'Thời trang'),
    ('Xe', 'Xe'),
    ('Xuất bản', 'Xuất bản'),
    ('Ẩm thực', 'Ẩm thực'),
    ('Âm nhạc', 'Âm nhạc'),
    )
TEST_CHOICES = (
    ('A', 'Test A'),
    ('B', 'Test B'),
    ('C', 'Test C'),
)
class Link(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    label = models.CharField(max_length=255, choices=LABEL_CHOICES)
    priority = models.IntegerField(default=0)
    imageurl = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.title)

class Label(models.Model):
    label = models.CharField(max_length=255, choices= LABEL_CHOICES)
    image = models.ImageField()
    def __str__(self):
        return str(self.label)

class TestModel(models.Model):
    testchoice = models.CharField(choices=TEST_CHOICES, max_length=255)
    