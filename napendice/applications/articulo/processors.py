from applications.miscelanea.models import Category


def category(request):
    '''
    processors para listar todas las categorias en header.html
    se va a inviar a todas los templates
    '''
    myCategorys = Category.objects.all()
    return {'myCategorys': myCategorys}
