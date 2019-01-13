<?php
    $servername = "localhost";
    $username = "pi";
    $password = "root";
    $dbname = "mydb";

    $conn = new mysqli($servername, $username, $password, $dbname);

    $sql = "SELECT s.card, s.date, c.name FROM logs s INNER JOIN cards c ON c.card = s.card ORDER BY date DESC";
    $result = $conn->query($sql);

    $rows = array();

    while($row = $result->fetch_assoc()) {
        $rows[] = $row;
    }

    print json_encode($rows);

    $conn->close();
?>