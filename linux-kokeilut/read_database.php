GNU nano 7.2                                                                     read_database.php *                                                                             <?php
$servername = "172.20.241.42";
$username = "dbaccess_ro"; // katso discordin pinned-viesteistä
$password = "1111"; // katso discordin pinned-viesteistä
$dbname = "measurements";
$groupid = 17; // oma groupid

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
        }

$sql = "SELECT * FROM rawdata";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
   while($row = $result->fetch_assoc()) {
      echo "Time: " . $row["timestamp"] . " - groupid: " . $row["groupid"] . " - from_mac: " . $row["from_mac"] . " - to_mac: " . $row["to_mac"] . " - X: " . $row["x"] . " - Y: ">}

$conn->close();
?>