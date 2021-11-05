        var task = {
            load: function (randomSeed, mode) { task.randomizeAnswers(randomSeed);  },
            unload: function () { return true; },
            getAnswer: function () {
                var answer = jQuery("input[name='answer']:checked");
                if (answer.length > 0) { return jQuery(answer[0]).val(); }
                else { return ''; }
            },
            reloadAnswer: function (answer) {
                if (answer) {
                    jQuery("input[name='answer']").each(function () {
                        if (jQuery(this).val() === answer) {
                            jQuery(this).prop('checked', true);
                        }}); }
                else { jQuery("input[name='answer']").prop('checked', false); }
            },
            displayMessage: function (type, html, isOptional) {
                if (type === 'validate') {
                } else if (type === 'cancel') {
                    if (confirm('Ali želite poenostaviti odgovore?')) {
                        taskReloadAnswer('');
                    }
                } else if (type === 'saved') {}
                else if (type === 'changed') {}
                else if (type === 'deleted') {}
            },
            randomizeAnswers: function (seed) { task.shuffle("answers", seed); },
            shuffle: function (tblName, seed) {
                var list = jQuery("#" + tblName + " > .answer");
                jQuery("#" + tblName + " > .answer").remove();
                var rand = new task.RandomNumberGenerator(seed);
                for (var j, x, i = list.length; i>0; i--) {
                    j = parseInt(rand.next() * i);
                    if (j < 0) j = 0;
                    if (j >= i) j =i-1;
                    x = list[i-1]; list[i-1] = list[j]; list[j] = x
                }
                var answers = $("#" + tblName);
                for (i = 0; i < list.length; i++) {
                    answers.append(list[i]);
                }
            },
            nextRandomNumber: function () {
                var hi = this.seed / this.Q;
                var lo = this.seed % this.Q;
                var test = this.A * lo - this.R * hi;
                if (test > 0) {
                    this.seed = test;
                } else {
                    this.seed = test + this.M;
                }
                return (this.seed * this.oneOverM);
            },
            RandomNumberGenerator: function (s) {
                var d = new Date();
                this.seed = s;
                this.A = 48271;
                this.M = 2147483647;
                this.Q = this.M / this.A;
                this.R = this.M % this.A;
                this.oneOverM = 1.0 / this.M;
                this.next = task.nextRandomNumber;
                return this;
            }
        };
