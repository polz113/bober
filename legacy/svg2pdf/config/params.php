<?php
date_default_timezone_set('Europe/Ljubljana');
// this contains the application parameters that can be maintained via GUI
return array(
	// this is displayed in the header section
	'title'=>'SVG 2 PDF Converter',
	// this is used in error pages
	'adminEmail'=>'dean@comcode.si',
	// the copyright information displayed in the footer section
	'copyrightInfo'=>'Copyright &copy; 2013'.(date('Y') != 2013 ? '-'.date('Y') : '').' by COMCODE d.o.o.',
);
