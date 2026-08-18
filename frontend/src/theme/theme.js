import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
  palette: {
    mode: "dark",

    primary: {
      main: "#7C5CFF",
    },

    success: {
      main: "#22C55E",
    },

    warning: {
      main: "#F59E0B",
    },

    error: {
      main: "#EF4444",
    },

    background: {
      default: "#0B0F14",
      paper: "#111820",
    },
  },

  shape: {
    borderRadius: 10,
  },

  typography: {
    fontFamily: "Inter, Arial, sans-serif",
  },
});