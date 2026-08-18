import {
  Drawer,
  Box,
  Typography,
  List,
  ListItemButton,
  ListItemText,
  Divider,
} from "@mui/material";

import { useNavigate, useLocation } from "react-router-dom";

const drawerWidth = 240;

function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();

  const menuItems = [
    { name: "Overview", path: "/" },
    { name: "Projects", path: "/projects" },
    { name: "API Changes", path: "/api-changes" },
    { name: "Impact Analysis", path: "/impact-analysis" },
    { name: "AI Repairs", path: "/ai-repairs" },
    { name: "Validation", path: "/validation" },
    
  ];

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: drawerWidth,
        flexShrink: 0,

        "& .MuiDrawer-paper": {
          width: drawerWidth,
          boxSizing: "border-box",
          backgroundColor: "#111820",
          borderRight: "1px solid #263241",
        },
      }}
    >
      {/* Logo */}
      <Box sx={{ p: 3 }}>
        <Typography
          variant="h5"
          sx={{
            fontWeight: 700,
            color: "#F8FAFC",
          }}
        >
          NovaGrid
        </Typography>

        <Typography
          variant="caption"
          sx={{
            color: "#94A3B8",
          }}
        >
          AI API Guardian
        </Typography>
      </Box>

      <Divider sx={{ borderColor: "#263241" }} />

      {/* Navigation */}
      <List sx={{ px: 1, py: 2 }}>
        {menuItems.map((item) => (
          <ListItemButton
            key={item.name}
            onClick={() => navigate(item.path)}
            selected={location.pathname === item.path}
            sx={{
              borderRadius: 2,
              mb: 0.5,

              "&:hover": {
                backgroundColor: "#171F2A",
              },

              "&.Mui-selected": {
                backgroundColor: "#1E293B",
              },

              "&.Mui-selected:hover": {
                backgroundColor: "#263241",
              },
            }}
          >
           <ListItemText
  primary={item.name}
  slotProps={{
    primary: {
      sx: {
        fontSize: 14,
        color: "#CBD5E1",
      },
    },
  }}
/> 
          </ListItemButton>
        ))}
      </List>
    </Drawer>
  );
}

export default Sidebar;