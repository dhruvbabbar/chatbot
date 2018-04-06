from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe

def calendar(request, year, month):
    my_workouts = Workouts.objects.order_by('my_date').filter(
    my_date__year=year, my_date__month=month
  )
    cal = WorkoutCalendar(my_workouts).formatmonth(year, month)
    return render_to_response('my_template.html', {'calendar': mark_safe(cal),})