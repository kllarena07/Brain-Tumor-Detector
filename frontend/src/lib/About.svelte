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
    <div id="video-wrapper">
      <video autoplay muted>
        <source src={video}>
        This browser does not support videos
      </video>
    </div>
    <p>
      <span class="bold">Reliability is our main priority.</span>
       By utilizing the latest cutting-edge AI technology to analyze MRI scans, 
       we ensure the
       <span class="gradient bold">highest levels of precision</span>
    </p>
  </div>
</section>

<style>
  #about-container {
    color: white;
  }
  .sub {
    display: flex;
    padding: 10rem 7rem;
    gap: 10rem;
  }
  .sub:nth-child(1) {
    justify-content: center;
    align-items: center;
  }
  .sub:nth-child(2) {
    flex-direction: row-reverse;
    align-items: center;
    justify-content: center;
  }
  p {
    max-width: 550px;
  }
  #video-wrapper {
    max-width: 1000px;
  }
  video {
    width: 100%;
  }
  @media only screen and (width < 1000px) {
    .sub:nth-child(1) {
      display: inline-block;
      padding: 2.5rem;
    }
    p {
      margin-top: 3rem;
      font-size: 1rem;
    }
    .sub:nth-child(2) {
      display: inline-block;
      padding: 2.5rem;
    }
  }
  @media only screen and (1000px < width < 1200px) {
    img {
      width: 1000px;
      margin-bottom: 3rem;
    }
    .sub {
      display: inline-block;
      margin: auto;
      padding: 2.5rem;
    }
    p {
      font-size: 2rem;
      margin: auto;
    }
  }
  @media only screen and (1200px < width < 1400px) {
    p {
      font-size: 1.25rem;
    }
  }
  @media only screen and (1400px < width < 1600px) {
    p {
      font-size: 1.5rem;
    }
  }
  @media only screen and (1600px < width < 1920px) {
    p {
      font-size: 2rem;
    }
  }
  @media only screen and (min-width: 1920px) {
    p {
      font-size: 2.25rem;
    }
  }
</style>