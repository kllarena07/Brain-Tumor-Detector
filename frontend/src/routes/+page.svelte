<script lang="ts">
	import Footer from "$lib/Footer.svelte";
  import Navbar from "$lib/Navbar.svelte";
	import UploadForm from "$lib/UploadForm.svelte";
	import TechStack from "$lib/TechStack.svelte";
	import OurTeam from "$lib/OurTeam.svelte";
	import About from "$lib/About.svelte";
	import Hero from "$lib/Hero.svelte";
</script>

<Navbar />
<main>
  <Hero />
  <About />
  <section id="demo">
    <UploadForm />
  </section>
  <OurTeam />
  <TechStack />
</main>
<Footer />