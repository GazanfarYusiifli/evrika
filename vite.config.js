import { defineConfig } from 'vite';
import { resolve } from 'path';
import fs from 'fs';

// Get all HTML files in the root directory
const htmlFiles = fs.readdirSync(__dirname)
  .filter(file => file.endsWith('.html') && file !== 'index.html')
  .reduce((acc, file) => {
    const name = file.replace('.html', '');
    acc[name] = resolve(__dirname, file);
    return acc;
  }, {
    main: resolve(__dirname, 'index.html'),
  });

export default defineConfig({
  base: './',
  server: {
    port: 3000,
    open: true,
  },
  build: {
    rollupOptions: {
      input: htmlFiles,
    },
  },
});
