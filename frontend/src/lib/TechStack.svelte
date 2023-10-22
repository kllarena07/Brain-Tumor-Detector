<script lang="ts">
  import TechIcon from "$lib/TechIcon.svelte";
  import SvelteLogo from '$lib/assets/SvelteLogo.png'
  import YoloLogo from '$lib/assets/yolo.png'
  import FigmaLogo from '$lib/assets/figma.png'
  import VercelLogo from '$lib/assets/vercel.png'
</script>

<section>
  <h3>Made with ❤️ and with...</h3>
  <ul>
    <li>
      <TechIcon src={SvelteLogo} />
    </li>
    <li>
      <TechIcon src={YoloLogo} />
    </li>
    <li>
      <TechIcon src={FigmaLogo} />
    </li>
    <li>
      <TechIcon src={VercelLogo} />
    </li>
  </ul>
</section>

<style>
  h3 {
    text-align: center;
    color: white;
  }
  ul {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    list-style: none;
  }
  @media only screen and (max-width: 1020px) {
    ul {
      margin-bottom: 2rem;
    }
  }
</style>