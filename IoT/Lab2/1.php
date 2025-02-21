<?php
	header("Content-Type:text/html; charset=utf-8");
	
	// assign the POSTed data T to the variable Temp.
	$Temp=$_POST[T];
	// assign the POSTed data H to the variable Humi.
	$Humi=$_POST[H];
	// assign the POSTed data S to the variable SensorID.
	$SensorID=$_POST[S];

	// output information of SensorID, Temperature, Humidity
	echo ' Sensor:'.$SensorID."\n";
	echo 'Temperature:'.$Temp. "\n";
	echo 'Humidity:'.$Humi. "\n";

	// open the file and set it to write mode
	$fp = fopen('/home/pi/www-data/temp_'.$SensorID.'.txt','w');
	// write Temp into the file
	fwrite($fp, $Temp);
	// close file
	fclose($fp);

	// open the file and set it to write mode
	$fp = fopen('/home/pi/www-data/humi_'.$SensorID.'.txt','w');
	// write Humi into the file
	fwrite($fp, $Humi);
	// close file
	fclose($fp);
?>

