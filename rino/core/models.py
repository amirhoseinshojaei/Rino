from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
import slugify
import os
from django.core.validators import MaxLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.

    # Positions
POSITION_CHOICES = (
    # Some of managers
    ('founder','Founder'),
    ('co-founder','Co-founder'),
    ('ceo','CEO'),
    ('cto','CTO'),
    ('cfo','CFO'),
    ('hr-manager', 'HR Manager'),
    ('sales-manager', 'Sales Manager'),
    ('marketing-manager', 'Marketing Manager'),
    ('business-analyst', 'Business Analyst'),
    # Some of programmer
    ('programming-team-lead','Programming Team Lead'),
    ('backend-developer','Backend Developer'),
    ('frontend-developer', 'Frontend Developer'),
    ('fullstack-developer', 'Full Stack Developer'),
    ('devops-engineer', 'DevOps Engineer'),
    ('mobile-developer', 'Mobile Developer'),
    ('qa-engineer', 'QA Engineer'),
    ('product-manager', 'Product Manager'),
    ('data-analyst', 'Data Analyst'),
    ('data-scientist','Data Scientist'),
    # Some of Designer
    ('design-team-lead', 'Design Team Lead'),
    ('ui-ux designer', 'UI/UX Designer'),
    ('graphic-designer', 'Graphic Designer'),
    ('motion-designer', 'Motion Designer'),
)



# Some of Project types
PROJECT_TYPES = (
    ('internal','داخلی'),
    ('external','خارجی')
)


# some request type for contact us
REQUEST_TYPE_CHOICES = (
    ('individual','فردی'),
    ('company','شرکت'),
    ('business_owner','صاحب کسب و کار / مغازه')
)


