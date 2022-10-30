# class MessageView(CreateView):
#     template_name = 'exercises_app/message.html'
#     form_class = MessageForm
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         cd = form.cleaned_data
#         subject = cd['subject']
#         content = cd['content']
#         to = cd['to']
#         from_u = cd['from_u']
#         Message.objects.create(subject=subject, content=content, to=to, from_u=from_u)
#         return super().form_valid(form)



# REJESTRACJA I LOGOWANIE W TYM SAMYM CZASIE
# USUWANIE LOGINÓW Z BAZY DANYCH