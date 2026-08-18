import { Box, Card, Typography } from "@mui/material";

function Dashboard() {
  return (
    <Box sx={{ p: 3 }}>

      <Typography
        variant="h5"
        sx={{ color: "white", mb: 3 }}
      >
        System Overview
      </Typography>

      <Box
        sx={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: 2,
        }}
      >

        <Card sx={{ backgroundColor: "#111820", p: 3 }}>
          <Typography sx={{ color: "#94A3B8" }}>
            APIs Monitored
          </Typography>

          <Typography
            variant="h3"
            sx={{ color: "white", mt: 1 }}
          >
            12
          </Typography>
        </Card>


        <Card sx={{ backgroundColor: "#111820", p: 3 }}>
          <Typography sx={{ color: "#94A3B8" }}>
            Risks Detected
          </Typography>

          <Typography
            variant="h3"
            sx={{ color: "#EF4444", mt: 1 }}
          >
            3
          </Typography>
        </Card>


        <Card sx={{ backgroundColor: "#111820", p: 3 }}>
          <Typography sx={{ color: "#94A3B8" }}>
            AI Repairs
          </Typography>

          <Typography
            variant="h3"
            sx={{ color: "#7C5CFF", mt: 1 }}
          >
            8
          </Typography>
        </Card>


        <Card sx={{ backgroundColor: "#111820", p: 3 }}>
          <Typography sx={{ color: "#94A3B8" }}>
            System Health
          </Typography>

          <Typography
            variant="h3"
            sx={{ color: "#22C55E", mt: 1 }}
          >
            96%
          </Typography>
        </Card>

      </Box>
            <Box
        sx={{
          mt: 4,
          backgroundColor: "#111820",
          border: "1px solid #263241",
          borderRadius: 3,
          p: 3,
        }}
      >
        <Typography
          variant="h6"
          sx={{
            color: "white",
            fontWeight: 600,
            mb: 2,
          }}
        >
          Recent API Changes
        </Typography>

        {/* Payment API */}
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            py: 2,
            borderBottom: "1px solid #263241",
          }}
        >
          <Box>
            <Typography sx={{ color: "white" }}>
              Payment API
            </Typography>

            <Typography
              variant="body2"
              sx={{ color: "#94A3B8", mt: 0.5 }}
            >
              Version 2.4 → 3.0
            </Typography>
          </Box>

          <Typography sx={{ color: "#EF4444", fontWeight: 600 }}>
            Breaking
          </Typography>
        </Box>

        {/* Authentication API */}
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            py: 2,
            borderBottom: "1px solid #263241",
          }}
        >
          <Box>
            <Typography sx={{ color: "white" }}>
              Authentication API
            </Typography>

            <Typography
              variant="body2"
              sx={{ color: "#94A3B8", mt: 0.5 }}
            >
              Version 1.8 → 1.9
            </Typography>
          </Box>

          <Typography sx={{ color: "#22C55E", fontWeight: 600 }}>
            Safe
          </Typography>
        </Box>

        {/* User API */}
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            py: 2,
          }}
        >
          <Box>
            <Typography sx={{ color: "white" }}>
              User API
            </Typography>

            <Typography
              variant="body2"
              sx={{ color: "#94A3B8", mt: 0.5 }}
            >
              Version 2.1 → 2.1
            </Typography>
          </Box>

          <Typography sx={{ color: "#7C5CFF", fontWeight: 600 }}>
            Stable
          </Typography>
        </Box>
      </Box>

    </Box>
  );
}

export default Dashboard;