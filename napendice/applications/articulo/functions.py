from .models import Article
from django.contrib.auth.models import User


#funcion para actualizar estados de notas
def update_type_article(process,type_article):
    if (process == 'save'):
        if type_article == 'F':
            #recuperamos ultima portada y actualizamos a destacado
            articulo = Article.objects.filter(
                published=True,
                type_article='F',
            ).order_by('-created')[0]
            articulo.type_article="O"
            articulo.save()
        elif type_article == 'O':
            #recuperamos ultios 3 destacados
            articulo = Article.objects.filter(
                published=True,
                type_article='O'
            ).order_by('-created')[:3][2]
            #actualizmos el destacado mas antiguo
            articulo.type_article = 'S'
            articulo.save()
        else:
            print('ingreso standar')
    else:
        if type_article == 'F':
            #recuperamos ultima destacado y actualizamos a portada
            articulo = Article.objects.filter(
                published=True,
                type_article='O',
            ).order_by('-created')[0]
            articulo.type_article="F"
            articulo.save()

    return True
