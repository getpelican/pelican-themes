{% if GOOGLE_ANALYTICS %}
    <!-- Global Site Tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={{GOOGLE_ANALYTICS}}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '{{GOOGLE_ANALYTICS}}', { 'anonymize_ip': true });
    </script>
    
{% endif %}
{% if GAUGES %}
    <script type="text/javascript">
    var _gauges = _gauges || [];
    (function() {
        var t   = document.createElement('script');
        t.type  = 'text/javascript';
        t.async = true;
        t.id    = 'gauges-tracker';
        t.setAttribute('data-site-id', '{{GAUGES}}');
        t.src = '//secure.gaug.es/track.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(t, s);
    })();
    </script>
{% endif %}
