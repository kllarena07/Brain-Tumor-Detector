<script lang="ts">
  import SmallBrain from '$lib/assets/smallbrain.png'

  let toggled = false
</script>

<header>
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
    <div id="mobile-container">
      <button on:click={() => toggled = !toggled}>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
        </svg>        
      </button>
    </div>
  </nav>
</header>
{#if toggled}
  <div id="dropdown">
    <nav>
      <a href='#hero-container' on:click={() => toggled = !toggled}>Home</a>
      <a href='#about-container' on:click={() => toggled = !toggled}>About Us</a>
      <a href='#our-team' on:click={() => toggled = !toggled}>Our Team</a>
      <a href='#demo' on:click={() => toggled = !toggled}>Demo</a>
    </nav>
  </div>
{/if}

<style>
  header {
    padding-top: 1.25rem;
  }
  header nav {
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
    background: rgba(217, 217, 217, 0.3);
    padding: .75rem 1.75rem;
    font-weight: bolder;
    border-radius: 2rem;
  }
  #mobile-container {
    display: none;
  }
  #mobile-container svg {
    height: 2rem;
  }
  #mobile-container button {
    padding: 0;
    background-color: transparent;
    border: none;
    outline: none;
    cursor: pointer;
  }
  #dropdown {
    position: absolute;
    background-color: black;
    z-index: 1;
    display: none;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: calc(100vh - 5.1875rem);
  }
  #dropdown nav {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 2.5rem;
  }
  #dropdown a {
    text-decoration: none;
    color: white;
  }
  #dropdown a:last-child {
    background-color: rgb(217, 217, 217);
    background: rgba(217, 217, 217, 0.3);
    padding: .75rem 1.75rem;
    font-weight: bolder;
    border-radius: 2rem;
  }
  @media only screen and (max-width: 1020px) {
    #desktop-container {
      display: none;
    }
    #mobile-container {
      display: inline-block;
    }
    #dropdown {
      display: flex;
    }
  }
</style>