<script lang="ts">
	import Footer from "$lib/Footer.svelte";
  import Navbar from "$lib/Navbar.svelte";
	import UploadForm from "$lib/UploadForm.svelte";
  import Brain from '$lib/assets/brain.png'
  import Heart from '$lib/assets/heart.png'
</script>

<Navbar />
<main>
  <section id="hero-container">
    <div id="hero-text">
      <h1>NeuroScanAI</h1>
      <p>Tumor detection made easy</p>
    </div>
    <img id="hero-image" src={Brain} alt="An AI generated brain" />
  </section>
  <section id="about-container">
    <div class="sub">
      <div>
        <img />
        <img />
      </div>
      <p>
        <span class="gradient bold">Inspired by the hard work of healthcare workers,</span>
         NeuroScanAI is dedicated to developing AI models that 
         <span class="bold">empower them to enhance brain tumor diagnosis</span>
      </p>
    </div>
    <div class="sub">
      <img />
      <p>
        <span class="bold">Reliability is our main priority.</span>
         By utilizing the latest cutting-edge AI technology to analyze MRI scans, 
         we ensure the
         <span class="gradient bold">highest levels of precision</span>
      </p>
    </div>
  </section>
  <section id="demo">
    <UploadForm />
  </section>
  <section id="our-team">
    <h2 class="bold">Our Team</h2>
    <div>
      <img />
      <p>Moumen Msallaty</p>
    </div>
    <div>
      <img />
      <p>Kieran Llarena</p>
    </div>
    <div>
      <img />
      <p>Jawad Mourad</p>
    </div>
    <div>
      <img />
      <p>Mahdi Rizk</p>
    </div>
  </section>
  <section>
    <h3>
      Made with <span><img src={Heart} /></span> and with...
      <div>
        <img />
      </div>
    </h3>
  </section>
</main>
<Footer />

<style>
  section {
    scroll-behavior: smooth;
  }
  #hero-container {
    display: flex;
    color: white;
    align-items: center;
    justify-content: space-around;
    background: radial-gradient(#450000, #000000);
    scroll-behavior: smooth;
  }
  h1 {
    background: linear-gradient(to right, #FF00E5, #9E00FF);
    background-clip: text;
    color: transparent;
    -webkit-text-fill-color: transparent; 
    -webkit-background-clip: text;
    font-size: 5rem;
  }
  #hero-container p {
    font-style: italic;
    font-weight: bold;
    text-align: right;
  }
  #hero-image {
    max-width: 986px;
  }
  #about-container {
    color: white;
  }
  #about-container .sub {
    display: flex;
    justify-content: space-between;
  }
  #about-container .sub img {
    width: 600px;
    height: 600px;
  }
  h2 {
    text-align: center;
    color: white;
  }
  h3 {
    text-align: center;
    color: white;
  }
  h3 img {
    width: 2rem;
  }
  .gradient {
    background: linear-gradient(to right, #FF00E5, #9E00FF);
    background-clip: text;
    color: transparent;
    -webkit-text-fill-color: transparent; 
    -webkit-background-clip: text;
  }
  .bold {
    font-weight: bold;
  }
  .gradient.bold {
    font-size: 1.3rem;
  }
</style>