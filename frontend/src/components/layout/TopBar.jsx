import { AppBar, Toolbar, Typography, Box, TextField, Avatar } from "@mui/material";

function TopBar() {
  return (
    <AppBar
      position="static"
      sx={{
        backgroundColor: "#0B0F14",
        borderBottom: "1px solid #263241",
      }}
    >
      <Toolbar sx={{ display: "flex", justifyContent: "space-between" }}>

        <Box>
          <Typography
            variant="h5"
            sx={{ color: "#F8FAFC", fontWeight: 700 }}
          >
            Overview
          </Typography>

          <Typography sx={{ color: "#94A3B8" }}>
            Monitor your APIs and detect breaking changes
          </Typography>
        </Box>

        <Box sx={{ display: "flex", alignItems: "center", gap: 2 }}>

          <TextField
            size="small"
            placeholder="Search..."
          />

          <Typography sx={{ fontSize: 22 }}>
            🔔
          </Typography>

          <Avatar sx={{ backgroundColor: "#7C5CFF" }}>
            A
          </Avatar>

        </Box>

      </Toolbar>
    </AppBar>
  );
}

export default TopBar;