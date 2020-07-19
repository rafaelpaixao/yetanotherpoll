<template>
  <v-row class="justify-center">
    <v-col lg="4" md="6" sm="8" cols="12">
      <v-row>
        <v-col class="text-left">
          <slot name="topleft">
            <h6 class="mb-3 text-h6 text-uppercase font-weight-black">
              <slot name="title" />
            </h6>
          </slot>
        </v-col>
        <v-col class="text-right">
          <slot name="topright" />
        </v-col>
      </v-row>
      <slot />
      <v-row>
        <v-col sm="6" cols="12" class="text-left">
          <slot name="bottomleft" />
        </v-col>
        <v-col sm="6" cols="12">
          <slot name="bottomright" class="text-right" />
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
