const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    proxy: {
      '^/(api|docs|openapi.json|redoc)': {
        target: 'http://api:8000',
        ws: true,
        changeOrigin: true
      },
    },
    static: {
        watch: {
            ignored: "/node_modules/",
            usePolling: true,
        },
    },
  },

  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  }
})
