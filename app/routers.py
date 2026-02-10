from rest_framework.routers import DefaultRouter
from .views import PatientViewsets , TestViewSets , ReportViewsets

router = DefaultRouter()
router.register(r'patients', PatientViewsets, basename='patients')
router.register(r'tests', TestViewSets, basename='tests')
router.register(r'reports', ReportViewsets, basename='reports')


