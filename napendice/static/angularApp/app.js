(function(){
    var app = angular.module("ApendiceApp",
                                  ['ngCookies','common.services',
                                    'textAngular',
                                ])
        .config(
        function($interpolateProvider, $httpProvider) {
          $interpolateProvider.startSymbol('{$');
          $interpolateProvider.endSymbol('$}');
          //
          $httpProvider.defaults.withCredentials = true;
          $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
          $httpProvider.defaults.xsrfCookieName = 'csrftoken';
          $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        }
        ).run(function($http, $cookies){
          $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        });

}());
