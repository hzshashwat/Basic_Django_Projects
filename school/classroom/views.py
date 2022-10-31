from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    #SUCCESS URL
    #URL NOT A template.html
    success_url = reverse_lazy('classroom:thankyou')
    #success_url = '/classroom/thank_you/'

    #what to do with the form?
    #ContactForm(request.POST)
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:thankyou')

class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'
    #queryset = Teacher.objects.order_by('first_name').filter(subject = 'Django')

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:listteacher')

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:listteacher')