<script lang="ts">
  import UploadIcon from '$lib/assets/upload-icon.png'

  let heroImage : string

  const onFileSelected = ({ target }) => {
    const image = target?.files[0];
    const reader = new FileReader();
    
    reader.readAsDataURL(image);
    reader.onload = e => {
      e.target?.result ? heroImage = e.target?.result : heroImage = ''
    }
  }
</script>

<form>
  <h2>Upload</h2>
  <div id="file-upload-container">
    <div id="icon-container">
      <img src={UploadIcon} />
      <p id="instructions">Drag and drop <span class="gradient bold">here</span></p>
    </div>
    <img id="hero-image-preview" src={heroImage} alt='' />
    <input required id="hero-image-upload" name="heroImage" type="file" accept="image/png, image/jpeg, image/jpg" on:change={(e) => onFileSelected(e)} />
  </div>
  <button class="bold" type="submit">Get results</button>
</form>

<style>
  form {
    display: flex;
    flex-direction: column;
    margin: 5rem;
    padding: 2rem;
    background: radial-gradient(#070707, #020202);
    border-radius: 3rem;
    transition: box-shadow 200ms ease;
  }
  form:hover {
    box-shadow: 0 0 1.875rem -1.25rem #FFFFFF;
    transition: box-shadow 200ms ease;
  }
  h2 {
    font-size: 3rem;
    margin: 2rem;
    color: white;
  }
  #file-upload-container {
    background-color: #141416;
    position: relative;
    margin: auto;
    width: 80%;
    aspect-ratio: 1600 / 751;
    border-radius: 50px;
  }
  #hero-image-preview {
    position: absolute;
    width: 100%;
    aspect-ratio: 1600 / 751;
    object-fit: cover;
  }
  #hero-image-preview {
    display: none;
  }
  #hero-image-preview[src] {
   display: block;
  }
  #hero-image-upload {
    position: absolute;
    width: 100%;
    height: 100%;
    opacity: 0;
    cursor: pointer;
  }
  #icon-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 2rem;
    align-items: center;
    position: absolute;
    width: 100%;
    height: 100%;
    color: white;
  }
  #instructions {
    font-size: 1.25rem;
  }
  button {
    padding: 1rem 3rem;
    color: white;
    margin: 1.5rem auto;
    border: none;
    cursor: pointer;
    background: linear-gradient(to right, #2E4EBD, #DB00FF);
    border-radius: 2rem;
    font-size: 1.15rem;
  }
  .gradient {
    background: linear-gradient(to left, #FF00E5, #9E00FF);
    background-clip: text;
    color: transparent;
    -webkit-text-fill-color: transparent; 
    -webkit-background-clip: text;
  }
  .bold {
    font-weight: bold;
  }
</style>