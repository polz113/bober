<div class="navbar navbar-inverse navbar-fixed-top">
    <div class="navbar-inner">
        <div class="container">
            <?php
            $superuser = Generic::isSuperAdmin();
            $user_role = Generic::getUserRole();

            $is_coordinator = false;
            if ($user_role >= 5) {
                $is_coordinator = Generic::isCoordinator();
            }
            $selectedCompany = null;

            if (Yii::app()->user->getState("currentCompany")) {
                // s$selectedCompany = Company::model()->findByPk(Yii::app()->user->getState("currentCompany"));
            }

            $leftMenu = array();
            $rightMenu = array();

            $showSystem = false;
            if ($superuser == 1) {
                $showSystem = true;
            }

            if ($user_role != null && $user_role > 0) {
                if ($superuser == 0) {
                    if ($user_role == 10) {
                        $country_admin = Country::model()->search();
                        $showSystem = true;
                    }
                    /*
                      $modelData = Company::model()->search();

                      foreach ($modelData->getData() as $company)
                      {
                      $clabel = $company->name;
                      $curl = '/index.php/site/switchCompany/'.$company->id;
                      $cactive = false;
                      $cadmin = CompanyUser::model()->find('company_id=:ci and user_id=:ui and is_admin=1', array('ci' => $company->id, ':ui' => Yii::app()->user->id)) != null;

                      if ($selectedCompany != null &&
                      $selectedCompany->id == $company->id)
                      {
                      $cactive = true;
                      }

                      if ($cadmin)
                      {
                      $clabel = '<i class="icon-star-empty"></i>'.$clabel;
                      }

                      $leftMenu[] = array('label' => $clabel, 'url' => $curl, 'active' => $cactive);
                      } */
                }

                $rightMenu = array(
                    array('label' => Yii::t('app', 'home'), 'url' => array('/site/index')),
                    // array('label'=>Yii::t('app', 'webshops'), 'url'=>array('/webshop/admin')),
                    // array('label'=>Yii::t('app', 'products'), 'url'=>array('/product/admin')),
                    // array('label'=>Yii::t('app', 'categories'), 'url'=>array('/category/admin')),
                    /*
                      array('label'=>Yii::t('app', 'settings').' <span class="caret"></span>', 'url'=>'#','itemOptions'=>array('class'=>'dropdown','tabindex'=>"-1"),'linkOptions'=>array('class'=>'dropdown-toggle','data-toggle'=>"dropdown"),
                      'items'=>array(
                      array('label'=>Yii::t('app', 'company_users'), 'url'=>'/index.php/companyUser/admin'),
                      array('label'=>Yii::t('app', 'attributes'), 'url'=>'/index.php/attribute/admin'),
                      array('label'=>Yii::t('app', 'attributegroups'), 'url'=>'/index.php/attributeGroup/admin'),
                      array('label'=>Yii::t('app', 'manufacturers'), 'url'=>'/index.php/manufacturer/admin'),
                      array('label'=>Yii::t('app', 'distributers'), 'url'=>'/index.php/distributer/admin'),
                      array('label'=>Yii::t('app', 'attributes_native'), 'url'=>'/index.php/attributeNative/admin'),
                      array('label'=>Yii::t('app', 'categories_native'), 'url'=>'/index.php/categoryNative/admin'),
                      )),
                     */
                    array('label' => Yii::t('app', 'Competition') . ' <span class="caret"></span>', 'url' => '#', /* 'visible'=>$superuser==1, */ 'itemOptions' => array('class' => 'dropdown', 'tabindex' => "-1"), 'linkOptions' => array('class' => 'dropdown-toggle', 'data-toggle' => "dropdown"),
                        'items' => array(
                            array('label' => Yii::t('app', 'Competitions'), 'url' => '/index.php/competition/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Competitors'), 'url' => '/index.php/competitionUser/admin', 'visible' => ($user_role >= 5)),
                            array('label' => Yii::t('app', 'Competition Awards'), 'url' => '/index.php/competitionUserAwards/admin', 'visible' => $superuser),
                            array('label' => Yii::t('app', 'Manage Competition Questions'), 'url' => '/index.php/competitionQuestion/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Manage Competition Question Categories'), 'url' => '/index.php/competitionQuestionCategory/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Register School For Competition'), 'url' => '/index.php/competitionCategorySchool/admin', 'visible' => ($user_role > 5 || $is_coordinator)),
                            array('label' => Yii::t('app', 'Register Competitors For Competition'), 'url' => '/index.php/competitionCategorySchoolMentor/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Manage shared files'), 'url' => '/index.php/shared/index', 'visible' => ($user_role >= 5)),
                        )),
                    array('label' => Yii::t('app', 'system') . ' <span class="caret"></span>', 'url' => '#', 'visible' => $showSystem, 'itemOptions' => array('class' => 'dropdown', 'tabindex' => "-1"), 'linkOptions' => array('class' => 'dropdown-toggle', 'data-toggle' => "dropdown"),
                        'items' => array(
                            array('label' => Yii::t('app', 'countries'), 'url' => '/index.php/country/admin', 'visible' => ($superuser == 1)),
                            array('label' => Yii::t('app', 'languages'), 'url' => '/index.php/language/admin', 'visible' => ($superuser == 1)),
                            array('label' => Yii::t('app', 'municipalities'), 'url' => '/index.php/municipality/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'users'), 'url' => '/index.php/user/admin', 'visible' => ($superuser == 1)),
                            array('label' => Yii::t('app', 'regions'), 'url' => '/index.php/region/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Competition Category'), 'url' => '/index.php/competitionCategory/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Manage Question Difficulties'), 'url' => '/index.php/competitionQuestionDifficulty/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Manage Country Administrators'), 'url' => '/index.php/countryAdministrator/admin', 'visible' => ($superuser == 1)),
                            array('label' => Yii::t('app', 'Manage Schools'), 'url' => '/index.php/school/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Manage Questions'), 'url' => '/index.php/question/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Manage Question Resources'), 'url' => '/index.php/questionResource/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Manage School Mentors'), 'url' => '/index.php/schoolMentor/admin', 'visible' => ($user_role >= 10)),
                            array('label' => Yii::t('app', 'Manage School Mentor Confirmations'), 'url' => '/index.php/schoolMentorConfirmation/admin', 'visible' => ($user_role >= 10)),
                        )),
                    array('label' => Yii::t('app', 'DEV') . ' <span class="caret"></span>', 'url' => '#', 'visible' => $_SERVER['SERVER_ADDR'] == "127.0.0.1", 'itemOptions' => array('class' => 'dropdown', 'tabindex' => "-1"), 'linkOptions' => array('class' => 'dropdown-toggle', 'data-toggle' => "dropdown"),
                        'items' => array(
                            array('label' => Yii::t('app', 'forms'), 'url' => array('/site/page', 'view' => 'forms')),
                            array('label' => Yii::t('app', 'tables'), 'url' => array('/site/page', 'view' => 'tables')),
                            array('label' => Yii::t('app', 'interface'), 'url' => array('/site/page', 'view' => 'interface')),
                            array('label' => Yii::t('app', 'typography'), 'url' => array('/site/page', 'view' => 'typography')),
                        )),
                );
                ?>
                <div class="nav-collapse">
                    <?php
                    if ($superuser == 0 &&
                            count($leftMenu) > 0) {
                        $this->widget('zii.widgets.CMenu', array(
                            'htmlOptions' => array('class' => 'pull-left nav'),
                            'submenuHtmlOptions' => array('class' => 'dropdown-menu'),
                            'itemCssClass' => 'menuitem-company',
                            'encodeLabel' => false,
                            'items' => array(
                                array('label' => $selectedCompany->name . ' <span class="caret"></span>', 'url' => '#', 'itemOptions' => array('class' => 'dropdown', 'tabindex' => "-1"), 'linkOptions' => array('class' => 'dropdown-toggle', 'data-toggle' => "dropdown"),
                                    'items' => $leftMenu
                                ),
                            ),
                        ));
                    }
                    ?>
                </div>

                <div class="btn-group pull-right">
                    <a class="btn btn-primary" href="#" onclick="return false;"><i class="icon-user icon-white"></i> <?php echo Yii::app()->user->name ?></a>
                    <a class="btn btn-primary dropdown-toggle" data-toggle="dropdown" href="#" title="<?php echo Yii::app()->user->name ?>"><span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li class="menuitem-user"><a onclick="showModalWindow('<?php echo Yii::t('app', 'My profile'); ?>', '<?php echo CController::createUrl('/user/profile/edit/ajax') ?>', {'formId': 'profile-form'})"><i class="icon-user"></i> <?php echo Yii::t('app', 'my_profile') ?></a></li>
                        <li class="menuitem-user"><a href="<?php echo CController::createUrl('/user/profile/changepassword') ?>"><i class="icon-user"></i> <?php echo Yii::t('app', 'Change Password') ?></a></li>
                        <?php
                        /* <li class="menuitem-user"><a onclick="showModalWindow('<?php echo Yii::t('app', 'create_company'); ?>', '<?php echo CController::createUrl('/company/create/ajax') ?>', { 'formId': 'company-formonly' })"><i class="icon-briefcase"></i> <?php echo Yii::t('app', 'new_company') ?></a></li> */
                        ?>
                        <li class="divider"></li>
                        <li class="menuitem-user"><a href="/index.php/site/logout"><i class="icon-remove-sign"></i> <?php echo Yii::t('app', 'logout') ?></a></li>
                    </ul>
                </div>

                <div class="nav-collapse">
                    <?php
                    $this->widget('zii.widgets.CMenu', array(
                        'htmlOptions' => array('class' => 'pull-right nav'),
                        'submenuHtmlOptions' => array('class' => 'dropdown-menu'),
                        'itemCssClass' => 'menuitem-general',
                        'encodeLabel' => false,
                        'items' => $rightMenu,
                    ));
                    ?>
                </div>

            <?php } ?>
        </div>
    </div>
</div>
<div class="subnav navbar navbar-fixed-top">
    <div class="navbar-inner">
        <div class="container">

        </div><!-- container -->
    </div><!-- navbar-inner -->
</div><!-- subnav -->