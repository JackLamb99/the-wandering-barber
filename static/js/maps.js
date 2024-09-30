// Coordinates for circling the M60 motorway around the greater Manchester area
// Generated using Google's 'My Maps' tool
// https://www.google.com/maps/d/edit?mid=1CM3_-vMxktowV_qYEjW_fsb5GL7rHfg&ll=53.474749537979406%2C-2.2502079999999958&z=12
const m60Coordinates = [
    { lat: 53.5524384, lng: -2.2596494 },
    { lat: 53.5487669, lng: -2.2685758 },
    { lat: 53.5444831, lng: -2.281622 },
    { lat: 53.5397908, lng: -2.2926084 },
    { lat: 53.5383626, lng: -2.305998 },
    { lat: 53.5342817, lng: -2.3135511 },
    { lat: 53.5308127, lng: -2.3231641 },
    { lat: 53.526323, lng: -2.34651 },
    { lat: 53.5261189, lng: -2.3602429 },
    { lat: 53.5201999, lng: -2.369856 },
    { lat: 53.5114219, lng: -2.3726026 },
    { lat: 53.5024378, lng: -2.3859922 },
    { lat: 53.4965155, lng: -2.3880521 },
    { lat: 53.4907966, lng: -2.381529 },
    { lat: 53.4865069, lng: -2.3784391 },
    { lat: 53.4787435, lng: -2.3774091 },
    { lat: 53.4697525, lng: -2.3732892 },
    { lat: 53.4650519, lng: -2.3660794 },
    { lat: 53.4601464, lng: -2.3447934 },
    { lat: 53.4568758, lng: -2.3406736 },
    { lat: 53.4458354, lng: -2.3427335 },
    { lat: 53.4423592, lng: -2.3399869 },
    { lat: 53.4384736, lng: -2.3355237 },
    { lat: 53.4378601, lng: -2.3235074 },
    { lat: 53.4356103, lng: -2.315611 },
    { lat: 53.430906, lng: -2.3066846 },
    { lat: 53.4282468, lng: -2.2984449 },
    { lat: 53.4237462, lng: -2.2939817 },
    { lat: 53.4165852, lng: -2.2888318 },
    { lat: 53.4131065, lng: -2.2771588 },
    { lat: 53.4131065, lng: -2.2630826 },
    { lat: 53.4102415, lng: -2.2551862 },
    { lat: 53.3975514, lng: -2.2404233 },
    { lat: 53.397142, lng: -2.229437 },
    { lat: 53.4002126, lng: -2.2084943 },
    { lat: 53.4012361, lng: -2.1968213 },
    { lat: 53.4061484, lng: -2.1865216 },
    { lat: 53.4083997, lng: -2.1652356 },
    { lat: 53.4129019, lng: -2.1545926 },
    { lat: 53.4188359, lng: -2.1377698 },
    { lat: 53.4184267, lng: -2.13262 },
    { lat: 53.423337, lng: -2.121977 },
    { lat: 53.4276331, lng: -2.1226636 },
    { lat: 53.4343832, lng: -2.1254102 },
    { lat: 53.4484935, lng: -2.1329633 },
    { lat: 53.4589199, lng: -2.1333066 },
    { lat: 53.4644388, lng: -2.1367398 },
    { lat: 53.4687307, lng: -2.1353665 },
    { lat: 53.4767002, lng: -2.1164838 },
    { lat: 53.484464, lng: -2.1123639 },
    { lat: 53.4922264, lng: -2.1147672 },
    { lat: 53.5012126, lng: -2.1250669 },
    { lat: 53.520404, lng: -2.1384564 },
    { lat: 53.5248943, lng: -2.1525327 },
    { lat: 53.5295883, lng: -2.1607724 },
    { lat: 53.5289761, lng: -2.1772519 },
    { lat: 53.5326493, lng: -2.1899549 },
    { lat: 53.5340777, lng: -2.2030011 },
    { lat: 53.5410149, lng: -2.2098676 },
    { lat: 53.543871, lng: -2.2211972 },
    { lat: 53.5412189, lng: -2.2339002 },
    { lat: 53.5524384, lng: -2.2596494 }
];

function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 11,
        center: { lat: 53.4808, lng: -2.2426 }, // Center of Greater Manchester
    });

    const serviceAreaPolygon = new google.maps.Polygon({
        paths: m60Coordinates,
        strokeColor: "#00563B", // Green outline
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#00563B", // Green fill
        fillOpacity: 0.35,
    });

    // Set the polygon on the map
    serviceAreaPolygon.setMap(map);
}
