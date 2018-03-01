(function(){
    "use strict";
    angular.module("ApendiceApp")
        .controller("ArticleListCtrl", ['articleservice', ArticleListCtrl]);

    function ArticleListCtrl(articleservice){
        var self = this;

        self.listar_articulos=function(kword){
          articleservice.lista_articulos(kword)
            .then(function(response){
              self.articulos = response.data;
            });
        }

        //metodo que atualiza el estado de un articulo
        self.actualizar_published = function(articulo){
          console.log('----'+articulo.published);
          var json = {
            'pk':articulo.pk,
          }
          console.log(articleservice.update__published_article(json));
          window.location.href = '/articulo-listar/2';
        };
    }
}());
