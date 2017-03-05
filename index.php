<?php
	$json = json_decode(file_get_contents("phone.txt"), true);
	header("content-type: text/xml");
    echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>
<Response>
	<?php
	if ($json['command'] == 'conference') {
		echo('<Dial>' . $json['number'] . '</Dial>');
	} else {
		echo('<Say>' . $json['message'] . '</Say>');
	}
    ?>
</Response>