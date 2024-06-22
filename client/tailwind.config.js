/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      keyframes: {
        typing: {
          "0%": { width: "0%", visibility: "hidden" },
          "100%": { width: "100%", visibility: "visible" }
        },
        blink: {
          "0%, 100%": { borderColor: "white" },
          "50%": { borderColor: "transparent" }
        }
      },
      animation: {
        typing: "typing 3s steps(60, end)   alternate , blink 0.7s step-end infinite"
      },
      boxShadow: {
        default: '4px 4px 10px',
      },
    },
  },
  plugins: [],
};
