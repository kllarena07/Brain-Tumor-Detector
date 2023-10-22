<script lang="ts">
  import Brain from '$lib/assets/brain.png'
</script>

<section id="hero-container">
  <div id="hero-text">
    <h1>NeuroScanAI</h1>
    <p>Tumor detection made easy</p>
    <a id="desktop-btn" class="bold" href='#demo'>Demo</a>
  </div>
  <img id="hero-image" src={Brain} alt="An AI generated brain" />
  <a id="mobile-btn" class="bold" href='#demo'>Demo</a>
</section>

<style>
  #hero-container {
    display: flex;
    color: white;
    align-items: center;
    justify-content: center;
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
    background: radial-gradient(#450000 5%, #000000 70%);
  }
  #hero-text {
    display: flex;
    flex-direction: column;
    margin-right: 1.5rem;
  }
  a {
    font-size: 1.25rem;
    color: white;
    text-decoration: none;
    background: linear-gradient(to right, #2E4EBD, #DB00FF);
    padding: .75rem 3.5rem;
    border-radius: 100rem;
    margin-top: 2rem;
    margin-left: auto;
    margin-right: auto;
  }
  #mobile-btn {
    display: none;
    transform: scale(3);
  }
  @media only screen and (max-width: 600px) {
    #hero-container {
      display: flex;
      flex-direction: column;
    }
    #desktop-btn {
      display: none;
    }
    #mobile-btn {
      display: inline-block;
    }
    #hero-text {
      transform: scale(1.4);
    }
    #hero-image {
      transform: scale(0.9);
    }
  }
  @media only screen and (600px < width <= 1020px) {
    #hero-container {
      display: flex;
      flex-direction: column;
    }
    #desktop-btn {
      display: none;
    }
    #mobile-btn {
      display: inline-block;
    }
    #hero-text {
      transform: scale(2);
    }
  }
  @media only screen and (width <= 1270px) {
    #hero-container {
      transform: scale(0.5);
    }
  }
  @media only screen and (1270px < width < 1635px) {
    #hero-container {
      transform: scale(0.8);
    }
  }
</style>