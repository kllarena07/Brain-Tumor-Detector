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
      <Portrait src={Moumen} name="Moumen Msallaty" role="Data Scientist / Lead ML Engineer" />
    </li>
    <li>
      <Portrait src={Kieran} name="Kieran Llarena" role="Designer / Fullstack Engineer" />
    </li>
    <li>
      <Portrait src={Jawad} name="Jawad Mourad" role="Frontend Engineer" />
    </li>
    <li>
      <Portrait src={Madhi} name="Mahdi Rizk" role="Data Scientist" />
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
  @media only screen and (width <= 1020px) {
    ul {
      display: flex;
      flex-direction: column;
    }
  }
  @media only screen and (max-width: 1650px) {
    #our-team {
      transform: scale(0.9);
    }
  }
</style>