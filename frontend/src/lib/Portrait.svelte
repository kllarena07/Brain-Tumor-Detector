<script lang="ts">
  export let src : string
  export let name : string
  export let role : string
</script>

<div>
  <img src={src} alt="{name}'s portrait" />
  <p id="name">{name}</p>
  <p id="role">{role}</p>
</div>

<style>
  #name {
    color: white;
    font-weight: bold;
    text-align: center;
    margin-top: 1rem;
  }
  #role {
    font-style: italic;
    color: white;
    text-align: center;
  }
</style>