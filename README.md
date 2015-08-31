# django-context-variables
Simple utility to help make declarative class-based views in Django


Each method on a CBV decorated with `context_variable` is evaluated once
per instance (==request) by the `get_context_variables` function and added
to the template's context.


##Usage
views.py:

    class MyCBV(TemplateView):
        template_name = "my_template.html"

        def get_context_data(self, **kwargs):
            return get_context_variables(self)

        @context_variable
        def page(self):
            return get_object_or_404(MyModel, self.kwargs.get('page_id'))

        @context_variable
        def page_title(self):
            return '%s - My Site' % self.page.title

my_template.html:

    <html>
        <title>{{ page_title }}</title>
        <body>
            {{ page.content }}
        </body>
    </html>
