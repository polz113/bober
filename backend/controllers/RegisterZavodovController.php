<?php

class RegisterZavodovController extends Controller
{
	public function actionIndex()
	{
        
	}
    
    public function actionSync() {
        include_once dirname(__FILE__).'/../components/RegisterZavodov/RegisterZavodov.php';
        header('Content-Type: text/html; charset=utf-8');
        RegisterZavodov::SyncZavodiWhereKategorijaActive();
    }
    
    public function actionSyncCategories() {
        include_once dirname(__FILE__).'/../components/RegisterZavodov/RegisterZavodov.php';
        header('Content-Type: text/html; charset=utf-8');
        RegisterZavodov::SyncZavodiKategorije();
    }

}

?>