# db for bad words in comments
class BadWords(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.CharField(max_length=50,unique=True, verbose_name='کلمه نامناسب')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')

    
    class Meta:
        verbose_name ='کلمه نامناسب'
        verbose_name_plural = 'کلمات نامناسب'


    def __str__(self):
        return self.word
    

# Validators for bad words in comments
def validate_no_bad_words(value):
    bad_word = BadWords.objects.values_list('word', flat=True)

    for word in bad_word:
        if word in value:
            raise ValidationError('استفاده از کلمه{word} مجاز نیست')
    





class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not first_name:
            raise ValueError('نام خود را وارد کنید')

        if not last_name:
            raise ValueError('نام خانوادگی خودرا وارد کنید')

        if not email:
            raise ValueError('ایمیل خود را وارد کنید')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # SuperUser section
    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



# Custom User
class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    user_name = models.CharField(max_length=50, verbose_name='نام کاربری')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='تاریخ عضویت')
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


    @property
    def username(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.user_name = self.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True




# Services db
class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', null=True, blank=True)
    image = models.ImageField(upload_to='services/', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    video = models.URLField(verbose_name='ویدیو', null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی')

    class Meta:
        verbose_name = 'سرویس'
        verbose_name_plural = 'خدمات'



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Services, self).save(self.title)



    def __str__(self):
        return self.title
    


# Services Multiple Images
class SrviceImages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='services/', null=True, blank=True)


    class Meta:
        verbose_name = 'تصویر سرویس'
        verbose_name_plural = 'تصاویر خدمات'



    def __str__(self):
        return f' Images for {self.service.title}'



# Teams db
class TeamMembers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    position = models.CharField(max_length=50, choices=POSITION_CHOICES ,verbose_name='سمت')
    description_duties = models.TextField(verbose_name='درباره وظایف')
    status = models.BooleanField(default=True, verbose_name='وضعیت')
    # social media
    face_book_link = models.URLField(verbose_name='لینک فیس بوک', null=True, blank=True)
    instagram_link = models.URLField(verbose_name='لینک اینستاگرام', null=True, blank=True)
    twitter_link = models.URLField(verbose_name='لینک توییتر', null=True, blank=True)
    github_link = models.URLField(verbose_name='لینک گیت هاب', null=True, blank=True)
    pinterest = models.URLField(verbose_name='لینک پینترست', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'عضو'
        verbose_name_plural = 'اعضای تیم'


    def __str__(self):
        return self.full_name
    


# Social Media rino
class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, verbose_name='نام فضای مجازی')
    link = models.URLField(verbose_name='لینک')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'لینک فضای مجازی'
        verbose_name_plural = 'لینک های فضای مجازی'


    def __str__(self):
        return self.name

   
# Category for projects
class ProjectsCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'دسته بندی پروژه'
        verbose_name_plural = 'دسته بندی پروژه ها'

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super(ProjectsCategory, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    




# Projects db
class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', blank=True, null=True)
    category = models.ForeignKey(ProjectsCategory, on_delete=models.CASCADE, verbose_name='دسته بندی')
    image = models.ImageField(upload_to='projects/')
    customer_name = models.CharField(max_length=50, verbose_name='نام مشتری')
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPES, default='external', verbose_name='نوع پروژه')
    description = models.TextField(verbose_name='توضیحات')
    start_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ شروع')
    end_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ پایان', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super(Projects, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title



# model for what our customer says
class CustomersSays(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    image = models.ImageField(upload_to='profile/customers/', default='default/profile.jpg', verbose_name='عکس مشتری')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')


    class Meta:
        verbose_name = 'نظر مشتری'
        verbose_name_plural = 'نظرات مشتریان'

    def __str__(self):
        return self.full_name
    

class SaysDescriptions(models.Model):
    customer = models.ForeignKey(CustomersSays, on_delete=models.CASCADE, related_name='customer_says_description')
    description = models.TextField(verbose_name='نظر')

    class Meta:
        verbose_name = 'گفته مشتری'
        verbose_name_plural = 'گفته های مشتریان'

    def __str__(self):
        return self.customer
    



class Packages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', null=True, blank=True)
    image = models.ImageField(upload_to='packages/image/Originals/', verbose_name='تصویر اصلی دوره')
    video = models.FileField(upload_to='packages/video/Originals/', verbose_name='ویدیو معرفی')
    description = models.TextField(verbose_name='توضیحات')
    is_free = models.BooleanField(default=False, verbose_name='رایگان')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت دوره', null=True, blank=True)
    is_sale = models.BooleanField(default=False, verbose_name='تخفیف', null=True, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت پس از تخفیف', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'پکیج آموزشی'
        verbose_name_plural = 'پکیج های آموزشی'

    
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Packages, self).save(*args, **kwargs)


    # Calculate Precentage
    def calculate_discount_precentage(self):
        if self.is_sale and self.sale_price > self.price:
            discount = (self.price - self.sale_price) / self.price * 100
            return round(discount, 0)
        

    def __str__(self):
        return self.title




# package Videos
class PackagesEpisode(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='package_episode')
    seasone = models.PositiveIntegerField(verbose_name='انتخاب فصل')
    episode = models.PositiveIntegerField(verbose_name='انتخاب اپیزود')
    # episode_video = models.FileField(upload_to='packages/', verbose_name='ویدیو')

    class Meta:
        verbose_name = 'اپیزود پکیج'
        verbose_name_plural = 'اپیزودهای پکیج ها'

    # Custom upload path
    def get_upload_path(instance, filename):
        package_name = instance.package.title

        return os.path.join(
            'packages',
            package_name,
            f'season{instance.seasone}'
            f'episode{instance.episode}',
            filename
        )
    
    episode_video = models.FileField(upload_to=get_upload_path, verbose_name='ویدیو')



class BlogCategories(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', null=True, blank=True)
    upload_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'دسته بندی وبلاگ'
        verbose_name_plural = 'دسته بندی وبلاگ ها'

    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(BlogCategories, self).save(*args, **kwargs)
    
   
    def __str__(self):
        return self.title

    

class Blogs(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات')
    category = models.ForeignKey(BlogCategories, on_delete=models.CASCADE, verbose_name='دسته بندی')
    # image = models.ImageField(upload_to='blogs/originals/', verbose_name='تصویر معرفی')
    upload_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ ها'

    
    def get_upload_path(instance, filename):
        blog_name = instance.title

        return os.path.join(
            'blogs',
            'originals',
            blog_name,
            filename
        )
    
    image = models.ImageField(upload_to=get_upload_path, verbose_name='ویدیو')


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Blogs, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title
    


class BlogImages(models.Model):
    blog = models.ForeignKey(Blogs, on_delete= models.CASCADE, related_name='images_blogs')
    image = models.ImageField(upload_to='blogs/', verbose_name='انتخاب تصویر')


    class Meta:
        verbose_name = 'تصویر مرتبط با وبلاگ'
        verbose_name_plural = 'تصاویر مرتبط با وبلاگ'

    def get_upload_path(instance, filename):
        blog_name = instance.blog.title

        return os.path.join(
            'blogs',
            blog_name,
            filename
        )
    
    image = models.ImageField(upload_to=get_upload_path, verbose_name='انتخاب تصویر')

    def __str__(self):
        return f'آپلود تصویر برای {self.blog.title}'



class BlogComments(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='blog_comments')
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    comment = models.TextField(max_length=100, verbose_name='نظر', validators=[
        MaxLengthValidator(100),
        validate_no_bad_words
    ])
    upload_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ انتشار')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'ثبت کامنت توسط {self.first_name} {self.last_name} برای وبلاگ {self.blog.title}'

    

class PackageComments(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='package_comments')
    first_name = models.CharField(max_length=50, verbose_name='نام ')    
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    comment = models.TextField(max_length=100, verbose_name='نظر', validators=[
        MaxLengthValidator(100),
        validate_no_bad_words
    ])
    upload_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ انتشار')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'ثبت کامنت برای دوره آموزشی {self.package.title} توسط {self.first_name} {self.last_name}'


class Contacts(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    regex_phone = RegexValidator(
        regex=r'^09\d{9}$',
        message='شماره تماس باید با 09 شروع شود و شامل 11 رقم باشد'
    )
    phone_number = models.CharField(max_length=11, verbose_name='شماره تماس', validators=[
        regex_phone
    ] )
    subject = models.CharField(max_length=150, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(default=timezone.now)

   
    class Meta:
        verbose_name = 'درخواست ارتباط'
        verbose_name_plural = 'درخواست های ارتباط'


    def __str__(self):
        return f'درخواست تماس از طرف {self.email}'
    


    

class Profiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, verbose_name='کاربر')
    slug = models.SlugField(verbose_name='اسلاگ', null=True, blank=True)


    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.user_name)
        super(Profiles, self).save(*args, **kwargs)


    
    def __str__(self):
        return self.user.user_name
    


class PurchasedPackages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE, related_name='purchase_profile', verbose_name='پروفایل')
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='purchase_package', verbose_name='پکیج آموزشی')
    purchase_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ خرید')

   
    class Meta:
        verbose_name = 'پکیج خریداری شده'
        verbose_name_plural = 'پکیج های خریداری شده'

    
   
    def __str__(self):
        return f'{self.profile.user.user_name} - {self.package.title}'
    


