<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.5/angular.min.js"></script>
    <script type="text/javascript">
        //Angular modul létrehozása.
        var app = angular.module('angApp', []);
        
        
        //Az angular controller létrehozása
        app.controller('angCtrl', function ($http, $scope, $interval){
            
            //Az adatok lekérdezése GET-en keresztül $http-vel.
            function getData() {
                $http({
                    method: 'GET',
                    url: 'db.php',
                }).then(function(result){
                    $scope.data = result.data;
                })
            }
            
            //Lekérdezést másodpercenként elvégzi.
            $interval(getData, 1000);
        });
    </script>
    <title>Document</title>
</head>
<body ng-app="angApp" ng-controller="angCtrl" ng-cloak>
    <!--Adatok megjelenítéshez szükséges table tag-->
    <table border="1px">
        <thead>
            <tr>    
                <th>CardID</th>
                <th>Name</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody>
            <!-- Az angular repeat-el kilistázom a getData()-val kapott adatokat -->
            <tr ng-repeat="item in data">
                <td>{{item.card}}</td>
                <td>{{item.name}}</td>
                <td>{{item.date}}</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
