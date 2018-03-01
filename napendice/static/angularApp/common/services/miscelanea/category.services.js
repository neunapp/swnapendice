(function(){
    "use strict"
    angular.module("common.services")
        .factory("categoryservice",categoryservice)
        function categoryservice($http){
          var self = {};

          //servicio que recupera lista de temas por buscador
          self.listar_category = function(){
            return  $http.get("/api/listar_categoria/");
          }

          return self;
        }
}());
