<script lang="ts">
  import Healthcare from '$lib/assets/healthcare.png'
  import video from '$lib/assets/reliability.mp4'
</script>

<section id="about-container">
  <div class="sub">
    <div id="healthcare-container">
      <img src={Healthcare} alt="A pair of healthcare workers" />
    </div>
    <p>
      <span class="gradient bold">Inspired by the hard work of healthcare workers,</span>
       NeuroScanAI is dedicated to developing AI models that 
       <span class="bold">empower them to enhance brain tumor diagnosis</span>
    </p>
  </div>
  <div class="sub">
    <p>
      <span class="bold">Reliability is our main priority.</span>
       By utilizing the latest cutting-edge AI technology to analyze MRI scans, 
       we ensure the
       <span class="gradient bold">highest levels of precision</span>
    </p>
    <video autoplay muted width="1200">
      <source src={video}>
      This browser does not support videos
    </video>
  </div>
</section>

<style>
  #about-container {
    color: white;
  }
  .sub {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10rem 7rem;
  }
  p {
    max-width: 550px;
    font-size: 2.25rem;
  }
</style>