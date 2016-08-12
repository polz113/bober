var grader = {
    /**
     * Function that validates user answer
     * 
     * @param Float randomSeed Value between 0...1
     * @param String answer    Answer in any format interacive task wants it
     * @param Integer minScore  Minimal score value
     * @param Integer maxScore  Maximum score value
     * 
     * @returns Integer Score of user answer of the task
     */
    gradeTask: function(randomSeed, answer, minScore, maxScore) {
        /* return value should be an integer between minScore and maxScore
         answer => string 
         minScore,maxScore => indicated the smallest and largest score that can be allocated to this task.
         */
        if (answer === 'Ponedeljek') {
            return 1;
        }
        return 0;
    }
};