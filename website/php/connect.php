<?php

// Creates a connection to MYSQL.
function connect() {

    $DB_HOST = "localhost";
    $DB_USERNAME = "root";
    $DB_PASSWORD = "root"; 
    $DB_DATABASE = "capstone";

    $conn = new mysqli($DB_HOST, $DB_USERNAME, $DB_PASSWORD, $DB_DATABASE);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    return $conn;
}

// Terminates the connection to MYSQL.
function close_connection($conn) {
    $conn->close();
}

?>