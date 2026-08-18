import {
  Box,
  Typography,
  Card,
  CardContent,
  Chip,
  Button,
} from "@mui/material";

function AIRepairs() {
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
        AI Repairs
      </Typography>

      <Typography
        sx={{
          color: "#94A3B8",
          mb: 3,
        }}
      >
        AI-generated solutions for detected API issues
      </Typography>

      {/* Repair 1 */}
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
                Payment API Repair
              </Typography>

              <Typography
                variant="body2"
                sx={{ color: "#94A3B8", mt: 1 }}
              >
                Required parameter removed in v3.0
              </Typography>
            </Box>

            <Chip
              label="AI SUGGESTION"
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
            AI recommends updating the payment request payload
            and replacing the removed parameter.
          </Typography>

          <Typography
            sx={{
              color: "#94A3B8",
              mt: 2,
            }}
          >
            Estimated confidence: 94%
          </Typography>

          <Button
            variant="contained"
            sx={{
              mt: 2,
              backgroundColor: "#7C5CFF",
              "&:hover": {
                backgroundColor: "#6848E8",
              },
            }}
          >
            Review Repair
          </Button>
        </CardContent>
      </Card>

      {/* Repair 2 */}
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
                Authentication API Repair
              </Typography>

              <Typography
                variant="body2"
                sx={{ color: "#94A3B8", mt: 1 }}
              >
                Endpoint structure changed
              </Typography>
            </Box>

            <Chip
              label="READY"
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
            AI detected a compatible endpoint update with no
            breaking changes required.
          </Typography>

          <Typography
            sx={{
              color: "#94A3B8",
              mt: 2,
            }}
          >
            Estimated confidence: 98%
          </Typography>

          <Button
            variant="outlined"
            sx={{
              mt: 2,
              color: "#7C5CFF",
              borderColor: "#7C5CFF",
            }}
          >
            Review Repair
          </Button>
        </CardContent>
      </Card>

      {/* Repair Statistics */}
      <Card
        sx={{
          backgroundColor: "#111820",
          border: "1px solid #263241",
          borderRadius: 3,
        }}
      >
        <CardContent>
          <Typography
            variant="h6"
            sx={{
              color: "#F8FAFC",
              fontWeight: 600,
            }}
          >
            Repair Statistics
          </Typography>

          <Typography
            sx={{
              color: "#94A3B8",
              mt: 2,
            }}
          >
            8 AI repairs generated
          </Typography>

          <Typography
            sx={{
              color: "#22C55E",
              mt: 1,
              fontWeight: 600,
            }}
          >
            6 repairs successfully validated
          </Typography>

          <Typography
            sx={{
              color: "#7C5CFF",
              mt: 1,
              fontWeight: 600,
            }}
          >
            94% average AI confidence
          </Typography>
        </CardContent>
      </Card>
    </Box>
  );
}

export default AIRepairs;