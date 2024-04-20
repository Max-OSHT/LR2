<template>
  <header>
    <nav class="navbar navbar-expand-sm">
      <div class="container mt-0">
        <div class="align-top" loading="lazy" id="label">
          <router-link :to="{ name: 'inside' }" id="logo"> Log Profile </router-link>
        </div>
        <button class="navbar-toggler ms-auto" type="button" data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
          aria-label="Переключатель навигации">
          <span>
            <svg class="icon" width="30" height="25">
              <use xlink:href="#align_text_distribute [#914]"></use>
            </svg>
          </span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="d-flex justify-content-center navbar-nav mx-auto w-100" id="navbar">
            <div class="nav-item m-2 px-2">
              <router-link :to="{ name: 'info' }"> Info </router-link>
            </div>
            <div class="nav-item m-2 px-2">
              <router-link :to="{ name: 'warning' }"> Warning </router-link>
            </div>
            <div class="nav-item m-2 px-2">
              <router-link :to="{ name: 'error' }"> Error </router-link>
            </div>
            <div class="nav-item m-2 px-2">
              <router-link :to="{ name: 'critical' }"> Critical </router-link>
            </div>
            <button type="button" id="Out" class="btn btn-outline-light" @click="outBtn">Выйти</button>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>

export default {
  data() {
    return {
      isAuthorized: true
    }
  },
  methods: {
    outBtn() {
      if (this.isAuthorized) {
        this.$router.push({ name: 'home' })
      }
    }
  }
}
</script>

<style lang="scss" scoped>
header {
  background-color: #0c0c0c;
  padding: 20px 0;

  a {
    text-decoration: none;
    font-weight: 700;
    color: #ffffff;
    font-size: 25px;
  }

  #logo{
    color: rgb(51, 182, 123);
    font-size: 30px;
  }

  button {
    margin-left: auto;
    border-width: 3px;
    border-color: rgb(51, 182, 123);
  }
  ul > div {
    border-color: rgb(51, 182, 123);
  }
  @media (max-width: 700px) {
    #label {
      display: none;
      visibility: hidden;
    }
    #navbarSupportedContent {
      width: 100%;
    }
  }
  @media (max-width: 575.98px) {
    #navbarSupportedContent {
      text-align: center;
    }
    #Out {
      width: 100%;
      margin-top: 10px;
    }
    #label {
      display: block;
      visibility: visible;
    }
  }
}
</style>
