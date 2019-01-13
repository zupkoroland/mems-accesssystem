<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="/angularjs/angular.js"></script>
    <script type="text/javascript">
        var app = angular.module('angApp', []);

        app.controller('angCtrl', function ($http, $scope, $interval){
            function getData() {
                $http({
                    method: 'GET',
                    url: 'db.php',
                }).then(function(result){
                    $scope.data = result.data;
                })
            }

            $interval(getData, 1000);
        });
    </script>
    <title>Document</title>
</head>
<body ng-app="angApp" ng-controller="angCtrl" ng-cloak>
    <table border="1px">
        <thead>
            <tr>    
                <th>CardID</th>
                <th>Name</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody>
            <tr ng-repeat="item in data">
                <td>{{item.card}}</td>
                <td>{{item.name}}</td>
                <td>{{item.date}}</td>
            </tr>
        </tbody>
    </table>
</body>
</html>