<script lang="ts">
	import Portrait from "./Portrait.svelte";
  import Moumen from '$lib/assets/Moumen.png'
  import Kieran from '$lib/assets/Kieran.png'
  import Jawad from '$lib/assets/Jawad.png'
  import Madhi from '$lib/assets/Madhi.png'
</script>
<section id="our-team">
  <h2 class="bold">Our Team</h2>
  <ul>
    <li>
      <Portrait src={Moumen} name="Moumen Msallaty" role="ML Engineer" />
    </li>
    <li>
      <Portrait src={Kieran} name="Kieran Llarena" role="Fullstack Engineer" />
    </li>
    <li>
      <Portrait src={Jawad} name="Jawad Mourad" role="Frontend Engineer" />
    </li>
    <li>
      <Portrait src={Madhi} name="Madhi Rizk" role="Data Scientist" />
    </li>
  </ul>
</section>

<style>
  section {
    margin-bottom: 5rem;
  }
  h2 {
    font-size: 3rem;
    color: white;
    text-align: center;
    margin-bottom: 1.25rem;
  }
  ul {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 3rem;
    padding: 0;
    list-style: none;
  }
</style>