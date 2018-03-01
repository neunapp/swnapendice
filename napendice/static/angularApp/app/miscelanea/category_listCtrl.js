(function(){
    "use strict";
    angular.module("ApendiceApp")
        .controller("ListarCategoryCtrl", ['categoryservice', ListarCategoryCtrl]);

    function ListarCategoryCtrl(categoryservice){
        var self = this;

        self.listar_categorias = function(){
          //peticion al servidor
          categoryservice.listar_category()
            .then(function(response){
              self.categorias = response.data;
            });
        }
    }
}());
