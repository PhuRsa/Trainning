<?php 
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=2.0">
    <style>
    body {
        background-color: rgba(0, 0, 0,0.9);
    }
    .content,.file-name{
        border: 1px solid #ccc;
        padding: 10px;
        margin-top: 10px;
        background-color: grey;
    }
    h2,h3,h4{
        color: red;
    }
    textarea{
        background-color: grey;
        color: red;
    }
    </style>
    <title>NOTE</title>
</head>
<body>
    <h2>Write You Note here:</h2>
    <form method="post">
    <input name="name" id="name" type="text" placeholder="Your Name">
    <button type="submit">submit</button>
    <br>
    <textarea name="note" id="note" cols="50" rows="10" placeholder="Write something here"></textarea>
    <br>
    <button type="submit">Write</button>
    </form>
</body>
</html>

<?php 
if(isset($_POST['name']) && $_POST['name']!==''){
    $_SESSION['name']=$_POST['name'];
}else if( $_SESSION['name']==''){
    die("<h2>Input Name First</h2>");
}
if(isset($_POST["note"]) && isset($_SESSION['name']) && $_POST['note']!=''){
    $name=$_SESSION['name'];
    $note = $_POST["note"];
    $dir_name= sha1($name);
    $filename = $name."_".md5(rand()).'.txt';
    shell_exec("cd /var/www/html/notes/ ;mkdir $dir_name");
    shell_exec("echo \"$note\" > /var/www/html/notes/$dir_name/$filename");
    $result = shell_exec("cat /var/www/html/notes/$dir_name/$filename");
    echo "<h3>$name content note:</h3>";
    echo '<div class="content">' .$result. '</div>';
}else if(isset($_SESSION['name'])){
    $name=$_SESSION["name"];
    $dir_name=sha1($name);
    $result = shell_exec("ls notes/$dir_name");
    echo "<h3>List file $name Note:</h3>";
    echo "<h4>Note save at ./notes/$dir_name/name_file</h4>";
    echo '<div class="file-name">' .$result. '</div>';
} 
?>
