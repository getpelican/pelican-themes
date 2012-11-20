
(function(doc, win, v) {
    
    /**
     * The microTags exception
     *
     * @class microTags.error
     * @constructor
     * @param message {String} an error message
     * @example
     *     try {
     *         var t = new microTags(undefined);
     *     } 
     *     catch(e) {
     *          if (e instaceOf micrTags.error) {
     *              console.debug("Epic fail: " + e.message);
     *          }
     *     }
     */
    function error(message) {
        this.message = "microTags: " + message;
    }
    error.prototype = Error.prototype;

    /**
     * Create a new microTags instance
     *
     * @class microTags
     * @constructor
     * @param element {HTMLElement} an element containing tags
     * @param options {Object} A JSON hash containing options
     */
    function microTags(element, options) {
        if (!(element && element.nodeName))
            throw new error("argument #1 must be an HTMLElement !");
        this._el = element;
        this._children = element.children;

        this._max_size = 3;
        this._min_size = 0.7;
        this._max_angle = 10;
        this._min_angle = -10;

        if (options != undefined)
            this._set_options(options);

        this._max_count = this._get_max_count();

        self = this;
        this.eachTag(function(element, count) {
            self._make_inline(element, count);
            self._set_size(element, count);
            self._set_tilt(element, count);
        });
    }

    /**
     * the microTags current version
     *
     * @attribute version {String}
     */
    microTags.prototype.version = v;
    microTags.version = v;


    microTags.prototype._set_options = function(options) {
        var max_size  = options['max-size'],
            min_size  = options['min-size'],
            max_angle = options['max-angle'],
            min_angle = options['min-angle'];

        if ((max_size >= 1) && (max_size > min_size))
            this._max_size = max_size;
        else
            throw error("option `max-size` must be >= 1 and > min-size");

        if ((min_size > 0) && (min_size < max_size))
            this._min_size = min_size;
        else
            throw error("option `min-size` must be > 0 and < max-size");

        if (max_angle > min_angle) {
            this._max_angle = max_angle;
            this._min_angle = min_angle;
        }
        else
            throw error("option `max-angle` must be > `min-angle`");
            
    }

    /**
     * Apply a function on each tag
     *
     * @param [Function] callback: the function to apply
     */
    microTags.prototype.eachTag = function(callback) { 
        var i, child, tag, count;
        for (i=0; i < this._children.length; i++) {
            child = this._children[i];
            if (child.attributes != undefined) {
                window._c = child;
                count = parseInt(child.attributes["data-count"].value || "1");
                callback(child, count);
            }
        }
    }


    microTags.prototype._get_max_count = function() {
        var max = 0;
        this.eachTag(function(element, count) {
            max = (max < count) ? count : max;
        });
        return max;
    }


    microTags.prototype._make_inline = function(element, coun) {
        element.style['display'] = 'inline-block';
    }


    microTags.prototype._set_size = function(element, count) {
        var size,
            max = this._max_size,
            min = this._min_size,
            max_count = this._max_count;

        size = (count * max / max_count);
        size = (size >= min) ? size : min;
        element.style['fontSize'] = size + 'em';
    }


    microTags.prototype._set_tilt = function(element, count) {
        var angle,
            max = this._max_angle,
            min = this._min_angle;
        angle = min + (Math.random() * (max - min));
        element.style['transform']       = 'rotate(' + angle + 'deg)';
        element.style['MozTransform']    = 'rotate(' + angle + 'deg)';
        element.style['OTransform']      = 'rotate(' + angle + 'deg)';
        element.style['WebkitTransform'] = 'rotate(' + angle + 'deg)';
        element.style['msTransform']     = 'rotate(' + angle + 'deg)';
    }


    if (win != undefined) {
        win.microTags = microTags;
        win.microTags.error = error;

        if (win.define && win.define.call) {
            win.define(function() {
                return microTags;
            });
        }
    }

})(window.document, window, "0.3.2");
