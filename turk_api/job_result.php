<?php
  $con = mysql_connect("127.0.0.1:3306","root","");
  mysql_select_db("wine", $con);
  if($_SERVER['REQUEST_METHOD'] === 'POST'){ 
    $jobId = mysql_real_escape_string($_POST["jobId"]);
    $name = mysql_real_escape_string($_POST["name"]);
    $year = mysql_real_escape_string($_POST["year"]);
    $winery = mysql_real_escape_string($_POST["winery"]);
    $query = "UPDATE jobs SET name='$name', year=$year, winery='$winery',".
             "status='COMPLETED' WHERE id=$jobId LIMIT 1;";
    mysql_query($query);
    echo mysql_error();
    die("Thank you.");
  } elseif (array_key_exists("jobId", $_GET)) {
    $jobId = mysql_real_escape_string($_GET["jobId"]);
    $query = "SELECT name, year, winery FROM jobs WHERE id = $jobId AND status = 'COMPLETED'";
    $result = mysql_query($query);
    if (mysql_num_rows($result)){
      $row = mysql_fetch_assoc($result);
      $name = $row["name"];
      $year = $row["year"];
      $winery = $row["winery"];
      die("$name, $year, $winery");
    } 
  } 
?>
<html>
  <head>
    <script type="text/javascript">
      setTimeout(window.location.reload.bind(window.location), 250);
    </script>
  <body>
    Waiting for result...
  </body>
  </head>
</html>
