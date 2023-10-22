<script lang="ts">
  import Brain from '$lib/assets/brain.png'
</script>

<section id="hero-container">
  <div id="hero-text">
    <h1>NeuroScanAI</h1>
    <p>Tumor detection made easy</p>
    <a class="bold" href='#demo'>Demo</a>
  </div>
  <img id="hero-image" src={Brain} alt="An AI generated brain" />
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
</style>