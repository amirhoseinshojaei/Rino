from django.contrib import admin
from . models import (
    BadWords,
    Users,
    Services,
    ServiceImages,
    TeamMembers,
    SocialMedia,
    ProjectsCategory,
    Projects,
    SaysDescriptions,
    CustomersSays,
    PackagesEpisode,
    PackageComments,
    Packages,
    BlogCategories,
    BlogImages,
    BlogComments,
    Blogs,
    Contacts,
    Profiles,
    PurchasedPackages
)
# Register your models here.

class ServiceImages(admin.StackedInline):
    model = ServiceImages


class SaysDescriptionAdmin(admin.StackedInline):
    model = SaysDescriptions



class PackageEpisodeAdmin(admin.StackedInline):
    model = PackagesEpisode



class PackageCommentsAdmin(admin.StackedInline):
    model = PackageComments


class BlogImagesAdmin(admin.StackedInline):
    model = BlogImages


class BlogCommentsAdmin(admin.StackedInline):
    model = BlogComments


class PurchasedPackagesAdmin(admin.StackedInline):
    model = PurchasedPackages



@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'date_joined',
        'is_admin',
        'is_active',
        'is_staff',


    )

    list_filter = (
        'is_active',
        'is_staff',
        'is_admin'
    )

    search_fields = (
        'username',
        'email'
    )

    date_hierarchy = 'date_joined'

    readonly_fields = (
        'date_joined',
        'last_login'
    )


    def has_add_permission(self, request):
        return request.user.is_superuser
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser
    
    def has_module_permission(self, request):
        return request.user.is_superuser
    
    def has_view_permission(self, request, obj = None):
        return request.user.is_superuser
    



@admin.register(BadWords)     
class BadWordsAdmin(admin.ModelAdmin):
    list_display = (
        'word',
        'created_at'
    )

    list_filter = (
        'created_at',
    )

    # list_editable = (
    #     'word',
    # )

    search_fields = (
        'word',
    )

    date_hierarchy = 'created_at'

    readonly_fields = (
        'created_at',
    )


    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'video',
        'date_added',
        'date_updated'
    )

    inlines = [ServiceImages]

    list_filter = (
        'date_added',
        'date_updated'
    )

    list_editable = (
        'slug',
    )

    search_fields = (
        'title',
        'slug'
    )

    date_hierarchy = 'date_added'

    readonly_fields = (
        'date_added',
        'date_updated'
    )


    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff


    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff



@admin.register(TeamMembers)
class TeammembersAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'position',
        'status',
        'face_book_link',
        'instagram_link',
        'twitter_link',
        'github_link',
        'website_link',
        'date_joined',
        'updated_at'
    )

    list_filter = (
        'status',
    )

    list_editable = (
        'status',
    )

    search_fields = (
        'full_name',
    )

    date_hierarchy = 'date_joined'

    readonly_fields = (
        'date_joined',
        'updated_at'
    )


    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    



@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'link',
        'date_added'
    )

    list_filter = (
        'name',
    )

    date_hierarchy = 'date_added'

    search_fields = (
        'name',
    )

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff



@admin.register(ProjectsCategory)
class ProjectsCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'date_added',
        'updated_at'
    )    

    list_filter = (
        'date_added',
        'updated_at'
    )  

    list_editable = (
        'slug',
    )

    date_hierarchy = 'date_added'

    search_fields = (
        'title',
        'slug'
    )

    readonly_fields = (
        'date_added',
        'updated_at'
    )

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'category',
        'image',
        'customer_name',
        'project_type',
        'start_date',
        'end_date',
        'date_added',
        'date_updated'
    )

    list_filter = (
        'project_type',
        'category'
    )

    list_editable = (
        'slug',
    )

    search_fields = (
        'title',
        'customer_name'
    )

    date_hierarchy = 'date_added'

    readonly_fields = (
        'date_added',
        'date_updated'
    )

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    


@admin.register(CustomersSays)
class CustomersSaysAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'image',
        'date_added',
        'updated_at'
    )

    inlines = [SaysDescriptionAdmin]

    list_filter = (
        'date_added',
        'updated_at'
    )

    search_fields = (
        'full_name',
    )

    date_hierarchy = 'date_added'


    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff



@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'image',
        'is_free',
        'price',
        'is_sale',
        'sale_price',
        'date_added',
        'updated_at'
    )

    inlines = [PackageEpisodeAdmin, PackageCommentsAdmin]

    list_editable = (
        'slug',
    )

    list_filter = (
        'is_free',
        'is_sale',
        'date_added',
        'updated_at'
    )

    date_hierarchy = 'date_added'

    search_fields = (
        'title',
    )

    readonly_fields = (
        'date_added',
        'updated_at'
    )

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    



@admin.register(BlogCategories)
class BlogCategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'upload_at',
        'updated_at'
    )

    list_editable = (
        'slug',
    )

    list_filter = (
        'upload_at',
        'updated_at'
    )

    search_fields = (
        'title',
    )

    date_hierarchy = 'upload_at'

    readonly_fields = (
        'upload_at',
        'updated_at'
    )

    
    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    



@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'image',
        'category',
        'upload_at',
        'updated_at'
    )

    list_filter = (
        'category',
        'upload_at',
        'updated_at'
    )

    list_editable = (
        'slug',
    )

    date_hierarchy = 'upload_at'

    search_fields = (
        'title',
        'slug'
    )

    readonly_fields = (
        'upload_at',
        'updated_at'
    )

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    



@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'request_type',
        'subject',
        'created_at',
        'status'
    )

    list_filter = (
        'request_type',
        'status'
    )

    list_editable = (
        'status',
    )

    search_fields = (
        'full_name',
        'email'
    )

    date_hierarchy = 'created_at'

    
    readonly_fields = (
        'full_name',
        'email',
        'phone_number',
        'request_type',
        'subject',
        'created_at',
    )

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.is_staff:
            return self.readonly_fields + tuple(field.name for field in self.opts.local_fields if field.name != 'status')
        return self.readonly_fields
    


    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    



@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'slug'
    )

    inlines = [PurchasedPackagesAdmin]

    list_filter = (
        'user',
    )

    search_fields = (
        'user',
        'slug'
    )

    readonly_fields = (
        'user',
        'slug'
    )

    def has_add_permission(self, request):
        return request.user.is_superuser 
    

    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser  
    

    def has_change_permission(self, request, obj =None):
        return request.user.is_superuser  
    

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    

    def has_view_permission(self, request, obj =None):
        return request.user.is_superuser or request.user.is_staff
    