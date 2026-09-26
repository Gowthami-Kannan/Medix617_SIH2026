// ============================================================
// OmniCare TinyML — 7 Channel Version
// ESP32-S3 / Arduino IDE
// ============================================================

#include <Arduino.h>
#include <math.h>

#define ALPHA               0.005
#define STD_FLOOR           0.1
#define Z_THRESHOLD         3.0
#define PLATEAU_MIN_SAMPLES 40
#define WARMUP_SAMPLES      30
#define N_CHANNELS          7

struct ZEngine {
  long   n;
  double mean;
  double M2;
  double ema_mean;
  double ema_std;
  bool   initialized;
};

ZEngine ch[N_CHANNELS];

const char* ch_name[N_CHANNELS] = {
  "HR", "SpO2", "EDA", "SkinTemp", "AmbTemp", "Motion", "PM2.5"
};

void z_init(ZEngine *e) {
  e->n = 0;
  e->mean = 0.0;
  e->M2 = 0.0;
  e->ema_mean = 0.0;
  e->ema_std = 0.0;
  e->initialized = false;
}

double z_update(ZEngine *e, double x) {
  e->n++;
  double d = x - e->mean;
  e->mean += d / e->n;
  e->M2 += d * (x - e->mean);

  if (e->n < 2) return 0.0;

  double v = e->M2 / (e->n - 1);
  if (v < 0) v = 0;
  double s = sqrt(v);

  if (!e->initialized) {
    e->ema_mean = e->mean;
    e->ema_std = (s > STD_FLOOR) ? s : STD_FLOOR;
    e->initialized = true;
  } else {
    e->ema_mean = ALPHA * e->mean + (1.0 - ALPHA) * e->ema_mean;
    double ns = ALPHA * s + (1.0 - ALPHA) * e->ema_std;
    e->ema_std = (ns > STD_FLOOR) ? ns : STD_FLOOR;
  }

  double z = (x - e->ema_mean) / e->ema_std;
  if (z >  10.0) z =  10.0;
  if (z < -10.0) z = -10.0;
  return z;
}

int run_length = 0;

int classifyPattern(double fused, int sample_idx) {
  if (sample_idx < WARMUP_SAMPLES) return 0;

  if (fused > Z_THRESHOLD) {
    run_length++;
    return 0;
  }
  if (run_length > 0) {
    int e = (run_length >= PLATEAU_MIN_SAMPLES) ? 2 : 1;
    run_length = 0;
    return e;
  }
  return 0;
}

void printConditions(int dominant_ch, int event) {
  Serial.print("Possible Condition: ");
  if (event == 1) {
    switch (dominant_ch) {
      case 0: Serial.println("Acute Stress / Heat Stress / Cardiac Event"); break;
      case 1: Serial.println("Respiratory Risk / Hypoxia / Breathing Difficulty"); break;
      case 2: Serial.println("Acute Stress / Pain / Startle Response"); break;
      case 3: Serial.println("Fever / Heat Stress / Infection"); break;
      case 4: Serial.println("Heat Stress / Environmental Risk"); break;
      case 5: Serial.println("Fall Detected / Seizure / Sudden Movement"); break;
      case 6: Serial.println("Respiratory Risk / Air Quality Alert"); break;
    }
  } else {
    switch (dominant_ch) {
      case 0: Serial.println("Fever / Heat Exhaustion / Dehydration"); break;
      case 1: Serial.println("Respiratory Risk / Hypoxia"); break;
      case 2: Serial.println("Dehydration / Sustained Stress / Heat Exhaustion"); break;
      case 3: Serial.println("Fever / Heat Stress / Infection"); break;
      case 4: Serial.println("Sustained Heat Stress / Environmental Risk"); break;
      case 5: Serial.println("Fatigue / Prolonged Movement / Seizure"); break;
      case 6: Serial.println("Respiratory Risk / Air Quality Alert"); break;
    }
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println();
  Serial.println("======================================");
  Serial.println("    OmniCare TinyML — 7 Channel");
  Serial.println("======================================");
  Serial.println("Welford + EMA + Z-score");
  Serial.println("7-channel fusion (MAX)");
  Serial.println("Spike / Plateau Classification");
  Serial.println("--------------------------------------");

  for (int i = 0; i < N_CHANNELS; i++) z_init(&ch[i]);

  Serial.println("System Ready");
  Serial.println("--------------------------------------");
}

void loop() {
  static int i = 0;

  // ---- SIMULATED VALUES ----
  double vals[N_CHANNELS] = {
    70.0 + ((i % 20) - 10) * 0.3,
    98.0 + ((i % 20) - 10) * 0.1,
    0.50 + ((i % 20) - 10) * 0.005,
    36.5 + ((i % 20) - 10) * 0.02,
    28.0 + ((i % 20) - 10) * 0.05,
    0.10 + ((i % 20) - 10) * 0.002,
    35.0 + ((i % 20) - 10) * 0.2
  };

  // Test events
  if (i >= 60 && i < 63) {
    vals[0] = 115.0;
    vals[2] = 1.20;
  }
  if (i >= 180 && i < 220) {
    vals[3] = 39.5;
  }

  double absz[N_CHANNELS];
  for (int c = 0; c < N_CHANNELS; c++) {
    double z = z_update(&ch[c], vals[c]);
    absz[c] = fabs(z);
  }

  double fused = 0.0;
  for (int c = 0; c < N_CHANNELS; c++) {
    if (absz[c] > fused) fused = absz[c];
  }

  int ev = classifyPattern(fused, i);

  if (ev == 1 || ev == 2) {
    int dom = 0;
    for (int c = 1; c < N_CHANNELS; c++) {
      if (absz[c] > absz[dom]) dom = c;
    }

    Serial.print("i=");
    Serial.print(i);
    Serial.print("  FUSED=");
    Serial.print(fused, 2);
    Serial.print("  DOMINANT=");
    Serial.println(ch_name[dom]);

    if (ev == 1) Serial.println("  >>> SPIKE ALERT");
    else          Serial.println("  >>> PLATEAU WARNING");

    printConditions(dom, ev);
    Serial.println();
  }

  i++;
  delay(250);
}
