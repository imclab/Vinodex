<html>
  <body>
<?php
  include("db_connect.php");
  if($_SERVER['REQUEST_METHOD'] === 'POST'){ 
    $jobId = mysql_real_escape_string($_POST["jobId"]);
    $name = mysql_real_escape_string($_POST["name"]);
    $year = mysql_real_escape_string($_POST["year"]);
    $winery = mysql_real_escape_string($_POST["winery"]);
    $query = "UPDATE jobs SET name='$name', year=$year, winery='$winery',".
             "status='COMPLETED' WHERE id=$jobId LIMIT 1;";
    mysql_query($query);
  } elseif (array_key_exists("jobId", $_GET)) {
    $jobId = mysql_real_escape_string($_GET["jobId"]);
    $query = "SELECT name, year, winery FROM jobs WHERE id = $jobId AND status = 'COMPLETED'";
    $result = mysql_query($query);
    if (mysql_num_rows($result)){
      $row = mysql_fetch_assoc($result);
      $name = $row["name"];
      $year = $row["year"];
      $winery = $row["winery"];
      echo "$name, $year, $winery";
    } else {
      echo "No results at this time";
    }
  } 
?>
