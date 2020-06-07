<template>
  <div class="mapsection">
    <!-- Map -->
    <l-map
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      @update:center="centerUpdate">

      <!-- Tile layer -->
      <l-tile-layer
        :url="url"
        :attribution="attribution"/>

      <!-- Potholes markers -->
      <l-marker v-for="pothole in potholes"
        :key="potholes.id"
        :lat-lng="[pothole.lat, pothole.lng]"
        @click="showSave=false">

        <!-- Popup -->
        <l-popup class="info">
          <h5>Información</h5>

          <!-- Status -->
          <p v-if="pothole.stat == 'repaired'" class="green-text">
            <i class="material-icons">check_circle</i> Reparado
          </p>
          <p v-else-if="pothole.stat == 'repairing'" class="blue-text">
            <i class="material-icons">remove_circle</i> En reparación
          </p>
          <p v-else class="red-text">
            <i class="material-icons">cancel</i> Reportado
          </p>
          <br>

          <!-- Details -->
          <p><span>Reportó: </span> {{ pothole.name }}</p>
          <p><span>Descripción: </span> {{ pothole.desc }}</p>
          <p><span>Ubicación: </span> {{ [pothole.lat, pothole.lng] }}</p>

          <!-- Actions -->
          <p v-if="pothole.stat == 'repairing'" class="row">
            <a href="#" class="btn btn-green col s12"
              @click="changeStatus('repaired', pothole.id)">
              ¿Reparado?
            </a>
          </p>
          <p v-else-if="pothole.stat == 'reported'" class="row">
            <a href="#" class="btn btn-blue col s12"
              @click="changeStatus('repairing', pothole.id)">
                ¿En reparación?
            </a><br>
            <a href="#" class="btn btn-green col s12"
              @click="changeStatus('repaired', pothole.id)">
                ¿Reparado?
            </a>
          </p>
          <p v-else class="row">
            <a href="#" class="btn btn-red col s12"
              @click="changeStatus('reported', pothole.id)">
              ¿Volver a reportar?
            </a>
          </p>
        </l-popup>

        <!-- Icon -->
        <l-icon v-if="pothole.stat == 'reported'" :options="red"/>
        <l-icon v-else-if="pothole.stat == 'repaired'" :options="green"/>
        <l-icon v-else :options="blue"/>
      </l-marker>

      <!-- Tracker -->
      <button type="button" id="toggleSave" @click="toggleSave" style="display: none;"></button>
      <l-marker v-if="showSave" :lat-lng="currentCenter">
        <!-- Icon -->
        <l-icon :options="red"></l-icon>

        <!-- Tolltip -->
        <l-tooltip :options="{ permanent: true, interactive: true }" class="row">
          <p class="col s12">Ubique el punto que desea reportar</p>
          <a class="col s12 btn btn-red" @click="openSave">¡Listo!</a>
        </l-tooltip>
      </l-marker>
    </l-map>

    <!-- Save -->
    <Save :point="currentCenter"></Save>
  </div>
</template>

<script>
import Save from './_save.vue';
import { L, latLng  } from 'leaflet';
import { LMap, LTileLayer, LMarker, LIcon, LPopup, LTooltip  } from 'vue2-leaflet';

export default {
  // Component
  name: 'mapsection',

  // components
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon,
    LPopup,
    LTooltip,
    Save
  },

  // Data
  data: function() {
    return {
      zoom: 14,
      center: latLng(10.412687, -75.52345),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      currentCenter: latLng(10.412687, -75.52345),
      mapOptions: {
        minZoom: 13,
        maxZoom: 18
      },
      red: {
        iconUrl: "https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png",
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png'
      },
      blue: {
        iconUrl: "https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png",
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png'
      },
      green: {
        iconUrl: "https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png",
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png'
      },
      potholes: [],
      showSave: false
    }
  },

  // Mounted
  mounted: function() {
    this.list();
  },

  // Methods
  methods: {
    // List
    list: function() {
      let self = this;
      self.potholes = null;

      // Call
      axios.get('list')

      // Success
      .then(function(response) {
        self.potholes = response.data;
        if(response.status == 204) {
          // Alert
          Swal({
            title: "Bienvenido",
            text: "En éste momento no hay baches reportados, sin embargo, puedes informar sobre uno haciendo click en 'Publicar'",
            icon: "info",
            button: "Continuar"
          });
        }
      });
    },

    // Update Center
    centerUpdate(center) {
      this.currentCenter = center;
    },

    // Toggle Save Button
    toggleSave: function(event) {
      this.showSave =! this.showSave
    },

    // Open Save Modal
    openSave: function(event) {
      $('#save').modal('open');
    },

    // Change status
    changeStatus: function(stat, id) {
      let self = this;

      // Call
      axios.post('/update', {
        'stat': stat,
        'id': id
      })
      // Success
      .then(function(response) {
        // Alert
        Swal({
          title: "Listo",
          text: "Reporte actualizado.",
          icon: "success",
          button: "Continuar"
        });

        self.list();
      });
    }
  }
};
</script>
