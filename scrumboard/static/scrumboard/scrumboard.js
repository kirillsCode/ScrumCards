(function(){
    'use strict';

    angular.module('scrumboard.demo', [])
        .controller('ScrumboardController', ['$scope', '$http', ScrumboardController]);

    function ScrumboardController($scope, $http) {
        $scope.add_title = function(list, title) {
            var card = {
                title: title,
                list: list.id
            };
            $http.post('scrumboard/cards/', card)
                .then(function(response){

                        list.cards.push(response.data);
                },
                    function(){
                        alert('Could not create a card');
                    }
                )
            ;

        };

        $scope.edit = false;
        $scope.data = [];

        $http.get('/scrumboard/lists/').then(function(response){
           $scope.data = response.data;
        });
    }
}());