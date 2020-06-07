<template>
  <!-- Modal -->
  <div id="save" class="modal modal-fixed-footer">
    <div class="modal-content">
      <h5>Registrar</h5>

      <p v-if="error" class="red-text"><br>
        <span class="material-icons left">cancel</span>Lo sentimos, {{ error }}
      </p>

      <!-- Form -->
      <form :action="send" class="row" method="POST">
        <div class="input-field col s12">
          <label for="name">Nombre</label>
          <input type="text" name="name" id="name" required v-model="form.name">
        </div>

        <div class="input-field col s6">
          <label for="lat">Latitud (Aut.)</label>
          <input type="text" name="lat" id="lat" v-model="form.lat" disabled>
        </div>

        <div class="input-field col s6">
          <label for="lng">Longitud (Aut.)</label>
          <input type="text" name="lng" id="lng" v-model="form.lng" disabled>
        </div>

        <div class="input-field col s12">
          <textarea id="desc" class="materialize-textarea" v-model="form.desc"></textarea>
          <label for="desc">Descripción</label>
        </div>
      </form>
    </div>

    <!-- Actions -->
    <div class="modal-footer">
      <a href="#!" class="modal-close btn-flat" @click="cancel">Cancelar</a>
      <a href="#!" class="btn btn-blue" @click="send">Enviar</a>
    </div>
  </div>
</template>

<script>
export default {
  // Component
  name: 'save',

  // Props
  props: {
    point: {
      required: true,
    }
  },

  // Data
  data: function() {
    return {
      form: {
        name: '',
        lat: this.point.lat,
        lng: this.point.lng,
        desc: ''
      },
      error: null
    }
  },

  // Watch
  watch: {
    point: function(val) {
      this.form.lat = val.lat;
      this.form.lng = val.lng;
    },
  },

  // Mounted
  mounted: function() {
    let self = this;

    // Init
    $('#save').modal({
      onCloseStart: function() {
        self.reset();
      }
    });
  },

  // Methods
  methods: {
    // Send
    send: function() {
      let self = this;

      // Call
      axios.post('save', self.form)

      // Success
      .then(function(response) {
        // Close
        $('#save').modal('close');

        // Reset
        self.error = null;

        // Recall
        self.$parent.list();
        self.cancel();

        // Alert
        Swal({
          title: "Listo",
          text: "Gracias por tu reporte.",
          icon: "success",
          button: "Continuar"
        });
      })

      // Error
      .catch(function(error) {
        self.error = error.response.data.message;
      });
    },

    // Cancel
    cancel: function() {
      this.$parent.toggleSave();
      this.reset();
    },

    // Reset
    reset: function() {
      this.form = {
        name: '',
        lat: this.point.lat,
        lng: this.point.lng,
        desc: ''
      };

      this.error = null;
    }
  }
}
</script>
