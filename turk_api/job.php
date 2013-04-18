<html>
  <body>
<?php
  include("db_connect.php");
  if(array_key_exists("imageUrl", $_POST)) {
    $imageUrl = mysql_real_escape_string($_POST["imageUrl"]);
    $query = "INSERT INTO jobs(imageUrl, status) VALUES('$imageUrl','IN_PROGRESS');";
    mysql_query($query, $con);
  } else {
    $result = mysql_query("SELECT id, imageUrl FROM jobs WHERE status = 'IN_PROGRESS';");
    if (!mysql_num_rows($result)){
      die("No Jobs!");
    }
    $row = mysql_fetch_assoc($result);
    $jobId = $row["id"];
    $imageUrl = $row["imageUrl"];
  }
?>
            <img src="<?php echo $imageUrl; ?>" />
            <form name="classify" action="job_result.php" method="POST">
              <input type="hidden" name="jobId" value = "<?php echo $jobId; ?>">
              <input type="text" name="name">Wine Name</input>
              <input type="text" name="year">Wine Year</input>
              <input type="text" name="winery">Winery</input>
              <input type="submit">Submit</input>
            </form>
  </body>
</html>
