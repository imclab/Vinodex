<?php
  include("db_connect.php");
  if(array_key_exists("imageUrl", $_POST)) {
    $imageUrl = mysql_real_escape_string($_POST["imageUrl"]);
    $query = "INSERT INTO jobs(imageUrl, status) VALUES('$imageUrl','IN_PROGRESS');";
    mysql_query($query, $con);
    $id = mysql_insert_id();
    header("Location: http://localhost:8888/job_result.php?jobId=$id");
    die();
  } else {
    $result = mysql_query("SELECT id, imageUrl FROM jobs WHERE status = 'IN_PROGRESS';");
    if (!mysql_num_rows($result)){
      header("HTTP/1.0 404 Not Found");
      die("No Jobs!");
    }
    $row = mysql_fetch_assoc($result);
    $jobId = $row["id"];
    $imageUrl = $row["imageUrl"];
  }
?>
<html>
  <body>
            <table><tr><td>
            <img src="<?php echo $imageUrl; ?>" style="width:300px;" />
            </td><td>
            <form name="classify" action="job_result.php" method="POST">
              <input type="hidden" name="jobId" value = "<?php echo $jobId; ?>">
              <input type="text" name="name">Wine Name</input><br />
              <input type="text" name="year">Wine Year</input><br />
              <input type="text" name="winery">Winery</input><br />
              <input type="submit" />
            </form></td></table>
  </body>
</html>
