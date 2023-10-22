<script lang="ts">
  import TechIcon from "$lib/TechIcon.svelte";
  import SvelteLogo from '$lib/assets/SvelteLogo.png'
</script>

<section>
  <h3>
    Made with ❤️ and with...
  </h3>
  <ul>
    <li>
      <TechIcon src={SvelteLogo} />
    </li>
    <li>
      <TechIcon src={SvelteLogo} />
    </li>
    <li>
      <TechIcon src={SvelteLogo} />
    </li>
    <li>
      <TechIcon src={SvelteLogo} />
    </li>
    <li>
      <TechIcon src={SvelteLogo} />
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
</style>