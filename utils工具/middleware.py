class UrlPathRecordMiddleware(object):
    exclude = ['/login/', '/register/', '/login_out/']
    def process_view(self, request, view_func, *args, **kwargs):
        if request.path not in UrlPathRecordMiddleware.exclude and not request.is_ajax():
            request.session['prev_url'] = request.path
