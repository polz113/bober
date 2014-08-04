<?php

// components/WidgetFactory.php

/**
 * Custom WidgetFactory class
 * Provides two new events:
 *  - onBeforeCreateWidget
 *  - onAfterCreateWidget
 *
 * Allows for advanced global widget alteration, going a step further than CWidgetFactory's
 * typical process which allows you to define default values for widgets.
 *
 * @author Jon Langevin (intel352) <jon@langevin.me>
 * @link https://gist.github.com/4513672
 */
class WidgetFactory extends CWidgetFactory
{

    /**
     * Raised right BEFORE a widget is created.
     * @param CEvent $event the event parameter
     */
    public function onBeforeCreateWidget(CEvent $event)
    {
        $this->raiseEvent('onBeforeCreateWidget',$event);
    }

    /**
     * Raised right AFTER a widget is created.
     * @param CEvent $event the event parameter
     */
    public function onAfterCreateWidget(CEvent $event)
    {
        $this->raiseEvent('onAfterCreateWidget',$event);
    }

    /**
     * Creates a new widget based on the given class name and initial properties.
     * @param CBaseController $owner the owner of the new widget
     * @param string $className the class name of the widget. This can also be a path alias (e.g. system.web.widgets.COutputCache)
     * @param array $properties the initial property values (name=>value) of the widget.
     * @return CWidget the newly created widget whose properties have been initialized with the given values.
     */
    public function createWidget($owner,$className,$properties=array())
    {
        if (! ($this->hasEventHandler('onBeforeCreateWidget') || $this->hasEventHandler('onAfterCreateWidget')))
            return parent::createWidget($owner, $className, $properties);

        $event=new WidgetEvent($this, $owner, $className, $properties);
        if ($this->hasEventHandler('onBeforeCreateWidget'))
            $this->raiseEvent('onBeforeCreateWidget', $event);
        $event->widget=parent::createWidget($owner, $className, $properties);
        if ($this->hasEventHandler('onAfterCreateWidget'))
            $this->raiseEvent('onAfterCreateWidget', $event);
        return $event->widget;
    }

}

class WidgetEvent extends CEvent
{
    /**
     * @var CBaseController Owner of the new widget
     */
    public $owner;

    /**
     * @var string Widget class name
     */
    public $className;

    /**
     * @var CWidget The newly created widget
     */
    public $widget;

    /**
     * Constructor.
     * @param WidgetFactory $sender The WidgetFactory instance
     * @param CBaseController $owner The owner of the new widget
     * @param string $className The class name of the widget. This can also be a path alias.
     * @param array $params The initial property values (name=>value) of the widget.
     */
    public function __construct(WidgetFactory $sender, CBaseController $owner, $className, array $params=array())
    {
        parent::__construct($sender, $params);
        $this->owner=$owner;
        $this->className=$className;
    }
}