(function(){
    "use strict";
    angular.module("ApendiceApp")
        .controller("ArticleUpdateCtrl", ['articleservice','categoryservice','textAngularManager', ArticleUpdateCtrl]);

    function ArticleUpdateCtrl(articleservice,categoryservice,textAngularManager){
        var self = this;

        self.tags = [];
        self.show_home = false;
        self.pk = '';

        //text angular conf
        self.disabled = false;


        //INICIALIZAMOS LO VALORES
        self.inicializar_articulo = function(kword){
            //recuperamos el objeto
            var articulo;
            articleservice.get_articulo(kword)
              .then(function(response){
                articulo = response.data;
                //inicializamos
                self.category = articulo.category;
                self.title = articulo.title;
                self.description = articulo.description;
                self.type_article = articulo.type_article;
                self.city = articulo.city;
                self.published = articulo.published;
                self.htmlcontent= articulo.content;
                self.image = articulo.image;
                self.credits_image = articulo.credits_image;
                self.show_home = articulo.show_home;
                self.credits_article = articulo.credits_article;
                self.tags = articulo.tag;
                self.pk = kword;
                //inicializamos los tag
                // for (var i = 0; i < articulo.tag.length; i++) {
                //   //recuperamos el tag
                //
                //   self.tags.push(articulo.tag[i].name)
                // }
              });

        }

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

        //funcion para enviar el json al servidor
        self.agregar_articulo = function(flat){
          //creamos el json a enviar
          var json = {
            'pk':parseInt(self.pk),
            'category':self.category,
            'title':self.title,
            'description':self.description,
            'type_article':self.type_article,
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
          console.log(articleservice.update_article(json));
          //proceso completado
          console.log(self.pk);
          console.log('---');
          window.location.href = '/articulo-listar/2';
        }
    }
}());
