
var API_URL = 'http://127.0.0.1:8000/agenda/'

angular.module('app.controllers', [])
  
.controller('agendaCtrl', ['$scope', '$http', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $http) {   

    $scope.result = "";
    $http.get(API_URL)
      .success(function(data, status, headers,config){
        console.log('data success');
        console.log(data); 
        $scope.result = data; 
      })
      .error(function(data, status, headers,config){
        console.log('data error');
      })
      .then(function(result){
        things = result.data;
      });
    
}])
   
.controller('cadastroCtrl', ['$scope', '$http', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $http) {

  $scope.save = function(cadastro) { 
     $http.post(API_URL, cadastro)
      .success(function(data, status, headers,config){
        console.log('data success');
        console.log(data); 
        $scope.result = data; 
      })
      .error(function(data, status, headers,config){
        console.log('data error');
      })
      .then(function(result){
        things = result.data;
      });
  };
}])
   
.controller('sobreCtrl', ['$scope', '$http', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $http) {


}])



    