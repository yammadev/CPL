<template>
  <section class="container" v-if="statistics">
    <!-- Statistics -->
    <div class="statistics z-depth-1" id="stats">
      <!-- Current -->
      <div class="current container row">
        <div class="col s3 center">
          <h4>{{ current.reported }}</h4>
          <p>Reportados</p>
          <span>{{ percentages.reported }}%</span>
        </div>

        <div class="col s3 center">
          <h4>{{ current.repairing }}</h4>
          <p>En reparación</p>
          <span>{{ percentages.repairing }}%</span>
        </div>

        <div class="col s3 center">
          <h4>{{ current.repaired }}</h4>
          <p>Reparados</p>
          <span>{{ percentages.repaired }}%</span>
        </div>

        <div class="col s3 center">
          <h4>{{ current.total }}</h4>
          <p>Total</p>
        </div>
      </div>

      <!-- Chart -->
      <canvas id="chart"></canvas>
    </div>
  </section>
</template>

<script>
import Chart from 'chart.js';

export default {
  // Component
  name: 'statistics',

  // Props
  props: {
    potholes: {
      required: true
    }
  },

  // Data
  data: function() {
    return {
      statistics: [],
      percentages: [],
      current: []
    }
  },

  // Watch
  watch: {
    potholes: function() {
      this.update();
    },
    statistics: function() {
      this.percentages = this.statistics.percentages;
      this.current = this.statistics.current;
      this.updateChart();
    }
  },

  // Mounted
  mounted: function() {
    this.update();
  },

  // Methods
  methods: {
    //
    update: function() {
      let self = this;

      // Call
      axios.get('/statistics')

      // Success
      .then(function(response) {
        self.statistics = response.data;
      });
    },

    // update Chart
    updateChart: function() {
      let self = this;

      let ctx = document.getElementById('chart').getContext('2d');
      let chart = new Chart(ctx, {
        data: {
          datasets: [{
            data: [
              self.percentages.reported,
              self.percentages.repairing,
              self.percentages.repaired
            ],
            backgroundColor: [
              'rgba(198, 40, 40, 0.9)',   // Red
              'rgba(42, 129, 203, 0.9)',  // Blue
              'rgba(42, 173, 39, 0.9)'    // Green
  					]
          }],
          labels: ['Reportados', 'En reparación', 'Reparados'],
        },

        type: 'polarArea',

        options: {
          responsive: true
        }
      });
    }
  }
}
</script>
