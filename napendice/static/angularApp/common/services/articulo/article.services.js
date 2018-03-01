(function(){
    "use strict"
    angular.module("common.services")
        .factory("articleservice",articleservice)
        function articleservice($http){
          var self = {};

          //servicio que recupera lista de temas por buscador
          self.add_article = function(json){
            return  $http.post("/api/articulo-nuevo/",json);
          }

          //servicio que actualiza un articulo
          self.update_article = function(json){
            return  $http.post("/api/articulo-update/",json);
          }

          //servicio que actualiza etado publicado un articulo
          self.update__published_article = function(json){
            return  $http.post("/api/articulo-update-published/",json);
          }

          //srvicio que recupera un articulo
          self.get_articulo = function(kword){
            return  $http.get("/api/articulo/retrive/"+kword+"/");
          }

          //servicio que lista artuclos por estado
          self.lista_articulos = function(kword){
            return  $http.get("/api/articulo/listar/"+kword+"/");
          }

          return self;
        }
}());
