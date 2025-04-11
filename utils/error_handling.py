from django.http import JsonResponse


def handle_not_found404(request, exception):
    """
    Custom 404 error handler.
    """
    return JsonResponse({'error': 'Page not found'}, status=404)

def handle_server_error500(request):
    """
    Custom 500 error handler.
    """
    return JsonResponse({'error': 'Internal server error'}, status=500)

def handle_bad_request400(request, exception):
    """
    Custom 400 error handler.
    """
    return JsonResponse({'error': 'Bad request'}, status=400)

def handle_permission_denied403(request, exception):
    """
    Custom 403 error handler.
    """
    return JsonResponse({'error': 'Permission denied'}, status=403)

def handle_method_not_allowed405(request, exception):
    """
    Custom 405 error handler.
    """
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def handle_not_acceptable406(request, exception):
    """
    Custom 406 error handler.
    """
    return JsonResponse({'error': 'Not acceptable'}, status=406)

def handle_conflict409(request, exception):
    """
    Custom 409 error handler.
    """
    return JsonResponse({'error': 'Conflict'}, status=409)

def handle_gone410(request, exception):
    """
    Custom 410 error handler.
    """
    return JsonResponse({'error': 'Gone'}, status=410)

