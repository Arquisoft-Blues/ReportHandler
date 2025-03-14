from ..models import Report

def get_reports():
    queryset = Report.objects.all().order_by('-created_at')[:10]
    return (queryset)

def create_report(form):
    report = form.save()
    report.save()
    return ()