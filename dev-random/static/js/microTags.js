
var µTags = function(element, options) {
    this._el = element;
    this._children = element.childNodes;

    this._max_size = 3;
    this._min_size = 0.7;
    this._max_angle = 15;
    this._min_angle = -15;

    if (options != undefined)
        this._set_options(options);

    this._max_count = this._get_max_count();
    this._set_sizes();
    this._set_tilt();
}

µTags.prototype.version = "0.1a"

µTags.prototype._set_options = function(options) {
    var max_size  = options['max-size'],
        min_size  = options['min-size'],
        max_angle = options['max-angle'],
        min_angle = options['min-angle'];

    if ((max_size >= 1) && (max_size > min_size))
        this._max_size = max_size;
    else
        console.error("µTags: option `max-size` must be >= 1 and > min-size");

    if ((min_size > 0) && (min_size < max_size))
        this._min_size = min_size;
    else
        console.error("µTags: option `min-size` must be > 0 and < max-size");

    if (max_angle > min_angle) {
        this._max_angle = max_angle;
        this._min_angle = min_angle;
    }
    else
        console.error("µTags: option `max-angle` must be > `min-angle`");
        
}

µTags.prototype.eachTag = function(callback) { 
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

µTags.prototype._get_max_count = function() {
    var max = 0;
    this.eachTag(function(element, count) {
        max = (max < count) ? count : max;
    });
    return max;
}

µTags.prototype._set_sizes = function() {
    var size,
        max = this._max_size,
        min = this._min_size,
        max_count = this._max_count;

    this.eachTag(function(element, count) {
        size = (count * max / max_count);
        size = (size >= min) ? size : min;
        console.debug(element+ ': ' + count + ': ' + size );
        element.style['fontSize'] = size + 'em';
    });
}

µTags.prototype._set_tilt = function() {
    var angle,
        max = this._max_angle,
        min = this._min_angle;
    this.eachTag(function(element, count) {
        angle = min + (Math.random() * (max - min));
        element.style['transform']       = 'rotate(' + angle + 'deg)';
        element.style['MozTransform']    = 'rotate(' + angle + 'deg)';
        element.style['OTransform']      = 'rotate(' + angle + 'deg)';
        element.style['WebkitTransform'] = 'rotate(' + angle + 'deg)';
        element.style['msTransform']     = 'rotate(' + angle + 'deg)';
    });

}

if (window != undefined) {
    window.µTags = µTags;
}


