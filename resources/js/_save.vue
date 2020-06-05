<template>
  <div class="container">
    <form :action="url" method="POST">
			<fieldset>
				<label for="name">Name</label>
				<input type="text" name="name" id="name" placeholder="Ex. John Smith" required autofocus>
				<label for="latitude">Latitude</label>
				<input type="text" name="latitude" id="latitude" placeholder="Ex. 10.393228" required autofocus>
				<label for="longitude">Longitude</label>
				<input type="text" name="longitude" id="longitude" placeholder="Ex. -75.483231" required autofocus>
				<label for="description">Description</label>
				<input type="text" name="description" id="description"
					placeholder="Ex. This is a big pothole located on street corner" required autofocus>
				<input type="submit" value="Save" />
			</fieldset>
		</form>
  </div>
</template>

<script>
export default {
  // Component
  name: 'save',

  // Properties
  props: {
    url: {
      type: String,
      required: true
    }
  },

  // Mounted
  mounted: function() {

  }
}
</script>
