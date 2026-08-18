import {
  Box,
  Typography,
  Card,
  CardContent,
  Button,
  Chip,
  TextField,
} from "@mui/material";

import { useState } from "react";

function Projects() {
    const [showConnect, setShowConnect] = useState(false);
  return (
    <Box>
      <Typography
        variant="h5"
        sx={{
          color: "#F8FAFC",
          fontWeight: 700,
          mb: 1,
        }}
      >
        Projects
      </Typography>

      <Typography
        sx={{
          color: "#94A3B8",
          mb: 3,
        }}
      >
        Manage your connected repositories and projects.
      </Typography>

      <Card
        sx={{
          backgroundColor: "#111827",
          border: "1px solid #1E293B",
          color: "#F8FAFC",
        }}
      >
        <CardContent>
          <Box
            sx={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              mb: 2,
            }}
          >
            <Box>
              <Typography
                variant="h6"
                sx={{ fontWeight: 600 }}
              >
                Connected Repository
              </Typography>

              <Typography
                sx={{
                  color: "#94A3B8",
                  mt: 0.5,
                }}
              >
                Connect a repository to monitor API changes.
              </Typography>
            </Box>

            <Chip
              label="Connected"
              sx={{
                backgroundColor: "#064E3B",
                color: "#6EE7B7",
              }}
            />
          </Box>

          <Button
            variant="contained"
            onClick={() => setShowConnect(!showConnect)}
            sx={{
              backgroundColor: "#2563EB",
              textTransform: "none",
              mt: 2,
            }}
          >
            Connect Repository
          </Button>
          {showConnect && (
  <Box sx={{ mt: 3 }}>
    <Typography
      sx={{
        color: "#F8FAFC",
        fontWeight: 600,
        mb: 2,
      }}
    >
      Connect Repository
    </Typography>

    <TextField
      fullWidth
      label="Repository URL"
      placeholder="https://github.com/username/repository"
      sx={{
        mb: 2,
        "& .MuiInputLabel-root": {
          color: "#94A3B8",
        },
        "& .MuiOutlinedInput-root": {
          color: "#F8FAFC",
          "& fieldset": {
            borderColor: "#334155",
          },
        },
      }}
    />

    <Button
      variant="contained"
      sx={{
        backgroundColor: "#2563EB",
        textTransform: "none",
      }}
    >
      Connect
    </Button>
  </Box>
)}
        </CardContent>
      </Card>
    </Box>
  );
}

export default Projects;