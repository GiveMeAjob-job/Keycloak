module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        primary: '#8B5CF6',
        accent: '#34D399'
      }
    }
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: [
      {
        light: {
          primary: '#8B5CF6',
          accent: '#34D399'
        }
      },
      'dark'
    ]
  }
};
