(function(){
    "use strict";
    angular.module("ApendiceApp")
        .controller("ArticleAddCtrl", ['articleservice','categoryservice','textAngularManager', ArticleAddCtrl]);

    function ArticleAddCtrl(articleservice,categoryservice,textAngularManager){
        var self = this;

        self.tags = [];
        self.mensaje = '';
        self.show_home = false;

        //text angular conf
        self.orightml = '<h3>Ingrese Contenido Aqui</h3>';
        self.htmlcontent = self.orightml;
        self.disabled = false;

        //funcion que recupera categorias
        self.listar_categoria = function(){
          categoryservice.listar_category()
            .then(function(response){
              self.categories = response.data;
            });
        }

        //funcion que agrega tags
        self.add_tag = function(keyEvent){
          if (keyEvent.which === 13){
            //verificasmos que no exista
            var existe = false;
            for (var i = 0; i < self.tags.length; i++) {
              if (self.tags[i]== self.tag) {
                existe=true;
              }
            }
            if (!existe) {
              self.tags.push(self.tag);
              self.tag = "";
            }
          }
        };

        //funcion que quita tag
        self.delete_tag = function(tag){
          var indexof = 0
          for (var i = 0; i < self.tags.length; i++) {
            if (self.tags[i] == tag) {
              indexof = i;
            }
          }
          self.tags.splice(indexof,1);
        };

        //funcion que realiza validaciones
        self.validations = function(){
          var valido = false;
          if (self.category == null) {
            self.mensaje = 'Selcciones una Categoria';
          }
          else {
            self.mensaje = '';
            valido = true;
          }
          //
          if (self.type_article == null) {
            self.mensaje = 'Selcciones una Tipo de Articulo';
          }
          else {
            self.mensaje = '';
            valido = true;
          }
          return valido;
        }

        //funcion para enviar el json al servidor
        self.agregar_articulo = function(flat){
          //creamos el json a enviar
          if (flat == "0") {
            self.published = true;
          }
          else {
            self.published = false;
          }

          //verificamos si existe un tag
          if (self.tags.length < 1) {
              self.tags.push('peru')
          }
          //
          if (self.validations()) {
            var json = {
              'category':self.category.name,
              'title':self.title,
              'description':self.description,
              'type_article':self.type_article.name,
              'city':self.city,
              'published':self.published,
              'content':self.htmlcontent,
              'image':self.image,
              'credits_image':self.credits_image,
              'show_home':self.show_home,
              'credits_article':self.credits_article,
              'tags':self.tags,
            };
            //peticion al servidor
            console.log(articleservice.add_article(json));
            //proceso completado
            console.log('---');
            window.location.href = '/articulo-listar/2';
          }
        }
    }
}());
