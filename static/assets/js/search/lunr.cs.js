/**
 * export the module via AMD, CommonJS or as a browser global
 * Export code from https://github.com/umdjs/umd/blob/master/returnExports.js
 */
;(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(factory)
    } else if (typeof exports === 'object') {
        /**
         * Node. Does not work with strict CommonJS, but
         * only CommonJS-like environments that support module.exports,
         * like Node.
         */
        module.exports = factory()
    } else {
        // Browser globals (root is window)
        factory()(root.lunr);
    }
}(this, function () {
    /**
     * Just return a value to define the module export.
     * This example returns an object, but the module
     * can return a function as the exported value.
     */
    return function(lunr) {
        /* throw error if lunr is not yet included */
        if ('undefined' === typeof lunr) {
            throw new Error('Lunr is not present. Please include / require Lunr before this script.');
        }

        /* throw error if lunr stemmer support is not yet included */
        if ('undefined' === typeof lunr.stemmerSupport) {
            throw new Error('Lunr stemmer support is not present. Please include / require Lunr stemmer support before this script.');
        }

        /* register specific locale function */
        lunr.cs = function() {
            this.pipeline.reset();
            this.pipeline.add(
                lunr.cs.trimmer,
                lunr.cs.stopWordFilter,
                lunr.cs.stemmer
            );
        };

        /* lunr trimmer function */
        lunr.cs.wordCharacters = "A-Za-z\\xAA\\xBA\\xC0-\\xD6\\xD8-\\xF6\\xF8-\\u02B8\\u02E0-\\u02E4\\u1D00-\\u1D25\\u1D2C-\\u1D5C\\u1D62-\\u1D65\\u1D6B-\\u1D77\\u1D79-\\u1DBE\\u1E00-\\u1EFF\\u2071\\u207F\\u2090-\\u209C\\u212A\\u212B\\u2132\\u214E\\u2160-\\u2188\\u2C60-\\u2C7F\\uA722-\\uA787\\uA78B-\\uA7AD\\uA7B0-\\uA7B7\\uA7F7-\\uA7FF\\uAB30-\\uAB5A\\uAB5C-\\uAB64\\uFB00-\\uFB06\\uFF21-\\uFF3A\\uFF41-\\uFF5A\\xC1\\xE1\\u010C\\u010D\\u010E\\u010F\\u011A\\u011B\\xCD\\xED\\u0147\\u0148\\xD3\\xF3\\xD4\\xF4\\u0158\\u0159\\u0160\\u0161\\u0164\\u0165\\xDA\\xFA\\u016E\\u016F\\xDD\\xFD\\u017D\\u017E\\u0159\\u013E\\u0148";
        lunr.cs.trimmer = lunr.trimmerSupport.generateTrimmer(lunr.cs.wordCharacters);

        lunr.Pipeline.registerFunction(lunr.cs.trimmer, 'trimmer-cs');

        /* lunr stemmer function */
        lunr.cs.stemmer = (function() {
            /* create the wrapped stemmer object */
            var Among = lunr.stemmerSupport.Among,
                SnowballProgram = lunr.stemmerSupport.SnowballProgram,
                st = new function CzechStemmer() {
                    var a_0 = [new Among("ce", -1, 1), new Among("ze", -1, 2),
                            new Among("\u00E8e", -1, 2), new Among("\u017Ee", -1, 2),
                            new Among("ci", -1, 1), new Among("zi", -1, 2),
                            new Among("\u010Di", -1, 2), new Among("\u017Ei", -1, 2),
                            new Among("\u010D\u00ED", -1, 2), new Among("\u017E\u00ED", -1, 2)
                        ],
                        a_1 = [
                            new Among("a", -1, 1), new Among("e", -1, 2),
                            new Among("i", -1, 1), new Among("o", -1, 1),
                            new Among("u", -1, 1), new Among("\u00E1", -1, 1),
                            new Among("\u00E9", -1, 2), new Among("\u00ED", -1, 1),
                            new Among("\u00F3", -1, 1), new Among("\u00FA", -1, 1),
                            new Among("\u011B", -1, 2), new Among("\u016F", -1, 1)
                        ],
                        a_2 = [
                            new Among("c", -1, 1), new Among("h", -1, 2),
                            new Among("k", -1, 1), new Among("l", -1, 1),
                            new Among("n", -1, 1), new Among("t", -1, 1),
                            new Among("y", -1, 1), new Among("z", -1, 1),
                            new Among("\u010D", -1, 1), new Among("\u010F", -1, 1),
                            new Among("\u0148", -1, 1), new Among("\u0159", -1, 1),
                            new Among("\u0161", -1, 1), new Among("\u0165", -1, 1),
                            new Among("\u017E", -1, 1)
                        ],
                        a_3 = [
                            new Among("ov", -1, 1), new Among("\u016F", -1, 2), 
                            new Among("uj", -1, 3), new Among("aj", -1, 4),
                            new Among("ej", -1, 5), new Among("ij", -1, 6),
                            new Among("uj\u00ED", -1, 3), new Among("aj\u00ED", -1, 4),
                            new Among("ej\u00ED", -1, 5), new Among("ij\u00ED", -1, 6),
                            new Among("ujeme", -1, 3), new Among("ujete", -1, 3),
                            new Among("ajeme", -1, 4), new Among("ajete", -1, 4),
                            new Among("ejeme", -1, 5), new Among("ejete", -1, 5),
                            new Among("ijeme", -1, 6), new Among("ijete", -1, 6)
                        ],
                        a_4 = [
                            new Among("u", -1, 1), new Among("a", -1, 2),
                            new Among("e", -1, 2), new Among("i", -1, 3),
                            new Among("\u00ED", -1, 3), new Among("y", -1, 3),
                            new Among("\u011B", -1, 2), new Among("ovi", -1, 4),
                            new Among("emi", -1, 5), new Among("ovi", -1, 6),
                            new Among("ovi", -1, 7), new Among("ovi", -1, 8),
                            new Among("ovy", -1, 9), new Among("ama", -1, 10),
                            new Among("ata", -1, 11), new Among("eti", -1, 12),
                            new Among("ove", -1, 13)
                        ],
                        a_5 = [
                            new Among("a", -1, 1), new Among("e", -1, 1),
                            new Among("i", -1, 1), new Among("y", -1, 1),
                            new Among("\u00E1", -1, 1), new Among("\u00E9", -1, 1),
                            new Among("\u00ED", -1, 1), new Among("u", -1, 2),
                            new Among("\u011B", -1, 1), new Among("\u016F", -1, 2)
                        ],
                        a_6 = [
                            new Among("e", -1, 1), new Among("i", -1, 1),
                            new Among("\u00ED", -1, 1), new Among("\u011B", -1, 1)
                        ],
                        a_7 = [
                            new Among("a", -1, 1), new Among("e", -1, 1),
                            new Among("i", -1, 1), new Among("\u00ED", -1, 1),
                            new Among("\u00E1", -1, 3), new Among("\u00E9", -1, 1),
                            new Among("\u011B", -1, 1)
                        ],
                        g_v = [17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 17, 4, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
                        I_p1, I_pV, sbp = new SnowballProgram();
                    
                    this.setCurrent = function(word) {
                        sbp.setCurrent(word);
                    };
                    
                    this.getCurrent = function() {
                        return sbp.getCurrent();
                    };
                    
                    function r_mark_regions() {
                        var v_1;
                        I_pV = sbp.limit;
                        I_p1 = sbp.limit;
                        v_1 = sbp.cursor;
                        if (sbp.in_grouping(g_v, 97, 367)) {
                            while (!sbp.out_grouping(g_v, 97, 367)) {
                                if (sbp.cursor >= sbp.limit) {
                                    break;
                                }
                                sbp.cursor++;
                            }
                            I_pV = sbp.cursor;
                            if (I_pV < v_1) {
                                I_pV = v_1;
                            }
                        }
                        sbp.cursor = v_1;
                        if (sbp.in_grouping(g_v, 97, 367)) {
                            while (!sbp.out_grouping(g_v, 97, 367)) {
                                if (sbp.cursor >= sbp.limit) {
                                    break;
                                }
                                sbp.cursor++;
                            }
                            while (!sbp.in_grouping(g_v, 97, 367)) {
                                if (sbp.cursor >= sbp.limit) {
                                    break;
                                }
                                sbp.cursor++;
                            }
                            if (sbp.cursor < sbp.limit) {
                                I_p1 = sbp.cursor;
                            }
                        }
                    }
                    
                    function r_RV() {
                        return I_pV <= sbp.cursor;
                    }
                    
                    function r_R1() {
                        return I_p1 <= sbp.cursor;
                    }
                    
                    function r_palatalise() {
                        var among_var;
                        sbp.ket = sbp.cursor;
                        among_var = sbp.find_among_b(a_0, 10);
                        if (among_var) {
                            sbp.bra = sbp.cursor;
                            if (r_RV()) {
                                switch (among_var) {
                                    case 1:
                                        sbp.slice_from("k");
                                        break;
                                    case 2:
                                        sbp.slice_from("h");
                                        break;
                                }
                            }
                        }
                    }
                    
                    function r_do_possessive() {
                        var among_var;
                        sbp.ket = sbp.cursor;
                        among_var = sbp.find_among_b(a_1, 12);
                        if (among_var) {
                            sbp.bra = sbp.cursor;
                            if (r_RV()) {
                                switch (among_var) {
                                    case 1:
                                        sbp.slice_del();
                                        break;
                                    case 2:
                                        sbp.slice_from("e");
                                        r_palatalise();
                                        break;
                                }
                            }
                        }
                    }
                    
                    function r_do_case() {
                        var among_var, v_1;
                        sbp.ket = sbp.cursor;
                        among_var = sbp.find_among_b(a_2, 15);
                        if (among_var) {
                            sbp.bra = sbp.cursor;
                            if (r_RV()) {
                                switch (among_var) {
                                    case 1:
                                        sbp.slice_del();
                                        break;
                                    case 2:
                                        sbp.slice_del();
                                        v_1 = sbp.limit - sbp.cursor;
                                        r_palatalise();
                                        sbp.cursor = sbp.limit - v_1;
                                        break;
                                }
                            }
                        }
                    }
                    
                    function r_do_derivational() {
                        var among_var;
                        sbp.ket = sbp.cursor;
                        among_var = sbp.find_among_b(a_3, 18);
                        if (among_var) {
                            sbp.bra = sbp.cursor;
                            if (r_R1()) {
                                switch (among_var) {
                                    case 1:
                                        sbp.slice_del();
                                        break;
                                    case 2:
                                        sbp.slice_from("a");
                                        break;
                                    case 3:
                                        sbp.slice_from("i");
                                        break;
                                    case 4:
                                        sbp.slice_from("e");
                                        break;
                                    case 5:
                                        sbp.slice_from("e");
                                        break;
                                    case 6:
                                        sbp.slice_from("i");
                                        break;
                                }
                            }
                        }
                    }
                    
                    function r_do_deriv_single() {
                        var among_var;
                        sbp.ket = sbp.cursor;
                        among_var = sbp.find_among_b(a_4, 17);
                        if (among_var) {
                            sbp.bra = sbp.cursor;
                            if (r_R1()) {
                                switch (among_var) {
                                    case 1:
                                        sbp.slice_del();
                                        break;
                                    case 2:
                                        sbp.slice_from("a");
                                        break;
                                    case 3:
                                        sbp.slice_from("i");
                                        break;
                                    case 4:
                                        sbp.slice_from("a");
                                        break;
                                    case 5:
                                        sbp.slice_from("e");
                                        break;
                                    case 6:
                                        sbp.slice_from("e");
                                        break;
                                    case 7:
                                        sbp.slice_from("a");
                                        break;
                                    case 8:
                                        sbp.slice_from("e");
                                        break;
                                    case 9:
                                        sbp.slice_from("e");
                                        break;
                                    case 10:
                                        sbp.slice_from("a");
                                        break;
                                    case 11:
                                        sbp.slice_from("a");
                                        break;
                                    case 12:
                                        sbp.slice_from("a");
                                        break;
                                    case 13:
                                        sbp.slice_from("a");
                                        break;
                                }
                            }
                        }
                    }
                    
                    function r_do_augmentative() {
                        var among_var;
                        sbp.ket = sbp.cursor;
                        among_var = sbp.find_among_b(a_5, 10);
                        if (among_var) {
                            sbp.bra = sbp.cursor;
                            if (r_R1()) {
                                switch (among_var) {
                                    case 1:
                                        sbp.slice_del();
                                        break;
                                    case 2:
                                        sbp.slice_from("i");
                                        r_palatalise();
                                        break;
                                }
                            }
                        }
                    }
                    
                    function r_do_diminutive() {
                        var among_var;
                        sbp.ket = sbp.cursor;
                        among_var = sbp.find_among_b(a_6, 4);
                        if (among_var) {
                            sbp.bra = sbp.cursor;
                            if (r_R1()) {
                                switch (among_var) {
                                    case 1:
                                        sbp.slice_del();
                                        break;
                                }
                            }
                        }
                    }
                    
                    function r_do_comparative() {
                        var among_var;
                        sbp.ket = sbp.cursor;
                        among_var = sbp.find_among_b(a_7, 7);
                        if (among_var) {
                            sbp.bra = sbp.cursor;
                            if (r_R1()) {
                                switch (among_var) {
                                    case 1:
                                        sbp.slice_del();
                                        break;
                                    case 3:
                                        sbp.slice_from("a");
                                        break;
                                }
                            }
                        }
                    }
                    
                    function r_stem() {
                        r_mark_regions();
                        sbp.limit_backward = sbp.cursor;
                        sbp.cursor = sbp.limit;
                        r_do_comparative();
                        sbp.cursor = sbp.limit;
                        r_do_diminutive();
                        sbp.cursor = sbp.limit;
                        r_do_augmentative();
                        sbp.cursor = sbp.limit;
                        r_do_derivational();
                        sbp.cursor = sbp.limit;
                        r_do_deriv_single();
                        sbp.cursor = sbp.limit;
                        r_do_case();
                        sbp.cursor = sbp.limit;
                        r_do_possessive();
                        sbp.cursor = sbp.limit_backward;
                        return true;
                    }
                    
                    this.stem = r_stem;
                };
                
                /* and return a function that returns a stemmer object */
                return function() {
                    /* create the stemmer object */
                    var czech = new st();
                    return function(token) {
                        /* and return a function that stems a word for the stemmer */
                        czech.setCurrent(token);
                        czech.stem();
                        return czech.getCurrent();
                    }
                }
            })();

        // Cache for Czech stopwords
        var czech_stop_words = [
            "a", "aby", "ale", "alespoň", "anebo", "ani", "aniž", "ano", "asi", "aspoň", "až", "bez", "bude", "budem", "budeme", "budeš",
            "budete", "budou", "budu", "by", "byl", "byla", "byli", "bylo", "byly", "bys", "být", "či", "článku", "člověk", "co", "což", "či",
            "další", "do", "ho", "i", "já", "jak", "jaké", "jako", "je", "jej", "jejich", "jejích", "její", "jeho", "jen", "jenž", "ještě", 
            "jestli", "jestliže", "ji", "jich", "jím", "jimi", "jiné", "již", "jsem", "jsi", "jsme", "jsou", "jste", "k", "kam", "kde", "kdo", 
            "když", "ke", "kolik", "kromě", "kterou", "kteroužto", "který", "kteří", "ku", "li", "málo", "mé", "mě", "mezi", "mi", "mí", "mít", 
            "mně", "mou", "může", "můj", "my", "na", "nad", "nám", "námi", "naproti", "nás", "náš", "naše", "ne", "nebo", "neboť", "než", "ni", 
            "nic", "nich", "ním", "nimi", "nějaký", "některý", "nyní", "o", "od", "ode", "on", "ona", "oni", "ono", "ony", "pak", "po", "pod", 
            "podle", "pokud", "pouze", "pro", "proč", "proto", "protože", "před", "při", "s", "se", "si", "sice", "své", "svůj", "svých", "svým", 
            "svými", "ta", "tak", "také", "takový", "tam", "tato", "tě", "tedy", "ten", "ti", "tím", "tímto", "to", "tobě", "tohle", "toho", 
            "tohoto", "tom", "tomto", "tomu", "tomuto", "totiž", "tu", "tuto", "tvá", "tvé", "tvoje", "tvůj", "ty", "tyto", "u", "už", "v", "vám", 
            "vámi", "vás", "váš", "vaše", "ve", "více", "však", "všechno", "všechen", "vy", "vždy", "z", "za", "zda", "zde", "ze", "že"
        ];

        /* lunr stop word filter. see https://lunrjs.com/docs/stop_word_filter.js.html */
        lunr.cs.stopWordFilter = lunr.generateStopWordFilter(czech_stop_words);
        
        // Register the filter with lunr
        lunr.Pipeline.registerFunction(lunr.cs.stopWordFilter, 'stopWordFilter-cs');

        // Register the stemmer with lunr
        lunr.Pipeline.registerFunction(lunr.cs.stemmer, 'stemmer-cs');
    };
}))