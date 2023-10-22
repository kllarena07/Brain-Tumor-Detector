<script lang="ts">
  import SmallBrain from '$lib/assets/smallbrain.png'
</script>

<footer>
  <nav>
    <div id="logo-container">
      <img src={SmallBrain} alt="NeuroScanAI logo" />
      <h3>NeuroScan<span>AI</span></h3>
    </div>
    <div id="desktop-container">
      <a href='#hero-container'>Home</a>
      <a href='#about-container'>About Us</a>
      <a href='#our-team'>Our Team</a>
      <a href='#demo'>Demo</a>
    </div>
  </nav>
</footer>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
  footer {
    padding-bottom: .5rem;
  }
  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 3rem;
    color: white;
    font-family: 'Montserrat', sans-serif;
  }
  #logo-container {
    display: flex;
    align-items: center;
  }
  h3 {
    margin-left: .75rem;
    font-weight: bold;
    font-size: 1.5rem;
  }
  h3 span {
    background: linear-gradient(to right, #FF00E5, #9E00FF);
    background-clip: text;
    color: transparent;
    -webkit-text-fill-color: transparent; 
    -webkit-background-clip: text;
  }
  #desktop-container a {
    margin: 0 1rem;
    text-decoration: none;
    color: white;
  }
  @media only screen and (max-width: 1020px) {
    footer {
      display: none;
    }
  } 
</style>