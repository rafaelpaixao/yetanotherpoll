<template>
  <v-row justify="center">
    <v-col lg="4" md="6" sm="8" cols="12">
      <h6 class="mb-3 text-h6 text-uppercase font-weight-black">
        <slot name="title" />
      </h6>
      <slot />
      <div class="text-center my-5">
        <slot name="footer" />
      </div>
    </v-col>
  </v-row>
</template>
