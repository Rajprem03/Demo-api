import {
  Box,
  Typography,
  Card,
  CardContent,
  Chip,
  Button,
} from "@mui/material";

function ApiChanges() {
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
        API Changes
      </Typography>

      <Typography
        sx={{
          color: "#94A3B8",
          mb: 3,
        }}
      >
        Detect and review changes in your monitored APIs
      </Typography>

      {/* Change 1 */}
      <Card
        sx={{
          backgroundColor: "#111820",
          border: "1px solid #3A2428",
          borderRadius: 3,
          mb: 2,
        }}
      >
        <CardContent>
          <Box
            sx={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <Box>
              <Typography
                variant="h6"
                sx={{ color: "#F8FAFC" }}
              >
                Payment API
              </Typography>

              <Typography
                variant="body2"
                sx={{ color: "#94A3B8", mt: 1 }}
              >
                Version 2.4 → 3.0
              </Typography>
            </Box>

            <Chip
              label="BREAKING CHANGE"
              sx={{
                color: "#EF4444",
                backgroundColor: "#EF444420",
                fontWeight: 600,
              }}
            />
          </Box>

          <Typography
            sx={{
              color: "#CBD5E1",
              mt: 3,
            }}
          >
            Required parameter removed from the payment request.
          </Typography>

          <Button
            variant="outlined"
            sx={{
              mt: 2,
              color: "#7C5CFF",
              borderColor: "#7C5CFF",
            }}
          >
            Analyze Impact
          </Button>
        </CardContent>
      </Card>

      {/* Change 2 */}
      <Card
        sx={{
          backgroundColor: "#111820",
          border: "1px solid #263241",
          borderRadius: 3,
          mb: 2,
        }}
      >
        <CardContent>
          <Box
            sx={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <Box>
              <Typography
                variant="h6"
                sx={{ color: "#F8FAFC" }}
              >
                Authentication API
              </Typography>

              <Typography
                variant="body2"
                sx={{ color: "#94A3B8", mt: 1 }}
              >
                Version 1.8 → 1.9
              </Typography>
            </Box>

            <Chip
              label="SAFE"
              sx={{
                color: "#22C55E",
                backgroundColor: "#22C55E20",
                fontWeight: 600,
              }}
            />
          </Box>

          <Typography
            sx={{
              color: "#CBD5E1",
              mt: 3,
            }}
          >
            Authentication endpoint updated without breaking
            existing requests.
          </Typography>

          <Button
            variant="outlined"
            sx={{
              mt: 2,
              color: "#7C5CFF",
              borderColor: "#7C5CFF",
            }}
          >
            View Details
          </Button>
        </CardContent>
      </Card>

      {/* Change 3 */}
      <Card
        sx={{
          backgroundColor: "#111820",
          border: "1px solid #263241",
          borderRadius: 3,
        }}
      >
        <CardContent>
          <Box
            sx={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <Box>
              <Typography
                variant="h6"
                sx={{ color: "#F8FAFC" }}
              >
                User API
              </Typography>

              <Typography
                variant="body2"
                sx={{ color: "#94A3B8", mt: 1 }}
              >
                Version 2.1 → 2.1
              </Typography>
            </Box>

            <Chip
              label="STABLE"
              sx={{
                color: "#7C5CFF",
                backgroundColor: "#7C5CFF20",
                fontWeight: 600,
              }}
            />
          </Box>

          <Typography
            sx={{
              color: "#CBD5E1",
              mt: 3,
            }}
          >
            No breaking changes detected in the latest version.
          </Typography>

          <Button
            variant="outlined"
            sx={{
              mt: 2,
              color: "#7C5CFF",
              borderColor: "#7C5CFF",
            }}
          >
            View Details
          </Button>
        </CardContent>
      </Card>
    </Box>
  );
}

export default ApiChanges;