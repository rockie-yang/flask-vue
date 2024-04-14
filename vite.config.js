import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      // string shorthand: http://localhost:5173/api -> http://localhost:8000/api
      '/api': 'http://localhost:8000',
    }
  },
  build: {
    assetsDir: "static",
  },
})
