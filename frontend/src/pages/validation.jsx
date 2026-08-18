import {
  Box,
  Typography,
  Card,
  CardContent,
  Chip,
  Button,
} from "@mui/material";

function Validation() {
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
        Validation
      </Typography>

      <Typography
        sx={{
          color: "#94A3B8",
          mb: 3,
        }}
      >
        Test AI-generated repairs before applying them to your application
      </Typography>

      {/* Payment API */}
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
                Payment API Repair
              </Typography>

              <Typography
                variant="body2"
                sx={{
                  color: "#94A3B8",
                  mt: 1,
                }}
              >
                Testing compatibility with API v3.0
              </Typography>
            </Box>

            <Chip
              label="PASSED"
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
            All required API requests completed successfully.
          </Typography>

          <Typography
            sx={{
              color: "#94A3B8",
              mt: 1,
            }}
          >
            12 / 12 test cases passed
          </Typography>

          <Button
            variant="outlined"
            sx={{
              mt: 2,
              color: "#7C5CFF",
              borderColor: "#7C5CFF",
            }}
          >
            View Tests
          </Button>
        </CardContent>
      </Card>

      {/* Authentication API */}
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
                Authentication API Repair
              </Typography>

              <Typography
                variant="body2"
                sx={{
                  color: "#94A3B8",
                  mt: 1,
                }}
              >
                Testing endpoint compatibility
              </Typography>
            </Box>

            <Chip
              label="WARNING"
              sx={{
                color: "#F59E0B",
                backgroundColor: "#F59E0B20",
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
            One test case detected an unexpected response format.
          </Typography>

          <Typography
            sx={{
              color: "#94A3B8",
              mt: 1,
            }}
          >
            11 / 12 test cases passed
          </Typography>

          <Button
            variant="outlined"
            sx={{
              mt: 2,
              color: "#F59E0B",
              borderColor: "#F59E0B",
            }}
          >
            Investigate
          </Button>
        </CardContent>
      </Card>

      {/* Validation Summary */}
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
            Validation Summary
          </Typography>

          <Typography
            sx={{
              color: "#94A3B8",
              mt: 2,
            }}
          >
            24 total test cases executed
          </Typography>

          <Typography
            sx={{
              color: "#22C55E",
              mt: 1,
              fontWeight: 600,
            }}
          >
            23 tests passed
          </Typography>

          <Typography
            sx={{
              color: "#F59E0B",
              mt: 1,
              fontWeight: 600,
            }}
          >
            1 test requires attention
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
            Run Validation
          </Button>
        </CardContent>
      </Card>
    </Box>
  );
}

export default Validation;