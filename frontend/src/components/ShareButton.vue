<template>
  <v-dialog v-model="dialog" width="250">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="warning" v-bind="attrs" v-on="on">Share this poll</v-btn>
    </template>

    <v-card>
      <v-toolbar dense>
        <v-toolbar-title>Share this poll</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon @click="dialog = false">mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text class="vue-social-sharing pt-5">
        <ShareNetwork
          v-for="network in networks"
          :network="network.network"
          :key="network.network"
          :style="{backgroundColor: network.color}"
          :url="sharing.url"
          :title="sharing.title"
          :description="sharing.description"
          :quote="sharing.quote"
          :hashtags="sharing.hashtags"
          :twitterUser="sharing.twitterUser"
        >
          <i :class="network.icon"></i>
          <span>{{ network.name }}</span>
        </ShareNetwork>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    poll: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      dialog: false,
      sharing: {
        url: window.location.href,
        title: this.poll.title,
        description: this.poll.description,
        quote: this.poll.title,
        hashtags: 'poll,yetanotherpoll',
        twitterUser: 'yetanotherpoll'
      },
      networks: [
        { network: 'email', name: 'Email', icon: 'far fah fa-lg fa-envelope', color: '#333333' },
        { network: 'facebook', name: 'Facebook', icon: 'fab fah fa-lg fa-facebook-f', color: '#1877f2' },
        { network: 'linkedin', name: 'LinkedIn', icon: 'fab fah fa-lg fa-linkedin', color: '#007bb5' },
        { network: 'reddit', name: 'Reddit', icon: 'fab fah fa-lg fa-reddit-alien', color: '#ff4500' },
        { network: 'skype', name: 'Skype', icon: 'fab fah fa-lg fa-skype', color: '#00aff0' },
        { network: 'telegram', name: 'Telegram', icon: 'fab fah fa-lg fa-telegram-plane', color: '#0088cc' },
        { network: 'twitter', name: 'Twitter', icon: 'fab fah fa-lg fa-twitter', color: '#1da1f2' },
        { network: 'whatsapp', name: 'Whatsapp', icon: 'fab fah fa-lg fa-whatsapp', color: '#25d366' },
      ]
    }
  }
}
</script>
<style lang="scss" scoped>
.vue-social-sharing {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica,
    Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';
  #share-network-list {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 1000px;
    margin: auto;
  }

  a[class^='share-network-'] {
    flex: none;
    color: #ffffff;
    background-color: #333;
    border-radius: 3px;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-content: center;
    align-items: center;
    cursor: pointer;
    margin: 0 10px 10px 0;
  }

  a[class^='share-network-'] .fah {
    background-color: rgba(0, 0, 0, 0.2);
    padding: 10px;
    flex: 0 1 auto;
  }

  a[class^='share-network-'] span {
    padding: 0 10px;
    flex: 1 1 0%;
    font-weight: 500;
  }

  a.share-network-twitter {
    background-color: #1da1f2;
  }

  a.share-network-fakeblock {
    background-color: #41b883;
  }
}
</style>
