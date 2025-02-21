<?php
	header("Content-Type:text/html; charset=utf-8");
	// assign the POSTed data T to the variable Temp.
	$Temp=$_POST[T];
	// assign the POSTed data H to the variable Humi.
	$Humi=$_POST[H];
	// assign the POSTed data S to the variable SensorID.
	$SensorID=$_POST[S];
	// assign the POSTed data M to the variable Month.
	$Month=$_POST[M];
	// assign the POSTed data D to the variable Date.
	$Date=$_POST[D];

	// output information of SensorID, Temperature, Humidity, Month, Date
	echo 'Month:'.$Month. "\n";
	echo 'Date:'.$Date. "\n";
	echo 'Sensor:'.$SensorID."\n";
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

	// open the file and set it to write mode
	$fp = fopen('/home/pi/www-data/month.txt','w');
	// write Month into the file
	fwrite($fp, $Month);
	// close file
	fclose($fp);

	// open the file and set it to write mode
	$fp = fopen('/home/pi/www-data/date.txt','w');
	// write Date into the file
	fwrite($fp, $Date);
	// close file
	fclose($fp);
?>


