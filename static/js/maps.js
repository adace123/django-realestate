const map = document.querySelector('#map-widget');
if (map) {
    const [lat, lon] = [map.dataset.lat, map.dataset.lon];
    try {
        const map = new OpenLayers.Map("map-widget");
        map.addLayer(new OpenLayers.Layer.OSM());
        const lonLat = new OpenLayers.LonLat(lon, lat)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
            map.getProjectionObject() // to Spherical Mercator Projection
          );
        const markers = new OpenLayers.Layer.Markers( "Markers" );
        map.addLayer(markers);
        markers.addMarker(new OpenLayers.Marker(lonLat));
        map.setCenter(lonLat, 17);
    } catch(e) {
        console.log(e);
    }
}