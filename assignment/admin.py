from django.contrib import admin

from .models import PublishAssignment, SubmitAssignment

# Register your models here.
class PublishAssignmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'assignment_name', 'due_date', 'created_at']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'teacher':
            kwargs['initial'] = request.user.id
        return super(PublishAssignmentAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


class SubmittedAssignmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'assignment', 'submitted_pdf_file', 'submission_date_time', 'given_mark',]
    list_filter = ('submission_date_time', )
    search_fields = ['student__id', 'assignment__assignment_name']

    def get_queryset(self, request):
        qs = super(SubmittedAssignmentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(student=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'student':
            kwargs['initial'] = request.user.id
        return super(SubmittedAssignmentAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )
    
    def add_view(self,request,extra_content=None):
        if request.user.groups.filter(name="Students").exists():
            self.exclude = ('given_mark', 'submission_date_time',)
            return super(SubmittedAssignmentAdmin,self).add_view(request)
        else:
            return super(SubmittedAssignmentAdmin,self).add_view(request)


    def change_view(self,request,object_id,extra_content=None):
        if request.user.groups.filter(name="Students").exists():
            self.exclude = ('given_mark', 'submission_date_time',)
            return super(SubmittedAssignmentAdmin,self).change_view(request,object_id)
        else:
            self.include = ('given_mark',)
            return super(SubmittedAssignmentAdmin,self).change_view(request,object_id)
        



admin.site.register(PublishAssignment, PublishAssignmentAdmin)
admin.site.register(SubmitAssignment, SubmittedAssignmentAdmin)