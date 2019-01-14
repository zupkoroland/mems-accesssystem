<?php
    //Adatbázis kapcsolathoz szükséges adatok.
    $servername = "localhost";
    $username = "pi";
    $password = "root";
    $dbname = "mydb";

    //Adatbázis kapcsolat létrehozása.
    $conn = new mysqli($servername, $username, $password, $dbname);

    //Az SQL query.
    $sql = "SELECT s.card, s.date, c.name FROM logs s INNER JOIN cards c ON c.card = s.card ORDER BY date DESC";

    //A query futtatása.
    $result = $conn->query($sql);

    //Tömb létrehozása JSON küldéséhez.
    $rows = array();

    //Az adatbázisból kapott eredményeken while ciklussal végig futunk és az eredményeket eltároljuk a tömbbe.
    while($row = $result->fetch_assoc()) {
        $rows[] = $row;
    }
    
    //A tömb tartalmának átalakítása JSON formátumra.
    print json_encode($rows);

    //Adatbázis kapcsolat zárása.
    $conn->close();
?>
