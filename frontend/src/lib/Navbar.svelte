<script lang="ts">
  import SmallBrain from '$lib/assets/smallbrain.png'
</script>

<header>
  <nav>
    <div id="logo-container">
      <img src={SmallBrain} alt="NeuroScanAI logo" />
      <h3>NeuroScan<span>AI</span></h3>
    </div>
    <div id="desktop-container">
      <a href='#'>Home</a>
      <a href='#'>About Us</a>
      <a href='#'>Details</a>
      <a href='#'>Demo</a>
    </div>
  </nav>
</header>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
  header {
    padding-top: 1.25rem;
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
  #desktop-container a:last-child {
    background-color: rgb(217, 217, 217);
    background: linear-gradient(270deg, rgba(217, 217, 217, 1), rgba(217, 217, 217, 0.3));
    padding: .75rem 1.75rem;
    font-weight: bolder;
    border-radius: 2rem;
  }
</style>