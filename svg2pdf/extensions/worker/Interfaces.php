<?php

interface IWorkerApplication
{
	/**
	 * @abstract
	 * @return IWorkerDaemon
	 */
	public function getWorker();
	/**
	 * @abstract
	 * @param IWorkerDaemon $worker
	 */
	public function setWorker($worker);
	
}

interface IWorkerDaemon extends IApplicationComponent
{
	/**
	 * @abstract
	 */
	public function run();
}