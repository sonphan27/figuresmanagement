<template lang="pug">
    v-container
        v-row.text-center
            v-col(cols="12")
                v-img(
                    :src="require('../assets/logo.svg')"
                    class="my-3"
                    contain
                    height="200")
        v-row
            v-btn(@click="getProducts")
                | Get Products
    </v-container>
</template>

<script>

export default {
    name: 'HelloWorld',

    data: () => ({
        ecosystem: [
            {
                text: 'vuetify-loader',
                href: 'https://github.com/vuetifyjs/vuetify-loader/tree/next',
            },
            {
                text: 'github',
                href: 'https://github.com/vuetifyjs/vuetify/tree/next',
            },
            {
                text: 'awesome-vuetify',
                href: 'https://github.com/vuetifyjs/awesome-vuetify',
            },
        ],
        importantLinks: [
            {
                text: 'Chat',
                href: 'https://community.vuetifyjs.com',
            },
            {
                text: 'Made with Vuetify',
                href: 'https://madewithvuejs.com/vuetify',
            },
            {
                text: 'Twitter',
                href: 'https://twitter.com/vuetifyjs',
            },
            {
                text: 'Articles',
                href: 'https://medium.com/vuetify',
            },
        ],
        whatsNext: [
            {
                text: 'Explore components',
                href: 'https://vuetifyjs.com',
            },
            {
                text: 'Roadmap',
                href: 'https://vuetifyjs.com/introduction/roadmap/',
            },
            {
                text: 'Frequently Asked Questions',
                href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
            },
        ],
    }),

    methods: {
        getProducts() {
            console.log('yolo111')
        }
    },
}
</script>
