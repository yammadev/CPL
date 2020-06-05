<template>
  <div class="mapsection">
    <l-map :zoom = "conf.zoom" :center = "conf.center" :options = "conf.mapOptions">
      <l-tile-layer :url = "conf.url" :attribution = "conf.attribution"/>
      <l-marker v-for = "pothole in potholes"
           :key = "potholes.id"
           :lat-lng = "pothole.position">
          <!--
         <l-icon>
           <div class="headline">
             {{ pothole.position }}
           </div>
         </l-icon>-->
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { L } from 'leaflet';
import { LMap, LTileLayer, LMarker, LIcon } from 'vue2-leaflet';

export default {
  // Component
  name: 'mapsection',

  // components
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon
  },

  // Data
  data: function() {
    return {
      // Configs
      conf: {
        zoom: 14,
        center: [10.412687, -75.52345],
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        mapOptions: {
          minZoom: 13,
          maxZoom: 18
        }
      },
      potholes: []
    }
  },

  // Mounted
  mounted: function() {
    this.list()
  },

  // Methods
  methods: {
    // List
    list: function() {
      let self = this;

      // Call
      axios.get('list')

      // Success
      .then(function(response) {
        self.potholes = response.data;
      });
    }
  }
};
</script>
